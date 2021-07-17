# -*- codeing = utf-8 -*-
# @Time : 2021/7/17 14:59
# @Auther : 亱華
# @File : demo2.py
# @SoftWare : PyCharm

import bs4
import re
import urllib.request,urllib.error
import xlwt

def main():
    baseurl = "https://movie.douban.com/top250?start="
    #1.爬取网页
    datalist = getData(baseurl)
    #2.逐一解析数据       ->    在爬取过程中边爬取边处理


    #3.保存数据
    savepath = ".\\豆瓣电影Top250.xls"
    #saveData(savepath)
    askURL("https://movie.douban.com/top250")

#得到一个指定URL的网页内容
def askURL(url):
    #伪装成为浏览器访问网站
    head = {    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36","X-Amzn-Trace-Id": "Root=1-60f297ad-062adad97fe836221ed8040c"
        }
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html



#爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10):                   #爬取十次页面
        url = baseurl+str(i*25)
        html = askURL(url)                  #保存获取的网页原码
    return datalist

#保存数据
def saveData(savepath):
    print("数据已保存")



if __name__ == "__main__":          #当程序执行时
#调用函数
    main()