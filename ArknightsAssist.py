# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, pyqtSignal
from MyHelper import *
import ArknightsThread
import ui_arknights_assist
import win32com.client


class ArknightsAssist(QWidget):
    stop_signal = pyqtSignal(int)

    def __init__(self):
        QWidget.__init__(self)
        self.ui = ui_arknights_assist.Ui_ArknightsAssist()
        self.init_ui()
        self.thread = None
        try:
            self.main_ts = win32com.client.Dispatch('ts.tssoft')
        except:
            logger.error("加载天使插件失败")
            self.ui.pushButton_start.setEnabled(False)

    def init_ui(self):
        self.ui.setupUi(self)
        self.ui.spinBox_count.setEnabled(False)
        self.ui.spinBox_auto_feed.setEnabled(False)
        self.ui.pushButton_stop.setEnabled(False)
        XStream.stdout().messageWritten.connect(self.ui.textBrowser.append)
        XStream.stderr().messageWritten.connect(self.ui.textBrowser.append)
        self.ui.checkBox_count.stateChanged.connect(self.on_checkbox_clicked)
        self.ui.checkBox_auto_feed.stateChanged.connect(self.on_checkbox_clicked)
        self.ui.pushButton_start.clicked.connect(self.on_start_button_clicked)
        self.ui.pushButton_stop.clicked.connect(self.on_stop_button_clicked)
        self.ui.pushButton_log_level.setCheckable(True)
        self.ui.pushButton_log_level.clicked[bool].connect(self.on_log_level_clicked)
        self.stop_signal.connect(self.stop_thread)

    def on_log_level_clicked(self, pressed):
        if pressed:
            logger.info('当前日志等级调整为：详细')
            self.ui.pushButton_log_level.setText('当前日志等级：详细')
            logger.setLevel(logging.DEBUG)
        else:
            logger.info('当前日志等级调整为：精简')
            self.ui.pushButton_log_level.setText('当前日志等级：精简')
            logger.setLevel(logging.INFO)

    def on_checkbox_clicked(self):
        self.ui.spinBox_count.setEnabled(True if self.ui.checkBox_count.checkState() == Qt.Checked else False)
        self.ui.spinBox_auto_feed.setEnabled(True if self.ui.checkBox_auto_feed.checkState() == Qt.Checked else False)

    def detect_mumu_window(self):
        hwnd_raw = self.main_ts.EnumWindowByProcess("NemuPlayer.exe", "", "", 16)
        handler_list = hwnd_raw.split(',')
        if handler_list == [''] or len(handler_list) < 2:
            logger.error('未检测到运行中的窗口')
            return False
        handler = handler_list[1]
        ts = win32com.client.Dispatch('ts.tssoft')
        if ts.BindWindow(handler, 'dx2', 'windows', 'windows', 0) != 1:
            logger.error('窗口绑定失败')
            return False
        size = ts.GetClientSize(handler)  # size: (ret, width, height)
        if size[1] != 1440 or size[2] != 899:
            logger.info('%d %d' % (size[1], size[2]))
            rect = ts.GetWindowRect(handler)  # rect: (ret, x1, y1, x2, y2)
            ts.SetClientSize(handler, 1440, 899)
            ts.MoveWindow(handler, rect[1], rect[2])
        count = self.ui.spinBox_count.value() if self.ui.checkBox_count.checkState() == Qt.Checked else 0
        feed = self.ui.spinBox_auto_feed.value() if self.ui.checkBox_auto_feed.checkState() == Qt.Checked else 0
        arknights_thread = ArknightsThread.ArknightsThread(self, ts)
        arknights_thread.set_counts(count, feed)
        arknights_thread.setName('0')
        self.thread = arknights_thread
        return True

    def on_start_button_clicked(self):
        if not self.detect_mumu_window():
            return
        self.ui.pushButton_stop.setEnabled(True)
        self.ui.pushButton_start.setEnabled(False)
        self.ui.checkBox_count.setEnabled(False)
        self.ui.checkBox_auto_feed.setEnabled(False)
        self.ui.spinBox_count.setEnabled(False)
        self.ui.spinBox_auto_feed.setEnabled(False)
        keep_awake()
        logger.debug('线程启动')
        self.thread.start()

    def on_stop_button_clicked(self):
        if self.ui.checkBox_shutdown.checkState():
            logger.info('任务被手动停止，取消[完成后关机]')
            self.ui.checkBox_shutdown.setCheckState(Qt.Unchecked)
        self.stop()

    def stop(self):
        if self.thread is not None:
            self.thread.stop()
            self.thread.unbind_window()
            self.thread.join()
            self.thread = None
            logger.debug('线程已停止')
        keep_awake(False)
        self.ui.pushButton_stop.setEnabled(False)
        self.ui.pushButton_start.setEnabled(True)
        self.ui.checkBox_count.setEnabled(True)
        self.ui.checkBox_auto_feed.setEnabled(True)
        self.on_checkbox_clicked()
        if self.ui.checkBox_shutdown.checkState():
            logger.info('!!! 系统将在 30s 后关机 !!!')
            reply = TimedMessageBox(30, self).exec_()
            if reply == QMessageBox.Ok:
                logger.info("已取消自动关机")

    def stop_thread(self, index=0):
        self.stop()

    def closeEvent(self, close_event):
        if self.ui.checkBox_shutdown.checkState():
            self.ui.checkBox_shutdown.setCheckState(Qt.Unchecked)
        self.stop()
