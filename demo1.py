# -*- codeing = utf-8 -*-
# @Time : 2021/7/16 16:48
# @Auther : 亱華
# @File : demo1.py
# @SoftWare : PyCharm

#Python基础学习

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
#指定范围查询         查询成功返回指定位置 否则报错
print("张三位于:",namelist.index("张三",0,2))
#统计
print("李四出现了",namelist.count("李四"),"次")

#列表操作
namelist = ["a","b","c","d"]
namelist.reverse()              #列表反转
for name in namelist:
    print(name,end="")          #取消换行
namelist.sort()
print()                         #换行
for name in namelist:
    print(name,end="")
namelist.sort(reverse=True)     #Python中True和False开头均为大写
print()                         #换行
for name in namelist:
    print(name,end="")


#三个办公室随机分配八个老师
import random
offices = [[],[],[]]
namelist = ["A","B","C","D","E","F","G","H"]
for name in namelist:
    index = random.randint(0,2)
    offices[index].append(name)                 #!
i = 1
for office in offices:
    print("办公室%d的人数为%d:" %(i,len(office)))
    i += 1
    for name in office:
        print("%s"%name,end="\t")               #!
    print("\n")
    print("*"*30)


#商品购买                   #安全性尚待优化
products = [["iphone","6888"],["MacPro","14800"],["小米6","2499"],["Coffee","31"],["Book","60"],["Nike","699"]]
i = 0
for item in products:
    print(i,end="\t");i += 1
    for name in item:
        print("%s"%name,end="\t")
    print()
sum = 0
purching = []
while True:
    a = input("请输入所需商品的序号(输入q退出)")
    if(a != "q"):
        a = int(a)
        purching.append(products[a])
        sum += int(products[a][1])
    else:
        break
for item in purching:
    for name in item:
        print("%s"%name,end="\t")
    print()
print("总价为:%d"%sum)


#元组                    #不可以修改
tup1 = (1)              #type(tup1) = <class 'int'>
tup2 = (1,)             #type(tup1) = <class 'tuple'>
tup3 = (1,2,'3',"4")
#元组数据访问
print("tup3[0:5]:",tup3[0:5])
print(type(tup3[0]),type(tup3[1]),type(tup3[2]),type(tup3[3]))      #int int str str
#元组数据连接
tup4 = tup2 + tup3
print(tup4)
#删除
del tup4

#字典
#定义
Info = {"name":"吴彦祖","age":18,17:17}
#直接访问                       #当搜寻的值不存在的时候，会出现错误
print(Info["name"])
print(Info["age"])
print(Info[17])
#间接访问
print(Info.get("gender"))      #搜寻不到的时候返回none
print(Info.get("none","m"))    #自定义返回默认值
#字典的增删改查
#增 Info.balabala无效!
Info["id"] = 123
print(Info["id"])
#删除
del Info["id"]                  #删除整个键值对
#print(Info["id"])
Info.clear()                    #清空整个字典
print("After Info.clear():",Info)
#修改
Info["name"] = "刘德华"
print(Info["name"])
print("*"*30)
#查询
Info = {"id":1,"name":"吴彦祖","age":18}
print(Info.keys())              #打印所有的键(列表)
print(Info.values())            #打印所有的值(列表)
print(Info.items())             #打印所有的项(列表),每个键值都是一个元组
#遍历所有的项
for key,value in Info.items():
    print("key=%s,value=%s"%(key,value))
#使用enumerate打印数字下标值                                 ※
mylist = ["a","b","c","d"]
for i,x in enumerate(mylist):
    print(i,x)


#函数
#定义
def printInfo():
    print("--------------------")
    print("  人生苦短，我用Python ")
    print("--------------------")
#调用
printInfo()

#带参数的函数
def add2Num(a,b):
    c = a+b
    print(c)
#调用
add2Num(11,22)

#带返回值的函数
def add2Num(a,b):
    return a+b
#调用
c = add2Num(11,12)
print(c)

#多返回值函数
def divide(a,b):
    shang = a/b
    yushu = a%b
    return shang,yushu      #多返回值用逗号分隔

a,b = divide(11,6)          #多参数接受
print(a,b)


#全局变量和局部变量
global a    #全局变量(在函数中)


#文件操作
#打开文件
f = open("test.txt","w")        #若有重名的文件，重新创建
f.write("Hello World!")
#关闭文件
f.close()

#读文件
f = open("test.txt","r")
text = f.read(5)
text1 = f.readline()
text2 = f.readlines()
print(text)                     #后面读取的数据是从上次读完后的位置开始的
print(text1)
print(text2)
f.close()


#读文件plus
f = open("test.txt","r")
content = f.readlines()
print(content)
i = 1
for temp in content:
    print("%d\t%s"%(i,temp))
    i += 1
for i,temp in enumerate(content):
    print(i,temp)


#异常处理
try:
    print("----------test----1----")
    f = open("123.txt","r")                 #读不存在的文件
    print("----------test----2----")
except FileNotFoundError:                   #若发现这种错误，则进行如下方式处理
    pass
#将异常信息输出
try:
    print(num)
except NameError as result:
    print(result)
#捕获所有异常
try:
    print("-------------test-----1---")
    f = open("123.txt","r")
    print(num)
except Exception as result:                 #承接所有异常
    print(result)

'''














