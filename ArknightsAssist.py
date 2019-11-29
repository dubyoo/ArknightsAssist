# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt
from MyHelper import *
import Arknights
import ui_arknights_assist
import BindWindow
import threading
import logging
import sys
import win32com.client


class ArknightsAssist(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = ui_arknights_assist.Ui_ArknightsAssist()
        self.ui.setupUi(self)
        self.ui.spinBox_count.setEnabled(False)
        self.ui.spinBox_auto_feed.setEnabled(False)
        self.ui.pushButton_stop.setEnabled(False)
        self.ui.checkBox_count.stateChanged.connect(self.on_checkbox_clicked)
        self.ui.checkBox_auto_feed.stateChanged.connect(self.on_checkbox_clicked)
        self.ui.pushButton_start.clicked.connect(self.start)
        self.ui.pushButton_stop.clicked.connect(self.stop)
        self.ui.pushButton_select_window.clicked.connect(self.select_window)
        self.child_window = BindWindow.BindWindow(self)
        self.bind_window_name = None
        self.thread = None
        self.ts = None  # win32com.client.Dispatch('ts.tssoft')
        self.arknights = Arknights.Arknights(self, self.ts)

    def on_checkbox_clicked(self):
        self.ui.spinBox_count.setEnabled(True if self.ui.checkBox_count.checkState() == Qt.Checked else False)
        self.ui.spinBox_auto_feed.setEnabled(True if self.ui.checkBox_auto_feed.checkState() == Qt.Checked else False)

    def select_window(self):
        x = self.x() + self.width()
        y = self.y()
        self.child_window.move(x, y)
        self.child_window.show()

    def on_window_selected(self, window_info):
        if window_info is None:
            self.ui.pushButton_select_window.setText('Select Window')
            self.bind_window_name = None
        else:
            self.bind_window_name = show_title = window_info.title
            if len(self.bind_window_name) >= 30:
                show_title = self.bind_window_name[:12] + ' ... ' + self.bind_window_name[-12:]
            self.ui.pushButton_select_window.setText(show_title)

    def start(self):
        self.ui.pushButton_stop.setEnabled(True)
        self.ui.pushButton_start.setEnabled(False)
        self.ui.checkBox_count.setEnabled(False)
        self.ui.checkBox_auto_feed.setEnabled(False)
        self.ui.spinBox_count.setEnabled(False)
        self.ui.spinBox_auto_feed.setEnabled(False)
        count = self.ui.spinBox_count.value() if self.ui.checkBox_count.checkState() == Qt.Checked else 0
        feed = self.ui.spinBox_auto_feed.value() if self.ui.checkBox_auto_feed.checkState() == Qt.Checked else 0
        self.arknights.set_counts(count, feed)
        # if not bind_window(self.ts, self.bind_window_name):
        #     # prompt bind error
        #     log_print('bind error')
        #     return
        # keep_awake()
        self.thread = threading.Thread(target=self.arknights.run)
        logging.debug('thread started')
        self.thread.start()

    def stop(self):
        if self.thread is not None:
            self.arknights.terminate()
            self.thread.join()
            self.thread = None
            logging.debug('thread stopped')
        # unbind_window(self.ts)
        # keep_awake(False)
        self.ui.pushButton_stop.setEnabled(False)
        self.ui.pushButton_start.setEnabled(True)
        self.ui.checkBox_count.setEnabled(True)
        self.ui.checkBox_auto_feed.setEnabled(True)
        self.on_checkbox_clicked()

    def closeEvent(self, close_event):
        self.child_window.close()
        self.stop()
