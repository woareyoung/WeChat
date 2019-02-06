from Assist.GlobalVariable import *


"""
保存朋友信息
param[friend_id]:朋友id号
param[sender]:发送者
param[receiver]:接收者
param[nick_name]:朋友昵称
param[friend_remark_name]:朋友备注
"""
def save_friend_info(friend_id, nick_name, remark_name):
    mem_file = QSettings(GlobalVariable.PersonalMsgFile, QSettings.IniFormat)
    null = True
    # 遍历本地用户id号
    child_group = mem_file.childGroups()
    for child in child_group:
        same = False
        mem_file.beginGroup(child)
        # 匹配到相同昵称
        if mem_file.value("NickName") == nick_name:
            mem_file.setValue("RemarkName", remark_name)
            same = True
            null = False
        # 匹配到相同备注
        elif mem_file.value("RemarkName") == remark_name:
            mem_file.setValue("NickName", nick_name)
            same = True
            null = False
        mem_file.endGroup()
        # 如果匹配到相同的昵称或备注，且用户id号不同，就修改用户id号
        if same and friend_id != child:
            mem_file.remove(child)
            mem_file.beginGroup(friend_id)
            mem_file.setValue("RemarkName", remark_name)
            mem_file.setValue("NickName", nick_name)
            mem_file.endGroup()
            if os.path.exists(GlobalVariable.RecordDataDirectory + friend_id + ".ini"):
                os.rename(GlobalVariable.RecordDataDirectory + friend_id + ".ini",
                          GlobalVariable.RecordDataDirectory + child + ".ini")
    # 如果没有找到该用户，则新增一个
    if null:
        mem_file.beginGroup(friend_id)
        mem_file.setValue("RemarkName", remark_name)
        mem_file.setValue("NickName", nick_name)
        mem_file.endGroup()
    del mem_file


"""
保存聊天消息
param[friend_id]:朋友id号
param[msg_id]:消息id号
param[msg_content]:消息内容
param[now_time]:发送时间
param[type]:消息类型
param[sender]:发送者
param[is_me]:是否是本机发送（0——不是，1——是）
"""
def save_chat_msg(friend_id, msg_id, msg_content, now_time, type, sender, is_me):
    mem_file = QSettings(GlobalVariable.RecordDataDirectory + friend_id + ".ini", QSettings.IniFormat)
    mem_file.beginGroup(msg_id)
    mem_file.setValue("Content", msg_content)
    mem_file.setValue("Time", now_time)
    mem_file.setValue("Type", type)
    mem_file.setValue("Sender", sender)
    mem_file.setValue("ISend", is_me)
    mem_file.endGroup()
    del mem_file


"""
保存消息记录
param[msg_handler]:ChatMessageHandler对象
param[now_time]:消息发送时间
"""
def save_msg(msg_handler, now_time):
    friend_id = msg_handler.get_current_user()
    msg_content = msg_handler.get_content()
    remark_name = msg_handler.get_remark_name()
    sender = msg_handler.get_sender()
    is_me = msg_handler.local_is_sender()
    save_friend_info(friend_id, msg_handler.get_nick_name(), remark_name)
    save_chat_msg(friend_id, msg_handler.get_msg_id(), msg_content, now_time, msg_handler.get_type(), sender, is_me)
