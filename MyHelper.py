# -*- coding: utf-8 -*-
import time
import random
import ctypes
import logging
import sys
import os
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox


# Detect Coordinate
Coord_DaiLiZhiHui = 1200, 700
Coord_KaiShiXingDong_Blue = 1391, 805
Coord_KaiShiXingDong_Red = 1173, 456
Coord_InTheBattle = 1339, 95

# Click Region (x1, y1, x2, y2)
Region_KaiShiXingDong_Blue = 1206, 757, 1370, 790
Region_KaiShiXingDong_Red = 1173, 456, 1308, 753
Region_Bonus = 1100, 260, 1400, 400

# Color Baseline
Color_DaiLiZhiHui = 'ffffff'
Color_KaiShiXingDong_Blue = '0075a8'
Color_KaiShiXingDong_Red = 'c14600'
Color_InTheBattle = 'ffffff'


logger = logging.getLogger('my_logger')


class TimedMessageBox(QMessageBox):
    def __init__(self, timeout=30, parent=None):
        super(TimedMessageBox, self).__init__(parent)
        self.timeout = timeout
        self.setWindowTitle("自动关机")
        self.setText("系统将在 %d 秒后关机，点击按钮取消？" % self.timeout)
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.tick)
        self.timer.start()

    def tick(self):
        self.timeout -= 1
        if self.timeout >= 0:
            logger.info('%d' % self.timeout)
            self.setText("系统将在 %d 秒后关机，点击按钮取消？" % self.timeout)
        else:
            self.timer.stop()
            logger.info("正在关机")
            os.system('shutdown /s /t 5')


class XStream(QtCore.QObject):
    _stdout = None
    _stderr = None
    messageWritten = QtCore.pyqtSignal(str)

    def write(self, msg):
        if not self.signalsBlocked():
            self.messageWritten.emit(msg)

    @staticmethod
    def stdout():
        if not XStream._stdout:
            XStream._stdout = XStream()
            sys.stdout = XStream._stdout
        return XStream._stdout

    @staticmethod
    def stderr():
        if not XStream._stderr:
            XStream._stderr = XStream()
            sys.stderr = XStream._stderr
        return XStream._stderr


class MyQtHandler(logging.Handler):
    def __init__(self):
        logging.Handler.__init__(self)

    def emit(self, record):
        record = self.format(record)
        if record:
            XStream.stdout().write('%s' % record)


def init_logger():
    text_browser_handler = MyQtHandler()
    terminal_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    text_browser_handler.setFormatter(formatter)
    terminal_handler.setFormatter(formatter)
    logger.addHandler(text_browser_handler)
    logger.addHandler(terminal_handler)
    logger.setLevel(logging.INFO)


def random_sleep(sleep_time, variable_time=0):
    """
    randomly sleep for a short time between `sleep_time` and `sleep_time + variable_time`
    because of the legacy reason, sleep_time and variable_time are in millisecond
    """
    slp = random.randint(sleep_time, sleep_time + variable_time)
    time.sleep(slp / 1000)


def click_in_region(ts, x1, y1, x2, y2):
    """
    randomly click a point in a rectangle region (x1, y1), (x2, y2)
    """
    x = random.randint(x1, x2)
    y = random.randint(y1, y2)
    ts.MoveTo(x, y)
    logger.debug('move to (%d, %d)' % (x, y))
    random_sleep(100, 100)
    ts.LeftClick()
    logger.debug('left click')


def keep_awake(enable=True):
    """
    make the screen keep awake, do not go to sleep mode
    """
    ES_CONTINUOUS = 0x80000000
    ES_SYSTEM_REQUIRED = 0x00000001
    ES_DISPLAY_REQUIRED = 0x00000002
    if enable:
        logger.info('enable screen awake')
        ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED)
    else:
        logger.info('disable screen awake')
        ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)


def bind_window(ts_plugin, window_name):
    need_ver = '4.019'
    if ts_plugin.ver() != need_ver:
        logger.error('register failed')
        return False
    else:
        logger.info('register success')

    hwnd = ts_plugin.FindWindow('', window_name)
    ts_ret = ts_plugin.BindWindow(hwnd, 'dx2', 'windows', 'windows', 0)
    if ts_ret != 1:
        logger.error('binding failed')
        return False
    logger.info('binding success')
    return True


def unbind_window(ts_plugin):
    logger.info('UnBindWindow return: %d' % ts_plugin.UnBindWindow())
