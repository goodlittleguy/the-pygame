from requests import*
from bs4 import BeautifulSoup as bs
import time
import csv
import re
import random
def gettexturl(url,code="utf-8"):
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
    }
    r=get(url,headers=headers)
    r.raise_for_status()
    r.encoding=code
    html=r.text
    soup=bs(html,"lxml")
    return soup
def getinfo(url):
    soup=gettexturl(url)
    dict={}
    list=[]
    try:
        tittle=soup.select('#content > div.leftContent > ul > li > div.info.clear > div.title > a')
        address=soup.select('#content > div.leftContent > ul > li > div.info.clear > div.flood > div > a:nth-child(2)')
        info=soup.select('#content > div.leftContent > ul > li> div.info.clear > div.address > div')
        attention=soup.select('#content > div.leftContent > ul > li> div.info.clear > div.followInfo')
        good=soup.select('#content > div.leftContent > ul > li> div.info.clear > div.tag')
        price=soup.select('#content > div.leftContent > ul > li > div.info.clear > div.priceInfo > div.totalPrice > span')
        perprice=soup.select('#content > div.leftContent > ul > li > div.info.clear > div.priceInfo > div.unitPrice > span')
    except:
        print("失败")
        pass

    for ti,ad,fo,at,go,pr,per in zip(tittle,address,info,attention,good,price,perprice):
        dict["房名"]=ti.get_text().strip()
        dict["地址"] = ad.get_text().strip()
        dict["房型"] = fo.get_text().split("|")[0].strip()
        dict["/m2"] = fo.get_text().split("|")[1].strip()[:-2]
        dict["朝向"] = fo.get_text().split("|")[2].strip()
        dict["精装/简装"] = fo.get_text().split("|")[3].strip()

        lc = re.findall(r'.楼层', fo.get_text().strip())
        if lc == []:
            lc.append("无")
        dict["所处楼层"] = lc[0]
        jzlc = re.findall(r'共.*?层', fo.get_text().strip())
        if jzlc == []:
            jzlc.append("无")

        dict["建筑楼层"]=jzlc[0]

        year= re.findall(r'\d{4}年建', fo.get_text().strip())
        if year==[]:
            year.append("无")
        dict["建成时间"]=year[0]
        dict["房子类型"]=fo.get_text().strip().split("|")[-1].replace("\n","")
        dict["关注度/人"]=at.get_text().split("/")[0][:-3].strip()
        dict["发布时间/月"]=at.get_text().split("/")[1][:-6].strip()
        dict["房子总价/万元"]=pr.get_text()[:-1].strip()
        dict["单位房价 万/m2"]=per.get_text()[2:-4].strip()
        list.append(dict)
    return list

def main():
    place= ['tianhe','yuexiu','liwan','haizhu','panyu','baiyun','huangpugz', 'conghua','zengcheng','huadou','nansha']
    for i in place:
        with open(i+'.csv',"a",newline='',encoding="utf-8") as filed:
            fieldnames=["房名","地址","房型","/m2","朝向","精装/简装","所处楼层","建筑楼层","建成时间","房子类型","关注度/人","发布时间/月","房子总价/万元","单位房价 万/m2" ]
            writer = csv.DictWriter(filed, fieldnames=fieldnames)
            writer.writeheader()
            for pg in range(1,3):
                url="https://gz.lianjia.com/ershoufang/{}/pg{}/".format(i,str(pg))
                dict=getinfo(url)
                for i in dict:
                    writer.writerow(i)

                print("第{}页爬取成功".format(pg))
                time.sleep(random.randint(0,3))
main()
