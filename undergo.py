from  selenium import webdriver
import time
import re
import lgin


#获取个人说说内容（若说说为个人所发：打印一遍，若为转发：打印两遍）
def then(html):

    content = re.findall('"con":"(.*?)"',html)
    d = {}
    les = len(content)
    f = open('diary.txt','w+')
    for j in range(les):
        d = {"说说内容":content[j]}
        for key in d:
            f.write(d[key])
            f.write('\t')
        f.write('\n')
    f.close() 
    
