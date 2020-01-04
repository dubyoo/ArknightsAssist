# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_arknights_assist.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ArknightsAssist(object):
    def setupUi(self, ArknightsAssist):
        ArknightsAssist.setObjectName("ArknightsAssist")
        ArknightsAssist.resize(540, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(ArknightsAssist)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_count = QtWidgets.QCheckBox(ArknightsAssist)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.checkBox_count.setFont(font)
        self.checkBox_count.setObjectName("checkBox_count")
        self.horizontalLayout_2.addWidget(self.checkBox_count)
        self.spinBox_count = QtWidgets.QSpinBox(ArknightsAssist)
        self.spinBox_count.setMaximum(99999)
        self.spinBox_count.setObjectName("spinBox_count")
        self.horizontalLayout_2.addWidget(self.spinBox_count)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox_auto_feed = QtWidgets.QCheckBox(ArknightsAssist)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.checkBox_auto_feed.setFont(font)
        self.checkBox_auto_feed.setObjectName("checkBox_auto_feed")
        self.horizontalLayout_3.addWidget(self.checkBox_auto_feed)
        self.spinBox_auto_feed = QtWidgets.QSpinBox(ArknightsAssist)
        self.spinBox_auto_feed.setMaximum(99999)
        self.spinBox_auto_feed.setObjectName("spinBox_auto_feed")
        self.horizontalLayout_3.addWidget(self.spinBox_auto_feed)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.checkBox_shutdown = QtWidgets.QCheckBox(ArknightsAssist)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.checkBox_shutdown.setFont(font)
        self.checkBox_shutdown.setObjectName("checkBox_shutdown")
        self.verticalLayout.addWidget(self.checkBox_shutdown)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_start = QtWidgets.QPushButton(ArknightsAssist)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout.addWidget(self.pushButton_start)
        self.pushButton_stop = QtWidgets.QPushButton(ArknightsAssist)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_stop.setFont(font)
        self.pushButton_stop.setAccessibleDescription("")
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.horizontalLayout.addWidget(self.pushButton_stop)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton_log_level = QtWidgets.QPushButton(ArknightsAssist)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_log_level.setFont(font)
        self.pushButton_log_level.setObjectName("pushButton_log_level")
        self.verticalLayout.addWidget(self.pushButton_log_level)
        self.textBrowser = QtWidgets.QTextBrowser(ArknightsAssist)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)

        self.retranslateUi(ArknightsAssist)
        QtCore.QMetaObject.connectSlotsByName(ArknightsAssist)

    def retranslateUi(self, ArknightsAssist):
        _translate = QtCore.QCoreApplication.translate
        ArknightsAssist.setWindowTitle(_translate("ArknightsAssist", "Arknight Assist"))
        self.checkBox_count.setText(_translate("ArknightsAssist", "计数"))
        self.checkBox_auto_feed.setText(_translate("ArknightsAssist", "自动喂食"))
        self.checkBox_shutdown.setText(_translate("ArknightsAssist", "自动关机"))
        self.pushButton_start.setText(_translate("ArknightsAssist", "开始"))
        self.pushButton_stop.setText(_translate("ArknightsAssist", "停止"))
        self.pushButton_log_level.setText(_translate("ArknightsAssist", "当前日志等级：精简"))

