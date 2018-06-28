from tkinter import *
import sys
import os
import itchat
from itchat.content import *
import datetime
import threading
sys.path.append("../tool")
from FileController import XMLFileController

class ChatBarMessage:
	def __init__(self, time = "", senderName = "", messageContext = ""):
		self.setData(time, senderName, messageContext)

	def setData(self, time, senderName, messageContext):
		self.time = time
		self.senderName = senderName
		self.messageContext = messageContext
#消息内容条
class ChatBar:
	height = 0
	def __init__(self, parent):
		self.__isLocal = False
		self.context = ChatBarMessage()
		rootPanel = PanedWindow(parent, orient = VERTICAL)
		rootPanel.pack(expand = YES, fill = X, ipady = ChatBar.height)
		self.__timeLabel = Label(rootPanel, text = self.context.time)
		rootPanel.add(self.__timeLabel)
		self.__messageLabel = Label(rootPanel, text = self.context.senderName + "--->" + self.context.messageContext)
		rootPanel.add(self.__messageLabel)
	#设置数据
	def setData(self, sender, messageContext, time, localSend = False):
		self.__isLocal = localSend
		self.context.setData(time, sender, messageContext)
	#复制数据
	def copyData(self, chatBarMessage, localSend = False):
		self.context.setData(chatBarMessage.time, chatBarMessage.senderName, chatBarMessage.messageContext, localSend)
		self.__refleshWidgets()
	#刷新时间
	def refleshTime(self):
		self.context.time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		self.__refleshWidgets()
	#刷新控件
	def __refleshWidgets(self):
		self.__timeLabel["text"] = self.context.time
		if self.__isLocal == True:
			self.__messageLabel["justify"] = "right"
		else:
			self.__messageLabel["justify"] = "left"
		if self.context.senderName:
			self.__messageLabel["text"] = self.context.senderName + "--->" + self.context.messageContext

class MainWindow:
	#初始化函数
	def __init__(self, winTitleName):
		self.__chatBarList = []
		self.userid = ""

		self.__fileController = XMLFileController()
		self.__fileController.Open("../properties/winPro.xml")
		self.__readProperties()

		self.__appWindow = Tk()
		self.__appWindow.protocol("WM_DELETE_WINDOW", self.__Close_Event)
		self.__appWindow.resizable(False, False)
		self.__appWindow.geometry(str(self.__windowWidth) + "x" + str(self.__widnowHeight) + "+" +
			str(int((self.__appWindow.winfo_screenwidth() - self.__windowWidth) / 2)) +  "+" +
			str(int((self.__appWindow.winfo_screenheight() - self.__widnowHeight) / 2)))
		self.__appWindow.title(winTitleName) #设置窗口标题
		self.__createContactList()
		self.__createContactContext()

		for i in range(self.__chatNumber):
			self.__chatBarList.append(ChatBar(self.__chatMemory))

		self.__fileController.Close()
	#start
	def startLoop(self):
		threading.Thread(target = self.__startWechat, name = "itchat_thread").start()
		self.__appWindow.mainloop()
	#读取配置文件
	def __readProperties(self):
		self.__windowWidth = int(self.__fileController.GetValue("appWindowWidth"))
		self.__widnowHeight = int(self.__fileController.GetValue("appWindowHeight"))
		self.__baseSpan = int(self.__fileController.GetValue("baseSpan"))
		self.__contactListWidth = int(self.__fileController.GetValue("contactListWidth"))
		self.__defaultBackgroundColor = self.__fileController.GetValue("defaultBackgroundColor")
		ChatBar.height = int(self.__fileController.GetValue("chatBarHeight"))
		self.__chatNumber = int(self.__fileController.GetValue("chatNumber"))
	#创建联系人列表
	def __createContactList(self):
		width = int(self.__fileController.GetValue("scrollbarWidth"))
		self.__contactList = Listbox(self.__appWindow)
		self.__contactList.place(x = self.__baseSpan, y = self.__baseSpan, width = self.__contactListWidth - width, height = self.__widnowHeight - 2 * self.__baseSpan)
		scrollbar = Scrollbar(self.__appWindow)
		scrollbar.set(0.65, 1)
		scrollbar.place(x = self.__contactListWidth - width, y = self.__baseSpan, width = width, height = self.__widnowHeight - 2 * self.__baseSpan)
		self.__contactList.configure(yscrollcommand = scrollbar.set)
		scrollbar['command'] = self.__contactList.yview
		self.__contactList.bind("<ButtonRelease-1>", self.__SelectContactor_Event__)
	#创建聊天面板
	def __createContactContext(self):
		self.__fileController.BeginParentNode("chatInterface")

		width = self.__windowWidth - self.__contactListWidth - 3 * self.__baseSpan
		height = self.__widnowHeight - 2 * self.__baseSpan
		sendWidth = int(self.__fileController.GetValue("sendWidth"))
		self.__rightPanel = Frame(self.__appWindow, bg = "green")
		self.__rightPanel.place(x = self.__contactListWidth + 2 * self.__baseSpan, y = self.__baseSpan, width = width, height = height)

		chatTitleHeight = int(self.__fileController.GetValue("titleHeight"))
		inputHeight = int(self.__fileController.GetValue("inputHeight"))

		self.__chatTitle = Label(self.__rightPanel, bg = self.__defaultBackgroundColor)
		self.__chatTitle.place(x = 0, y = 0, width = width, height = chatTitleHeight)

		self.__chatMemory = LabelFrame(self.__rightPanel, bg = self.__defaultBackgroundColor)
		self.__chatMemory.place(x = 0, y = chatTitleHeight, width = width, height = height - chatTitleHeight - inputHeight)

		self.__messageInput = Text(self.__rightPanel, bg = "white")
		self.__messageInput.place(x = 0, y = height - inputHeight, width = width - sendWidth, height = inputHeight)
		self.__messageInput.bind("<Return>", self.__SendMessage_Event__)

		self.__sendMessageButton = Button(self.__rightPanel, text = "发送")
		self.__sendMessageButton.place(x = width - sendWidth, y = height - inputHeight, width = sendWidth, height = inputHeight)
		self.__sendMessageButton.bind("<Button-1>", self.__SendMessage_Event__)
		self.__fileController.EndParentNode()

	#发送消息事件
	def __SendMessage_Event__(self, event):
		inputString = self.__messageInput.get("0.0", "end").strip()
		length = len(inputString)
		self.__messageInput.delete(0.0, END)
	#选择联系人事件
	def __SelectContactor_Event__(self, event):
		try:
			self.__chatTitle["text"] = self.__contactList.get(self.__contactList.curselection())
		except Exception as e:
			return

	#窗口关闭事件
	def __Close_Event(self):
		itchat.logout()
		self.__appWindow.destroy()
		self.__appWindow.quit()
		sys.exit(0)
	#开启微信
	def __startWechat(self):
		itchat.auto_login(hotReload = True) #登录微信
		itchat.run() #进入微信控制台环境

	#读取聊天记录
	def __readChatMemory(self):
		file = XMLFileController()
		file.Open("../record/" + self.userid + ".xml")
		timeList = file.GetChildParentNodeStringList()
		i = self.__chatNumber - 1
		for time in range(len(timeList) - 1, -1, -1):
			file.BeginParentNode(time)
			sender = file.GetValue("RemarkName")
			isLocal = file.GetValue("local") == "True"
			if sender == "":
				sender = file.GetValue("NickName")
			self.__chatBarList[i].setData(sender, file.GetValue("message"), time, isLocal)
			file.EndParentNode()
			i = i - 1
			if i == -1:
				break
		while i >= 0:
			self.__chatBarList[i].setData("", "", "")
		file.Close()
	#
	def getTextMsg(self, userid):
		print(text)

@itchat.msg_register(TEXT)#接收到私聊消息时，进入此函数
def receive_text(msg):
	global main_window
	global localUserName
	username = msg["User"]["UserName"] #获取当前的用户id号
	file = XMLFileController()
	file.Open("../record/" + username + ".xml")
	file.BeginParentNode(datetime.now().strftime("%Y-%m-%d_%H:%M:%S"))
	file.SetValue("message", msg["Content"])
	file.SetValue("msg_type", "text")
	#判断是否时文件传输助手
	if username == "filehelper":
		file.SetValue("RemarkName", "文件传输助手")
		file.SetValue("NickName", "文件传输助手")
		if msg["ToUserName"] == "filehelper":
			file.SetValue("local", "True")
		else:
			file.SetValue("local", "False")
	#如果不是文件传输助手
	else:
		file.SetValue("RemarkName", msg["User"]["RemarkName"])
		file.SetValue("NickName", msg["User"]["NickName"])
		#判断消息发送方和接收方
		if localUserName == "":
			if username == msg["FromUserName"]:
				localUserName = msg["ToUserName"]
				file.SetValue("local", "False")
			else:
				localUserName = msg["FromUserName"]
				file.SetValue("local", "True")
		elif localUserName == msg["FromUserName"]:
			file.SetValue("local", "True")
		else:
			file.SetValue("local", "False")
	file.EndParentNode()
	file.Close()
	main_window.getTextMsg(username)

if __name__ == "__main__":
	global main_window
	global localUserName
	global condition
	global fileOpenning
	if os.path.exists("../properties/winPro.xml") == False:
		configFile = XMLFileController()
		configFile.Open("../properties/winPro.xml")
		configFile.SetValue("appWindowWidth", "700")
		configFile.SetValue("appWindowHeight", "500")
		configFile.SetValue("defaultBackgroundColor", "gray")
		configFile.SetValue("baseSpan", "5")
		configFile.SetValue("contactListWidth", "150")
		configFile.SetValue("scrollbarWidth", "15")
		configure.BeginParentNode("chatInterface")
		configFile.SetValue("titleHeight", "35")
		configFile.SetValue("inputHeight", "50")
		configFile.SetValue("sendWidth", "50")
		configFile.SetValue("chatNumber", "10")
		configFile.SetValue("chatBarHeight", "50")
		configure.EndParentNode()
		configFile.Close()
	localUserName = ""
	fileOpenning = False
	condition = threading.Condition()
	main_window = MainWindow("微信")
	main_window.startLoop()
