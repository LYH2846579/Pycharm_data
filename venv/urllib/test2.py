# -*- codeing = utf-8 -*-
# @Time : 2021/7/17 18:14
# @Auther : 亱華
# @File : test2.py
# @SoftWare : PyCharm


from bs4 import BeautifulSoup

file = open("./baidu.html","rb")
html = file.read()
bs = BeautifulSoup(html,"html.parser")      #解析器解析

# print(bs.title)
#
# #1.Tag 标签:拿到第一个匹配的内容
#
# #不包含标签输出（字符串）
# print(bs.title.string)
# #拿到标签中的所有属性
# print(bs.a.attrs)

#print(bs)                  #bs表示整个文档
# print(type(bs))

# print(bs.name)
# print(bs.attrs)

#----------------------------------
#文档的遍历




#文档的搜索



