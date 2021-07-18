# -*- codeing = utf-8 -*-
# @Time : 2021/7/17 16:31
# @Auther : 亱華
# @File : test1.py
# @SoftWare : PyCharm

#urllib补充

import urllib.request
# reponse = urllib.request.urlopen("http://www.baidu.com")
# print(reponse.read().decode('utf-8'))
# f = open("baidu.txt","w")
# f.write(reponse.read().decode('utf-8'))
# f.close()

#获取一个post请求
import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode("utf-8"))

#伪装
# url = "http://douban.com"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
#     "X-Amzn-Trace-Id": "Root=1-60f297ad-062adad97fe836221ed8040c"
# }
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))














