from PyQt5.QtWidgets import *
from UI.Component.uiChatMessageBar import *

class ChatMessageBar(QWidget, Ui_ChatMessageBar):

    def __init__(self, parent=None):
        super(ChatMessageBar, self).__init__(parent)
        self.setupUi(self)

    def set_sender(self, sender, is_me=False):
        self.SenderLabel.setText(sender)
        if is_me:
            self.ContentLabel.setStyleSheet("background-color: rgb(0, 200, 0);")

    def set_time(self, time):
        self.TimeLabel.setText(time)

    def set_content(self, content):
        self.ContentLabel.setText(content)

    def set_record(self, r):
        self.set_sender(r.Sender)
        self.set_time(r.Time)
        self.set_content(r.Content)

