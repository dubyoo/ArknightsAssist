# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication
import ArknightsAssist
import win32com.client
import sys
from MyHelper import *
import logging


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', level=logging.DEBUG)
    logging.debug('python version: %s' % sys.version)

    # 需要提前在 windows 中注册 TSPlug.dll
    # 方法: regsvr32.exe TSPlug.dll

    # Reference: http://timgolden.me.uk/pywin32-docs/html/com/win32com/HTML/QuickStartClientCom.html
    # 建立 COM Object

    # ts = win32com.client.Dispatch('ts.tssoft')
    #
    # try:
    #     assert(bind_window(ts, '明日方舟 - MuMu模拟器'))
    #     keep_awake()
    #     arknights = Arknights.Arknights(ts)
    #     arknights.main_loop()
    # except:
    #     log_print('terminated')
    #     log_print('UnBindWindow return:', ts.UnBindWindow())

    app = QApplication(sys.argv)
    assist = ArknightsAssist.ArknightsAssist()
    assist.show()
    sys.exit(app.exec_())

