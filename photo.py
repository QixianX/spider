from  selenium import webdriver
import time
import re
import urllib.request


def save(html,count):

    
#获取图片url
    newlist = []
    imglist = re.findall('"url" : "(.*?)"',html)
    #print(imglist)
    count+=1
    con = str(count)

    
 #解密
    for i in imglist:
        i = i.split('\\')
        i = ''.join(i)
        newlist.append(i)
        lens = len(newlist)

        
#保存图片到指定路径
    for m in range(lens):
        n = str(m) 
        filename = 'd:/ImageSave/'+con+n+'.jpg'
        urllib.request.urlretrieve(newlist[m],filename)
        time.sleep(2)


