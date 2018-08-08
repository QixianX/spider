from  selenium import webdriver
import time
import re
import album

#登录获取url的程序
def loginn(name,pwd):
    browser = webdriver.Chrome()
    browser.get('https://user.qzone.qq.com')


#跳转到用户名密码形式
    browser.switch_to_frame('login_frame')
    log = browser.find_element_by_id("switcher_plogin")
    log.click()
    time.sleep(0.5)


#定位用户名框并输入
    use = browser.find_element_by_id('u')
    use.send_keys(name)


#定位密码框并输入
    ps = browser.find_element_by_id('p')
    ps.send_keys(pwd)
    btn = browser.find_element_by_id('login_button')
    time.sleep(0.5)
    btn.click()
    time.sleep(0.5)
    
    
 #跳转到个人主页
    inf = browser.find_element_by_link_text("我的主页")
    inf.click()


#获得cookie
    cookie= {}
    hashes = 5381
    for i in browser.get_cookies():
        cookie[i["name"]] = i["value"]
    print(cookie)
        

#计算gtk
    for letter in cookie['p_skey']:
        hashes += (hashes << 5) + ord(letter)
    hashes = hashes & 0x7fffffff
    hashes = str(hashes)

    
 #获得token
    html = browser.page_source
    g_qzonetoken=re.search('window\.g_qzonetoken = \(function\(\)\{ try\{return (.*?);\} catch\(e\)',html)
    g_qzonetoken = str(g_qzonetoken[0]).split('\"')[1]
    g_qzonetoken =str(g_qzonetoken)


#获得个人信息url写到本地
    url =  'https://h5.qzone.qq.com/proxy/domain/base.qzone.qq.com'+\
          '/cgi-bin/user/cgi_userinfo_get_all?uin='+name+\
          '&vuin='+name+'&fupdate=1&rd='+'0.7137596336600174'+\
          '&g_tk='+hashes+'&qztoken='+g_qzonetoken
    pass


    
#获得相册html,调用保存函数
    url1 = 'https://h5.qzone.qq.com/proxy/domain/photo.qzon'+\
           'e.qq.com/fcgi-bin/fcg_list_album_v3?g_tk='+\
           hashes+'&callback=shine0_Callback&t=261523179&hostUin='+name+'&uin='+name+\
           '&appid=4&inCharset=utf-8&outCharset=utf-8&source=qzone&plat=qzone'\
           +'&format=jsonp&notice=0&filter=1&handset=4&pageNumModeSort=40&'+\
           'pageNumModeClass=15&needUserInfo=1&idcNum=4&callback'+\
           'Fun=shine0&_=1533627125951'
    time.sleep(1)
    page = browser.get(url1)
    html = browser.page_source 
    album.al(html)

#好友列表
    #url2 =
    pass



