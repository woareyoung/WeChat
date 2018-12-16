# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FriendsControllInterface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FriendsControllInterface(object):
    def setupUi(self, FriendsControllInterface):
        FriendsControllInterface.setObjectName("FriendsControllInterface")
        FriendsControllInterface.resize(527, 364)
        self.verticalLayout = QtWidgets.QVBoxLayout(FriendsControllInterface)
        self.verticalLayout.setContentsMargins(2, 2, 2, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea_2 = QtWidgets.QScrollArea(FriendsControllInterface)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.FriendListWidget = QtWidgets.QWidget()
        self.FriendListWidget.setGeometry(QtCore.QRect(0, 0, 521, 292))
        self.FriendListWidget.setObjectName("FriendListWidget")
        self.FriendListLayout = QtWidgets.QVBoxLayout(self.FriendListWidget)
        self.FriendListLayout.setContentsMargins(0, 0, 0, 0)
        self.FriendListLayout.setSpacing(0)
        self.FriendListLayout.setObjectName("FriendListLayout")
        self.scrollArea_2.setWidget(self.FriendListWidget)
        self.verticalLayout.addWidget(self.scrollArea_2)
        self.widget = QtWidgets.QWidget(FriendsControllInterface)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Message = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Message.sizePolicy().hasHeightForWidth())
        self.Message.setSizePolicy(sizePolicy)
        self.Message.setMinimumSize(QtCore.QSize(0, 50))
        self.Message.setObjectName("Message")
        self.horizontalLayout_3.addWidget(self.Message)
        self.Friend = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Friend.sizePolicy().hasHeightForWidth())
        self.Friend.setSizePolicy(sizePolicy)
        self.Friend.setMinimumSize(QtCore.QSize(0, 50))
        self.Friend.setObjectName("Friend")
        self.horizontalLayout_3.addWidget(self.Friend)
        self.FriendCircle = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FriendCircle.sizePolicy().hasHeightForWidth())
        self.FriendCircle.setSizePolicy(sizePolicy)
        self.FriendCircle.setMinimumSize(QtCore.QSize(0, 50))
        self.FriendCircle.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.FriendCircle.setObjectName("FriendCircle")
        self.horizontalLayout_3.addWidget(self.FriendCircle)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(FriendsControllInterface)
        QtCore.QMetaObject.connectSlotsByName(FriendsControllInterface)

    def retranslateUi(self, FriendsControllInterface):
        _translate = QtCore.QCoreApplication.translate
        FriendsControllInterface.setWindowTitle(_translate("FriendsControllInterface", "Form"))
        self.Message.setText(_translate("FriendsControllInterface", "PushButton"))
        self.Friend.setText(_translate("FriendsControllInterface", "PushButton"))
        self.FriendCircle.setText(_translate("FriendsControllInterface", "PushButton"))

