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

    私有变量：
    RootDirectory:根目录
    """

    def __init__(self):
        GlobalVariable.CurrentFriendId = ""
        GlobalVariable.RootDirectory = self.__create_directory("Data")
        GlobalVariable.FriendDataDirectory = self.__create_directory(GlobalVariable.RootDirectory + "Friend")
        GlobalVariable.RecordDataDirectory = self.__create_directory(GlobalVariable.RootDirectory + "Record")

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


# 通过id号获取昵称
def get_nickname_by_id(friend_id):
    mem_file = QSettings(GlobalVariable.FriendDataDirectory + friend_id + ".ini", QSettings.IniFormat)
    result = mem_file.value("NickName")
    del mem_file
    return result


# 通过id号获取备注
def get_remarkname_by_id(friend_id):
    mem_file = QSettings(GlobalVariable.FriendDataDirectory + friend_id + ".ini", QSettings.IniFormat)
    result = mem_file.value("RemarkName")
    del mem_file
    if result == "":
        return get_nickname_by_id(friend_id)
    return result


# 通过id号获取聊天纪录
def get_record_list(friend_id):
    record = []
    mem_file = QSettings(GlobalVariable.RecordDataDirectory + friend_id + ".ini", QSettings.IniFormat)
    child = mem_file.childGroups()
    for msg_id in child:
        mem_file.beginGroup(msg_id)
        temp = Record.get_record_object("text")
        temp.Time = mem_file.value("Time")
        temp.MsgId = msg_id
        if mem_file.value("ISend") == "1":
            temp.Sender = "我"
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


# 获取当前时间（含毫秒）
def get_now_time_with_microseconds():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    return time_stamp
