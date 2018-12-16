import itchat
from itchat.content import *
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtCore import QThread
from Assist.GlobalVariable import *
import re

class ChatMessageReceiver(QThread):

    receive_text_signal = pyqtSignal(dict)  # 发送文本消息信号
    send_successfully_signal = pyqtSignal(str, str, str, str, int)  # 发送消息成功的信号

    # 开始执行
    def run(self):
        ChatMessageReceiver.__CMR = self
        itchat.auto_login(hotReload=True)  # 登录微信
        itchat.run()  # 进入微信控制台环境

    # 窗口关闭，退出微信
    @pyqtSlot()
    def end(self):
        itchat.logout()

    """
    发送消息
    param[target_id]:对方的id号
    param[content]:消息内容
    """
    @pyqtSlot(str, str)
    def send_msg(self, target_id, content):
        success = itchat.send(content, target_id)
        if success:
            self.send_successfully_signal.emit(get_now_time_with_microseconds(), content, "我", get_now_time(), 1)

    # 接收私聊信息
    @staticmethod
    @itchat.msg_register(TEXT)
    def __receive_text(msg):
        ChatMessageReceiver.__CMR.receive_text_signal.emit(msg)

