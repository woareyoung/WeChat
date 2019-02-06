from Assist.GlobalVariable import *


# 私聊消息处理器
class PrivateMessageHandler:

    def __init__(self, msg):
        self.__msg_content = msg
        self.__Type = "text"

    # 获取当前朋友的id号
    def get_current_user(self):
        return str(self.__msg_content["User"]["UserName"])

    # 获取发送者
    def get_sender(self):
        return str(self.__msg_content["FromUserName"])

    # 获取消息内容
    def get_content(self):
        return str(self.__msg_content["Content"])

    # 获取消息类型
    def get_type(self):
        return str(self.__Type)

    # 获取对方昵称
    def get_nick_name(self):
        if self.__msg_content["User"]["UserName"] == "filehelper":
            return "文件传输助手"
        return str(self.__msg_content["User"]["NickName"])

    # 获取对方备注
    def get_remark_name(self):
        if self.__msg_content["User"]["UserName"] == "filehelper":
            return "文件传输助手"
        return str(self.__msg_content["User"]["RemarkName"])

    # 获取接收者
    def get_receiver(self):
        return str(self.__msg_content["ToUserName"])

    # 获取朋友的省份
    def get_province(self):
        if self.__msg_content["User"]["UserName"] == "filehelper":
            return ""
        return str(self.__msg_content["User"]["Province"])

    # 获取朋友的城市
    def get_city(self):
        if self.__msg_content["User"]["UserName"] == "filehelper":
            return ""
        return str(self.__msg_content["User"]["City"])

    # 获取朋友的个性签名
    def get_signature(self):
        if self.__msg_content["User"]["UserName"] == "filehelper":
            return ""
        return str(self.__msg_content["User"]["Signature"])

    # 获取头像地址
    def get_headimg_addr(self):
        if self.__msg_content["User"]["UserName"] == "filehelper":
            return ""
        return str(self.__msg_content["User"]["HeadImgUrl"])

    # 获取消息id号
    def get_msg_id(self):
        return str(self.__msg_content["MsgId"])

    # 判断本机是否是发送者，否——1，是——0
    def local_is_sender(self):
        if self.get_sender() != get_local_id() and self.get_sender() != "filehelper":
            return 1
        return 0


# 群聊消息处理器
class GroupMessageHandler:

    def __init__(self, msg):
        self.__msg_content = msg
        self.__Type = "text"

    # 获取消息内容
    def get_content(self):
        return str(self.__msg_content["Content"])

    # 获取消息id号
    def get_msg_id(self):
        return str(self.__msg_content["MsgId"])

    # 获取发送者
    def get_sender(self):
        return str(self.__msg_content["FromUserName"])

    # 获取发送者的备注名称
    def get_sender_remark_name(self):
        return str(self.__msg_content["ActualNickName"])

    # 获取群聊名称
    def get_group_name(self):
        return str(self.__msg_content["User"]["NickName"])

    # 获取@对象的备注名称
    def get_at_remark_name(self):
        pass

    # 获取@对象的群名称
    def get_at_group_name(self):
        pass

    # 判断本机是否是发送者，否——1，是——0
    def local_is_sender(self):
        if self.get_sender() != get_local_id():
            return 1
        return 0
