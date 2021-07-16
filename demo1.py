# -*- codeing = utf-8 -*-
# @Time : 2021/7/16 16:48
# @Auther : 亱華
# @File : demo1.py
# @SoftWare : PyCharm

#这是我的第一个Python程序
print("hello world")
'''
这是多行注释

#格式化输出
a=10
print("这是一个数字:",a)
age = 19
print("我的年纪是: %d岁"%age)
print("我的名字是: %s,我的国籍是: %s"%("亱華","中国"))
print("aaa","bbb","ccc")
print("www","baidu","com",sep=".")
print("hello",end="")
print("world",end="\t")
print("python",end="\n")
print("end")
#输入
password = input("请输入密码:")
print("您输入的密码是:",password)
print(type(password))
#强制类型转换
a = input("请输入123:")
a = int("123")

#if-else 语句
if 1>2:
    print("1>2")
elif 3<4:
    print("3<4")
else:
    print("ERROR!")
#引入随机数
import random
computer = random.randint(0,2)
print("computer=%d"%computer)

import random

#石头剪子布游戏
a = input("请输入:剪刀(0)、石头(1)、布(2):")
if a.isdigit():             #判断是否为数字
    a = int(a)              #强制类型转换
    if(a!=0 and a!=1 and a!=2):
        print("输入错误!")
    else:
        b=random.randint(0,2)
        if(a == 0):
            print("你的输入为:剪刀(0)")
        elif(a == 1):
            print("你的输入为:石头(1)")
        elif(a == 2):
            print("你的输入为:布(2)")
        print("随机生成的数字为:%d"%b)
        if(b>a and b-a==1):
            print("哈哈，你输了:)")
        elif(b==0 and a==2):
            print("哈哈，你输了:)")
        elif(a==b):
            print("平局!")
        else:
            print("恭喜你赢了!")
else:
    print("输入错误!")

#0~100求和
sum = 0
for i in range(101):
    sum += i
print("sum=%d"%sum)
number = 0;i=0
while i<101:
    number += i
    i += 1
print("number=%d"%number)
'''

#列表
namelist = ["张三","李四","王五"]
print(namelist[0])
#添加成员
namelist.append("赵六")
namelist.insert(0,"钻石王老五")
#namelist.extend("刘七")              #注意Extend的添加形式
print("*"*30)
for name in namelist:
    print(name)
#删除元素
namelist.remove("王五")
del namelist[0]                         #删除头号元素
namelist.pop()
print("*"*30)
for name in namelist:
    print(name)
#输入查找名字是否在队列中
iname = input("请输入一个名字:")
if iname in namelist:
    print("%s在队列中"%iname)
else:
    print("%s不在队列中"%iname)






















