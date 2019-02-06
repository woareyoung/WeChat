import os
from PyQt5.QtCore import QSettings
from Model.Record import *
import operator
from datetime import datetime
import time


class GlobalVariable:

    """
    公有变量：
    CurrentFriendId:当前正在聊天的朋友id号
    FriendDataDirectory:朋友信息的文件夹
    RecordDataDirectory:聊天记录的文件夹
    LocalID:本人的id号

    私有变量：
    RootDirectory:根目录
    """

    def __init__(self):
        GlobalVariable.CurrentFriendId = ""
        GlobalVariable.RootDirectory = self.__create_directory("Data")
        GlobalVariable.FriendDataDirectory = self.__create_directory(GlobalVariable.RootDirectory + "Friend")
        GlobalVariable.RecordDataDirectory = self.__create_directory(GlobalVariable.RootDirectory + "Record")
        GlobalVariable.LocalID = ""
        GlobalVariable.PersonalMsgFile = GlobalVariable.FriendDataDirectory + "permsg.ini"

    def __create_directory(self, dire):
        if os.path.isfile(dire):
            i = 0
            while os.path.isfile(dire + str(i)):
                i += 1
            dire += str(i)
        elif not os.path.exists(dire):
            os.mkdir(dire)
        dire += "/"
        return dire


GlobalVariable()


# 获取本人的id号
def get_local_id():
    return GlobalVariable.LocalID


# 通过id号获取昵称
def get_nickname_by_id(friend_id):
    mem_file = QSettings(GlobalVariable.PersonalMsgFile, QSettings.IniFormat)
    mem_file.beginGroup(friend_id)
    result = mem_file.value("NickName")
    mem_file.endGroup()
    del mem_file
    return result


# 通过id号获取备注
def get_remarkname_by_id(friend_id):
    mem_file = QSettings(GlobalVariable.PersonalMsgFile, QSettings.IniFormat)
    mem_file.beginGroup(friend_id)
    result = mem_file.value("RemarkName")
    mem_file.endGroup()
    del mem_file
    if result == "":
        return get_nickname_by_id(friend_id)
    return result


# 通过id号获取聊天纪录
def get_record_list(friend_id):
    record = []
    if not os.path.exists(GlobalVariable.RecordDataDirectory + friend_id + ".ini"):
        return None
    mem_file = QSettings(GlobalVariable.RecordDataDirectory + friend_id + ".ini", QSettings.IniFormat)
    child = mem_file.childGroups()
    for msg_id in child:
        mem_file.beginGroup(msg_id)
        temp = Record.get_record_object("text")
        temp.Time = mem_file.value("Time")
        temp.MsgId = msg_id
        if mem_file.value("ISend") == "1":
            temp.Sender = get_local_id()
        else:
            temp.Sender = mem_file.value("Sender")
        temp.Content = mem_file.value("Content")
        record.append(temp)
        mem_file.endGroup()
    del mem_file
    cmpfun = operator.attrgetter('Time')
    record.sort(key=cmpfun)
    return record


# 获取当前时间
def get_now_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

