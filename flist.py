from  selenium import webdriver
import time
import re
import csv
import lgin

#打印好友列表和亲密度等信息
def then(html):
    d = {}
    uin = re.findall('"uin":(\d+)',html)
    nickname = re.findall('"name":"(.*?)"',html)
    index= re.findall('"index":(\d+)',html)
    score = re.findall('"score":(\d+)',html)
    special_flag = re.findall('"special_flag":"(.*?)"',html)
    les = len(uin)
    f = open('friendlist.txt','w+')
    for j in range(les):
        if special_flag[j] == '0':
            special_flag[j] = '普通'  
        else:
            special_flag[j] = '特别关心'
        d = {"序号":index[j],"好友QQ":uin[j],"昵称":nickname[j],"亲密度":score[j],"是否为特别关心":special_flag[j]}
        for key in d:
            f.write(d[key])
            f.write('\t')
        f.write('\n')
    f.close() 
