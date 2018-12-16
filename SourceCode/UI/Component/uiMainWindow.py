# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Left = QtWidgets.QWidget(self.centralwidget)
        self.Left.setMaximumSize(QtCore.QSize(250, 16777215))
        self.Left.setObjectName("Left")
        self.LeftLayout = QtWidgets.QVBoxLayout(self.Left)
        self.LeftLayout.setContentsMargins(0, 0, 0, 6)
        self.LeftLayout.setSpacing(0)
        self.LeftLayout.setObjectName("LeftLayout")
        self.horizontalLayout.addWidget(self.Left)
        self.Right = QtWidgets.QWidget(self.centralwidget)
        self.Right.setObjectName("Right")
        self.RightLayout = QtWidgets.QVBoxLayout(self.Right)
        self.RightLayout.setContentsMargins(0, 0, 0, 0)
        self.RightLayout.setSpacing(6)
        self.RightLayout.setObjectName("RightLayout")
        self.horizontalLayout.addWidget(self.Right)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

