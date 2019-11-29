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
        ArknightsAssist.resize(280, 150)
        self.gridLayout = QtWidgets.QGridLayout(ArknightsAssist)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_count = QtWidgets.QCheckBox(ArknightsAssist)
        self.checkBox_count.setObjectName("checkBox_count")
        self.gridLayout.addWidget(self.checkBox_count, 0, 0, 1, 1)
        self.spinBox_count = QtWidgets.QSpinBox(ArknightsAssist)
        self.spinBox_count.setMaximum(99999)
        self.spinBox_count.setObjectName("spinBox_count")
        self.gridLayout.addWidget(self.spinBox_count, 0, 1, 1, 1)
        self.checkBox_auto_feed = QtWidgets.QCheckBox(ArknightsAssist)
        self.checkBox_auto_feed.setObjectName("checkBox_auto_feed")
        self.gridLayout.addWidget(self.checkBox_auto_feed, 1, 0, 1, 1)
        self.spinBox_auto_feed = QtWidgets.QSpinBox(ArknightsAssist)
        self.spinBox_auto_feed.setMaximum(99999)
        self.spinBox_auto_feed.setObjectName("spinBox_auto_feed")
        self.gridLayout.addWidget(self.spinBox_auto_feed, 1, 1, 1, 1)
        self.pushButton_select_window = QtWidgets.QPushButton(ArknightsAssist)
        self.pushButton_select_window.setObjectName("pushButton_select_window")
        self.gridLayout.addWidget(self.pushButton_select_window, 2, 0, 1, 2)
        self.pushButton_start = QtWidgets.QPushButton(ArknightsAssist)
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout.addWidget(self.pushButton_start, 3, 0, 1, 1)
        self.pushButton_stop = QtWidgets.QPushButton(ArknightsAssist)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.gridLayout.addWidget(self.pushButton_stop, 3, 1, 1, 1)

        self.retranslateUi(ArknightsAssist)
        QtCore.QMetaObject.connectSlotsByName(ArknightsAssist)

    def retranslateUi(self, ArknightsAssist):
        _translate = QtCore.QCoreApplication.translate
        ArknightsAssist.setWindowTitle(_translate("ArknightsAssist", "Arknight Assist"))
        self.checkBox_count.setText(_translate("ArknightsAssist", "Count"))
        self.checkBox_auto_feed.setText(_translate("ArknightsAssist", "Auto Feed"))
        self.pushButton_select_window.setText(_translate("ArknightsAssist", "Select Window"))
        self.pushButton_start.setText(_translate("ArknightsAssist", "Start"))
        self.pushButton_stop.setText(_translate("ArknightsAssist", "Stop"))

