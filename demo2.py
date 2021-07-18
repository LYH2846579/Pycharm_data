# -*- codeing = utf-8 -*-
# @Time : 2021/7/17 14:59
# @Auther : 亱華
# @File : demo2.py
# @SoftWare : PyCharm

from bs4 import BeautifulSoup
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
    savepath = "豆瓣电影Top250.xls"
    saveData(datalist,savepath)
    #askURL("https://movie.douban.com/top250")

#影片链接规则
findLink = re.compile(r'<a href="(.*?)">')    #创建正则表达式对象(字符串匹配模式)
findImage = re.compile(r'<img alt=.*src="(.*?) width=(.*)"/>',re.S)        #忽略换行符        #将width添加
findTitle = re.compile(r'<span class="title">(.*)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)



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
        #逐一处理数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):         #查找符合要求的字符串（搜寻每一个Item）
            #print(item)
            data = []                                           #保存一部电影的所有信息
            item = str(item)                                    #转换为字符串

            #电影链接
            titles = re.findall(findTitle,item)
            if (len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)                         #添加中文名
                otitle = titles[1].replace("/","")          #去掉无关的/
                otitle = otitle.replace(r"\xa0","")
                data.append(otitle)                         #添加外文名
            else:
                data.append(titles[0])
                data.append(' ')                            #若外文名不存在，留空
            image = re.findall(findImage,item)[0]
            data.append(image)
            link = re.findall(findLink,item)[0] #只打印一个       #使用正则表达式查找指定的字符串
            data.append(link)
            rating = re.findall(findRating,item)[0]
            data.append(rating)
            judge = re.findall(findJudge,item)[0]
            data.append(judge)
            inq = re.findall(findInq,item)                      #存在不存在的情况
            if len(inq)!=0:
                inq = inq[0].replace("。","")
                data.append(inq)
            else:
                data.append(" ")

            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd)   #去掉<br/>
            bd = re.sub('/'," ",bd)     #替换/
            data.append(bd.strip())     #去掉前后的空格

            datalist.append(data)               #处理好的一部电影

            print(datalist)
    return datalist

#保存数据
# def saveData(savepath):
#     print("数据已保存")

#保存数据
def saveData(datalist,savepath):
    print("save....")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)  #创建workbook对象
    sheet = book.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True)    #创建工作表
    col = ("影片中文名","电影详情链接","图片链接","影片外国名","评分","评价数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i]) #列名
    for i in range(0,250):
        print("第%d条" %(i+1))
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])      #数据

    book.save(savepath)       #保存

if __name__ == "__main__":          #当程序执行时
#调用函数
    main()