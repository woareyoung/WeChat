from PyQt5.Qt import *
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from UI.Component.uiChatRecordInterface import *
from UI.ChatMessageBar import *
from Assist.GlobalVariable import *
from PyQt5 import sip

# 聊天界面
class ChatRecordInterface(QWidget, Ui_ChatRecordInterface):

    send_msg_signal = pyqtSignal(str, str)  # 发送消息给朋友

    def __init__(self, parent=None):
        super(ChatRecordInterface, self).__init__(parent)
        self.setupUi(self)
        self.SendButton.setText("发送")
        self.FriendNameLabel.setText("")
        self.SendButton.clicked.connect(self.__send_message)
        self.InputField.keyPressEvent = self.__key_down
        self.InputField.keyReleaseEvent = self.__key_up
        self.__ShiftIsDown = False
        self.InputField.hide()

        self.__Msg_Bar = {}  # 消息id号——消息显示控件

    # 读取聊天纪录到界面
    def __read_chat_record(self, friend_id):
        friend_remark_name = get_remarkname_by_id(friend_id)
        record = get_record_list(friend_id)
        i = len(record) - 1
        count = 5  # 显示最近5条消息
        final_msg = []
        while i >= 0 and count > 0:
            r = record[i]
            final_msg.append(r)
            i -= 1
            count -= 1
        final_msg.reverse()
        for r in final_msg:
            self.add_msg(r.MsgId, r.Content, friend_remark_name, r.Time, r.Sender)

    # 清空聊天界面
    def __clear_msg(self):
        for key in self.__Msg_Bar.keys():
            temp_bar = self.__Msg_Bar[key]
            self.RecordLayout.removeWidget(temp_bar)
            sip.delete(temp_bar)
        self.__Msg_Bar.clear()

    """
    设置当前聊天对象
    param[friend_id]:朋友的id号
    """
    @pyqtSlot(str)
    def set_current_friend(self, friend_id):
        if self.InputField.isHidden():
            self.InputField.show()
        self.FriendNameLabel.setText(get_remarkname_by_id(friend_id))
        self.__clear_msg()
        self.__read_chat_record(friend_id)

    """发送按钮事件"""
    @pyqtSlot()
    def __send_message(self):
        content = self.InputField.toPlainText().strip()
        self.InputField.setText("")
        self.InputField.setFocus()
        self.send_msg_signal.emit(GlobalVariable.CurrentFriendId, content)

    """
    添加新的消息到窗口
    param[msg_id]:消息id
    param[content]:消息内容
    param[sender_remark]:发送者的备注名称
    param[send_time]:发送时间
    param[is_me]:是否是本机发送（0——不是，1——是）
    """
    @pyqtSlot(str, str, str, str, int)
    def add_msg(self, msg_id, content, sender_remark, send_time, is_me):
        msg_bar = ChatMessageBar(self)
        msg_bar.set_time(send_time)
        msg_bar.set_content(content)
        msg_bar.set_sender(sender_remark, is_me == 1)
        self.RecordLayout.addWidget(msg_bar)
        self.__Msg_Bar[msg_id] = msg_bar
        return msg_bar

    """输入框按钮按下事件"""
    def __key_down(self, event):
        QTextEdit.keyPressEvent(self.InputField, event)
        key = event.key()
        # 组合键
        if key == Qt.Key_Shift:
            self.__ShiftIsDown = True
        # 回车键
        elif (key == Qt.Key_Return or key == Qt.Key_Enter) and not self.__ShiftIsDown:
            self.__send_message()

    """输入框按钮松开事件"""
    def __key_up(self, event):
        if event.key() == Qt.Key_Shift:
            self.__ShiftIsDown = False

