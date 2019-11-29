# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication
import ArknightsAssist
import sys
import logging


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', level=logging.DEBUG)
    logging.debug('python version: %s' % sys.version)

    # 需要提前在 windows 中注册 TSPlug.dll
    # 方法: regsvr32.exe TSPlug.dll

    app = QApplication(sys.argv)
    assist = ArknightsAssist.ArknightsAssist()
    assist.show()
    sys.exit(app.exec_())

