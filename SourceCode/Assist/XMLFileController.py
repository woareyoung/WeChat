from xml.dom import minidom
import os


class XMLFileController:
    __GroupNodeList = []  # 当前操作的结点
    __FileName = ""  # 当前操作的配置文件名
    __GroupDepth = 0  # __GroupNodeList的长度
    __Modify = False  # 标记是否修改

    """
    私有成员列表：
    __GroupNodeList:结点栈，记录当前操作的结点
    __FileName:当前操作的文件名
    __GroupDepth:结点栈的深度
    
    __Document:当前的Document对象
    """

    def __init__(self):
        self.__Modify = False
    """
    打开文件
    param[filename]:文件名
    """
    def open(self, filename):
        self.__FileName = filename
        self.__GroupNodeList = []
        if os.path.exists(filename):
            self.__Document = minidom.parse(filename)
            root_node = self.__Document.getElementsByTagName("root")
            if len(root_node) <= 0:
                root = self.__Document.createElement("root")
                self.__Document.appendChild(root)
                self.__Modify = True
            else:
                self.__GroupNodeList.append(root_node[0])
        else:
            self.__Document = minidom.Document()
            root = self.__Document.createElement("root")
            self.__Document.appendChild(root)
            self.__GroupNodeList.append(root)
            self.__Modify = True
        self.__GroupDepth = 1
    """
    设置当前操作的结点
    param[node_name]:结点名称
    param[index]:当同名的结果有多个时，index起作用（从0起）
    """
    def begin_parent_node(self, node_name, index = 0):
        current_node = self.__GroupNodeList[self.__GroupDepth - 1]
        child_node = current_node.getElementsByTagName(node_name)
        if len(child_node) <= 0:
            node = self.__Document.createElement(node_name)
            current_node.appendChild(node)
            self.__GroupNodeList.append(node)
            self.__Modify = True
        else:
            self.__GroupNodeList.append(child_node[index])
        self.__GroupDepth = self.__GroupDepth + 1

    # 结束当前操作的组
    def end_parent_node(self):
        if self.__GroupDepth > 1:
            self.__GroupNodeList.pop()
            self.__GroupDepth = self.__GroupDepth - 1

    """
    设置结点的id属性
    param[value]:id值
    """
    def set_parent_id(self, value):
        current_node = self.__GroupNodeList[self.__GroupDepth - 1]
        current_node.setAttribute("id", value)
        self.__Modify = True

    # 获取结点的属性
    def get_parent_id(self):
        current_node = self.__GroupNodeList[self.__GroupDepth - 1]
        return current_node.getAttribute("id")

    """
    设置属性值（如果没有属性，则添加；否则系改）
    param[key]:属性名
    param[value]:属性值
    """
    def set_value(self, key, value):
        current_node = self.__GroupNodeList[self.__GroupDepth - 1]
        target_node = current_node.getElementsByTagName(key)
        if len(target_node) == 0:
            final_node = self.__Document.createElement(key)
            text_node = self.__Document.createTextNode(value)
            final_node.appendChild(text_node)
            current_node.appendChild(final_node)
        else:
            for target in target_node:
                if len(target.childNodes) == 0:
                    text_node = self.__Document.createTextNode(value)
                    target.appendChild(text_node)
                else:
                    target.firstChild.data = value
        self.__Modify = True

    """
    添加属性值（添加一个属性）
    param[key]:属性名
    param[value]:属性值
    """
    def add_value(self, key, value):
        current_node = self.__GroupNodeList[self.__GroupDepth - 1]
        final_node = self.__Document.createElement(key)
        text_node = self.__Document.createTextNode(value)
        final_node.appendChild(text_node)
        current_node.appendChild(final_node)
        self.__Modify = True

    """
    获取结点的属性
    param[key]:属性名
    """
    def get_value(self, key):
        current_node = self.__GroupNodeList[self.__GroupDepth - 1]
        target_node = current_node.getElementsByTagName(key)
        try:
            if len(target_node) == 0:
                return ""
            else:
                return target_node[0].firstChild.data
        except Exception as e:
            return ""

    # 获取当前结点下所有非文本结点的名称
    def get_child_parent_node_string_list(self):
        node_list = []
        current_node = self.__GroupNodeList[self.__GroupDepth - 1]
        child_list = current_node.childNodes
        if len(child_list) > 0:
            for node in child_list:
                if self.__is_text_node(node) == False:
                    node_list.append(node.node_name)
        return node_list

    # 获取当前结点下所有文本结点
    def get_child_text_node_name(self):
        string_list = []
        current_node = self.__GroupNodeList[self.__GroupDepth - 1]
        child_list = current_node.childNodes
        for node in child_list:
            if self.__is_text_node(node):
                string_list.append(node.node_name)
        return string_list

    # 获取当前结点下所有文本结点的值
    def get_child_text_node_value(self):
        stringList = []
        current_node = self.__GroupNodeList[self.__GroupDepth - 1]
        child_list = current_node.childNodes
        for node in child_list:
            if self.__is_text_node(node):
                stringList.append(node.firstChild.data)
        return stringList

    """
    移除结点
    param[node_name]:结点名称
    """
    def remove_child_node(self, node_name):
        current_node = self.__GroupNodeList[self.__GroupDepth - 1]
        target_node = current_node.getElementsByTagName(node_name)
        for node in target_node:
            current_node.removeChild(node)
        self.__Modify = True

    """
    判断某个结点是否是文本结点
    param[node]:结点对象
    """
    def __is_text_node(self, node):
        if node.firstChild.nodeType == minidom.Node.TEXT_NODE:
            return True
        else:
            return False

    # 关闭文件
    def close(self):
        if self.__Modify:
            # 读写文件的句柄
            file_handle = open(self.__FileName, "w")
            # 写入操作，第二个参数为缩进（加在每行结束后），第三个为增量缩进（加在每行开始前并增量）
            self.__Document.writexml(file_handle, addindent='  ', newl='\n', encoding='utf-8')
            file_handle.close()
        self.__FileName = ""


# 写入xml文件（重写函数）
def fixed_writexml(self, writer, indent="", addindent="", newl=""):
    writer.write(indent + "<" + self.tagName)
    attrs = self._get_attributes()
    a_names = attrs.keys()
    for a_name in a_names:
        writer.write(" %s=\"" % a_name)
        minidom._write_data(writer, attrs[a_name].value)
        writer.write("\"")
    if self.childNodes:
        if len(self.childNodes) == 1 and self.childNodes[0].nodeType == minidom.Node.TEXT_NODE:
            writer.write(">")
            self.childNodes[0].writexml(writer, "", "", "")
            writer.write("</%s>%s" % (self.tagName, newl))
            return
        writer.write(">%s" % (newl))
        for node in self.childNodes:
            if node.nodeType is not minidom.Node.TEXT_NODE:
                node.writexml(writer, indent + addindent, addindent, newl)
        writer.write("%s</%s>%s" % (indent, self.tagName, newl))
    else:
        writer.write("/>%s" % (newl))


minidom.Element.writexml = fixed_writexml
