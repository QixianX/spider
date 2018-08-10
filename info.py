import re
import urllib.request
from selenium import webdriver
import time
import hashlib


def inf(html1):
    nickname = re.findall('"nickname":"(.*?)"',  html1)  # 昵称
    gender = re.findall('"sex":(\d+)', html1)  # 性别
    age = re.findall('"age":(\d+)',  html1)  # 年龄
    birthday = re.findall('"birthday":"(.*?)"',  html1)  # 生日
    birthyear = re.findall('"birthyear":(\d+)',  html1)  # 出生年
    constellation = re.findall('"constellation":(\d+)',  html1)  # 星座
    bloodtype = re.findall('"bloodtype":(\d+)',  html1)  # 血型
    marriage = re.findall('"marriage":(\d+)',  html1)  # 婚姻状况
    living_country = re.findall('"country":"(.*?)"',  html1)  # 居住地（国家）
    living_province = re.findall('"province":"(.*?)"',  html1)  # 居住地（省份）
    living_city = re.findall('"city":"(.*?)"',  html1)  # 居住地（城市）
    hometown_country = re.findall('"hco":"(.*?)"',  html1)  # 故乡（国家）
    hometown_provine = re.findall('"hp":"(.*?)"', html1)  # 故乡（省份）
    hometown_city = re.findall('"hc":"(.*?)"',  html1)  # 故乡（城市）
    career = re.findall('"career":"(.*?)"',  html1)  # 职业
    company = re.findall('"company":"(.*?)"',  html1)  # 公司名称
    company_country = re.findall('"cco":"(.*?)"',  html1)  # 公司地址（国家）
    company_province = re.findall('"cp":"(.*?)"',  html1)  # 公司地址（省份)
    company_city = re.findall('"cc":"(.*?)"',  html1)  # 公司地址（城市）
    company_address = re.findall('"cb":"(.*?)"',  html1)  # 公司详细地址


    if '1' in gender:
        gender[0] = "男"
    elif '0' in gender:
        gender[0] = "女"
    if '4' in constellation:
        constellation[0] = "狮子座"
    else:
        constellation[0] = "其他"
    if '3' in bloodtype:
       bloodtype[0] = "O"
    else:
       bloodtype[0] = "其他"
    if '1' in marriage:
       marriage[0] = "单身"
    else:
       marriage[0] = "其他"
    
    d={'昵称':nickname,'性别':gender,'年龄':age,'生日':birthday,'出生年':birthyear,
         '星座':constellation,
         '血型': bloodtype,'婚姻状况': marriage,'居住地（国家）':living_country,
         '居住地（省份）':living_province,'居住地（城市）':living_city,
         '故乡（国家）':hometown_country,'故乡（省份）':hometown_provine,
         '故乡（城市）':hometown_city,'职业':career ,'公司名称':company,
         '公司地址（国家':company_country , '公司地址（省份)':company_province,
         '公司地址（城市）':company_city,'公司详细地址':company_address,}
    print(d)
    #加密
    a=[]
    b=[]
    #将字典中键和值循环取出添加到列表中
    for i in d.keys():
        a.append(i)
        a.append(d[i])
    print (a)
    lens = len(a)
    for i in range(lens):
        if i%2 == 1:
            x=a[i][0]
            x = str(x)
            b.append(x)
        else:
            x = a[i]
            x = str(x)
            b.append(x)
    print(b)
    c=("".join(b))
    print(c)
    s=hashlib.md5(c.encode(encoding='UTF-8')).hexdigest()
    print(s)
    f=open('jiami.txt','w')
    f.write(s)
    f.close()
    
