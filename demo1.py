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
'''
import random

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


























