# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FriendBar.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FriendBar(object):
    def setupUi(self, FriendBar):
        FriendBar.setObjectName("FriendBar")
        FriendBar.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(FriendBar)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.FriendName = QtWidgets.QLabel(FriendBar)
        self.FriendName.setObjectName("FriendName")
        self.verticalLayout.addWidget(self.FriendName)
        self.ClosestRecord = QtWidgets.QLabel(FriendBar)
        self.ClosestRecord.setObjectName("ClosestRecord")
        self.verticalLayout.addWidget(self.ClosestRecord)

        self.retranslateUi(FriendBar)
        QtCore.QMetaObject.connectSlotsByName(FriendBar)

    def retranslateUi(self, FriendBar):
        _translate = QtCore.QCoreApplication.translate
        FriendBar.setWindowTitle(_translate("FriendBar", "Form"))
        self.FriendName.setText(_translate("FriendBar", "TextLabel"))
        self.ClosestRecord.setText(_translate("FriendBar", "TextLabel"))

