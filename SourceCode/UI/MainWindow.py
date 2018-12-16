from UI.Component.uiMainWindow import *
from UI.FriendsControllInterface import *
from UI.ChatRecordInterface import *
from PyQt5.QtCore import pyqtSlot, pyqtSignal

class MainWindow(QMainWindow, Ui_MainWindow):

    exit_proc_signal = pyqtSignal()  # 退出程序信号

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("微信")
        self.ChatRecordInterface = ChatRecordInterface(self)
        self.__FriendControllInterface = FriendsControllInterface(self)
        self.RightLayout.addWidget(self.ChatRecordInterface)
        self.LeftLayout.addWidget(self.__FriendControllInterface)

        self.__FriendControllInterface.new_msg_signal.connect(self.ChatRecordInterface.add_msg)
        self.__FriendControllInterface.click_friend_signal.connect(self.ChatRecordInterface.set_current_friend)

    @pyqtSlot(dict)
    def receive_text(self, msg):
        self.__FriendControllInterface.set_friend(msg)

    def closeEvent(self, event):
        self.exit_proc_signal.emit()
        event.accept()
