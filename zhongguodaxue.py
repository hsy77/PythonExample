import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist,html):#将一个页面放到一个ulist中
    soup=BeautifulSoup(html,"html.parser")
    for tr in soup.find("tbody").children:#从tbody中找到tr
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')#从tr中找到td
            ulist.append([tds[0].string,tds[1].string,tds[3].string])
    pass                      #不做任何操作

def printUnivList(ulist,num):#打印ulist的多少个（num）
    tplt="{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))

def main():
    uinfo=[]
    url="http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    html=getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)#20 univs

main()
