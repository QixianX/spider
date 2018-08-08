import time
import re
import urllib.request


def al(html):

    
    #获取图片url
    newlist = []
    imglist = re.findall(r'\bh\S*?A\b', html)


    #解密
    for i in imglist:
        i = i.split('\\')
        i = ''.join(i)
        newlist.append(i)
        

    #保存图片到指定路径
    for each in newlist:
        filename = 'C:\\Users\hp\Desktop\qqs\ImageSave\\'+each.split('/')[-1]+'.jpg'
        urllib.request.urlretrieve(each,filename)
        time.sleep(1)
