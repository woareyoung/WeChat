# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChatRecordInterface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChatRecordInterface(object):
    def setupUi(self, ChatRecordInterface):
        ChatRecordInterface.setObjectName("ChatRecordInterface")
        ChatRecordInterface.resize(560, 410)
        self.verticalLayout = QtWidgets.QVBoxLayout(ChatRecordInterface)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.FriendNameLabel = QtWidgets.QLabel(ChatRecordInterface)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FriendNameLabel.sizePolicy().hasHeightForWidth())
        self.FriendNameLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FriendNameLabel.setFont(font)
        self.FriendNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.FriendNameLabel.setObjectName("FriendNameLabel")
        self.verticalLayout.addWidget(self.FriendNameLabel)
        self.RecordWidget = QtWidgets.QWidget(ChatRecordInterface)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RecordWidget.sizePolicy().hasHeightForWidth())
        self.RecordWidget.setSizePolicy(sizePolicy)
        self.RecordWidget.setObjectName("RecordWidget")
        self.createLayout()
        self.verticalLayout.addWidget(self.RecordWidget)
        self.widget_2 = QtWidgets.QWidget(ChatRecordInterface)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 100))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 483, 98))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.InputField = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputField.sizePolicy().hasHeightForWidth())
        self.InputField.setSizePolicy(sizePolicy)
        self.InputField.setObjectName("InputField")
        self.verticalLayout_3.addWidget(self.InputField)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        self.SendButton = QtWidgets.QPushButton(self.widget_2)
        self.SendButton.setMaximumSize(QtCore.QSize(100, 100))
        self.SendButton.setObjectName("SendButton")
        self.horizontalLayout_2.addWidget(self.SendButton)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(ChatRecordInterface)
        QtCore.QMetaObject.connectSlotsByName(ChatRecordInterface)

    def retranslateUi(self, ChatRecordInterface):
        _translate = QtCore.QCoreApplication.translate
        ChatRecordInterface.setWindowTitle(_translate("ChatRecordInterface", "Form"))
        self.FriendNameLabel.setText(_translate("ChatRecordInterface", "TextLabel"))
        self.SendButton.setText(_translate("ChatRecordInterface", "PushButton"))

    def createLayout(self):
        self.RecordLayout = QtWidgets.QVBoxLayout(self.RecordWidget)
        self.RecordLayout.setContentsMargins(0, 0, 0, 0)
        self.RecordLayout.setSpacing(0)
        self.RecordLayout.setObjectName("RecordLayout")
        self.RecordLayout.addStretch()

