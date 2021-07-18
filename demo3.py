# -*- codeing = utf-8 -*-
# @Time : 2021/7/18 9:35
# @Auther : 亱華
# @File : demo3.py
# @SoftWare : PyCharm

from bs4 import BeautifulSoup
import bs4
import re
import urllib.request,urllib.error
import xlwt

def main():
    baseurl = "https://movie.douban.com/top250?start="
    #1.爬取网页
    #datalist = getData(baseurl)
    #2.逐一解析数据       ->    在爬取过程中边爬取边处理
    linklist = getData(baseurl)
    datalist = getInfo(linklist)

    #3.保存数据
    savepath = "豆瓣电影Top25详细数据.xls"
    saveData(datalist,savepath)
    #askURL("https://movie.douban.com/top250")

#影片链接规则
findLink = re.compile(r'<a href="(.*?)">')    #创建正则表达式对象(字符串匹配模式)
# findImage = re.compile(r'<img alt=.*src="(.*?) width=(.*)"/>',re.S)        #忽略换行符        #将width添加
# findTitle = re.compile(r'<span class="title">(.*)</span>')
# findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# findJudge = re.compile(r'<span>(\d*)人评价</span>')
# findInq = re.compile(r'<span class="inq">(.*)</span>')
# findBd = re.compile(r'<p class="">(.*?)</p>',re.S)
findName = re.compile(r'data-name="(.*?)"')
findSummary = re.compile(r'<span property="v:summary">(.*?)</span>',re.S)
findtype = re.compile(r'<span class="pl">类型:(.*?)</span><br/>',re.S)
findnation = re.compile(r'<span class="pl">制片国家/地区:</span>(.*?)<br/>')
findlanguage = re.compile(r'<span class="pl">语言:</span>(.*?)<br/>')
findelsname = re.compile(r'<span class="pl">又名:</span>(.*?)<br/>')

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
    linklist = []
    for i in range(0,1):                   #第一页
        url = baseurl
        html = askURL(url)                  #保存获取的网页原码
        #逐一处理数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):         #查找符合要求的字符串（搜寻每一个Item）
            #print(item)
            #data = []                                           #保存一部电影的所有信息
            item = str(item)                                    #转换为字符串

            #电影链接
            link = re.findall(findLink,item)[0] #只打印一个       #使用正则表达式查找指定的字符串
            linklist.append(link)
    #print(linklist)
    return linklist
            #data.append(link)


            #datalist.append(data)               #处理好的一部电影

            #print(datalist)
    #return datalist

def getInfo(linklist):
    datalist = []
    for link in linklist:
        data = []
        url = link
        html = askURL(url)
        soup = BeautifulSoup(html, "html.parser")
        strhtml = str(soup)
        #print(strhtml)

        #电影名称
        name = re.findall(findName,strhtml)
        # print(name)
        data.append(name)
        #电影总结
        summary = re.findall(findSummary,strhtml)
        # print(summary)
        data.append(summary)
        #电影类型
        type_mov = re.findall(findtype,strhtml)
        type_mov = str(type_mov)
        type_mov = type_mov.replace(r'</span> <span property="v:genre">',"")
        type_mov = type_mov.replace(r'</span>', "")
        type_mov = type_mov.replace(r'/ <span property="v:genre">', "")
        data.append(type_mov)
        # print(type_mov)
        #制片国家
        nation = re.findall(findnation,strhtml)
        data.append(nation)
        #print(nation)
        #语言
        language = re.findall(findlanguage,strhtml)
        data.append(language)
        #print(language)
        #又名
        elsename = re.findall(findelsname,strhtml)
        data.append(elsename)
        #print(elsename)

        datalist.append(data)

    #print(datalist)
    return datalist

    # for item in soup.find_all('div', class_="item"):  # 查找符合要求的字符串（搜寻每一个Item）
    #     data = []                                     # 保存一部电影的所有信息
    #     item = str(item)                              # 转换为字符串

        # summary = re.findall(findSummary,item)
        # print(summary)
        # name = re.findall(findName,item)
        # print(name)



#保存数据
# def saveData(savepath):
#     print("数据已保存")

#保存数据
def saveData(datalist,savepath):
    print("save....")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)  #创建workbook对象
    sheet = book.add_sheet('豆瓣电影Top25详细信息',cell_overwrite_ok=True)    #创建工作表
    col = ("影片中文名","总结","类型","国家","语言","又名")
    for i in range(0,6):
        sheet.write(0,i,col[i]) #列名
    for i in range(0,25):
        print("第%d条" %(i+1))
        data = datalist[i]
        for j in range(0,6):
            sheet.write(i+1,j,data[j])      #数据

    book.save(savepath)       #保存

if __name__ == "__main__":          #当程序执行时
#调用函数
    main()