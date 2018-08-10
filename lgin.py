from  selenium import webdriver
import time
import re
import photo
import info
import undergo
import flist


#登录获取url的程序，后台运行浏览器
def loginn(name,pwd):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get('https://user.qzone.qq.com')


#跳转到用户名密码形式
    browser.switch_to_frame('login_frame')
    log = browser.find_element_by_id("switcher_plogin")
    log.click()
    time.sleep(0.5)


#定位用户名框并输入
    use = browser.find_element_by_id('u')
    use.send_keys(name)


#定位密码框并输入，判断是否登录成功
    ps = browser.find_element_by_id('p')
    ps.send_keys(pwd)
    btn = browser.find_element_by_id('login_button')
    time.sleep(0.5)
    btn.click()
    time.sleep(0.5)
    right = 'https://user.qzone.qq.com/'+name
    now_url = browser.current_url
    if now_url == right:
        print('登录成功')
    else:
        print('账号或密码错误')
              
          
#跳转到我的主页
    inf = browser.find_element_by_link_text("我的主页")
    inf.click()


#获得cookie
    cookie= {}
    hashes = 5381
    for i in browser.get_cookies():
        cookie[i["name"]] = i["value"]
        

#计算gtk
    for letter in cookie['p_skey']:
        hashes += (hashes << 5) + ord(letter)
    hashes = hashes & 0x7fffffff
    hashes = str(hashes)

    
 #获得token
    html = browser.page_source
    g_qzonetoken=re.search('window\.g_qzonetoken'+\
                           ' = \(function\(\)\{ try\{return (.*?);\} catch\(e\)',html)
    g_qzonetoken = str(g_qzonetoken[0]).split('\"')[1]
    g_qzonetoken =str(g_qzonetoken)


#获得个人信息url写到本地
    url =  'https://h5.qzone.qq.com/proxy/domain/base.qzone.qq.com'+\
          '/cgi-bin/user/cgi_userinfo_get_all?uin='+name+\
          '&vuin='+name+'&fupdate=1&rd='+'0.7137596336600174'+\
          '&g_tk='+hashes+'&qztoken='+g_qzonetoken
    page = browser.get(url)
    html1 = browser.page_source
    info.inf(html1)


#获取好友列表并保存在本地
    url = 'https://user.qzone.qq.com/proxy/dom'+\
          'ain/r.qzone.qq.com/cgi-bin/tfriend/f'+\
          'riend_ship_manager.cgi?uin='+name+\
          '&do=1&rd=0.07649617356193117&fupd'+\
          'ate=1&clean=1&g_tk='+hashes+'&qzonetoken='+\
          g_qzonetoken+'&g_tk='+hashes
    page = browser.get(url)
    html = browser.page_source
    flist.then(html)

   
#获得相册html,调用保存函数
    url1 = 'https://h5.qzone.qq.com/proxy/domain/photo.qzon'+\
           'e.qq.com/fcgi-bin/fcg_list_album_v3?g_tk='+\
           hashes+'&callback=shine0_Callback&t=26152317'+\
           '9&hostUin='+name+'&uin='+name+\
           '&appid=4&inCharset=utf-8&outCharset=utf-8&source=qzone&plat=qzone'\
           +'&format=jsonp&notice=0&filter=1&handset=4&pageNumModeSort=40&'+\
           'pageNumModeClass=15&needUserInfo=1&idcNum=4&callback'+\
           'Fun=shine0&_=1533627125951'
    time.sleep(1)
    page = browser.get(url1)
    html = browser.page_source
    time.sleep(1)
    pid = re.findall('"id" : "(.*?)"', html)
    count = 0
    time.sleep(1)
    for i in pid:
        alid = i
        url =  'https://h5.qzone.qq.com/proxy/domain/photo.qzone.'+\
              'qq.com/fcgi-bin/cgi_list_photo?g_tk='+hashes+'&callback'+\
              '=shine0_Callback&t=984071564&mode=0&idcNum=4'+\
              '&hostUin='+name+'&topicId='+alid+'&noTopic=0&uin='+name+\
              '&pageStart=0&pageNum=30&skipCmtCount=0&singleurl='+\
              '1&batchId=&notice=0&appid=4&inCharset=utf-8&outCharset='+\
              'utf-8&source=qzone&plat=qzone&outstyle=json&format=jsonp&json_esc=1&questi'+\
              'on=&answer=&callbackFun=shine0&_=1533781622395'      
        page = browser.get(url)
        html = browser.page_source
        time.sleep(2)
        photo.save(html,count)
        count+=1


#获得说说
    url = 'https://user.qzone.qq.com/proxy/'+\
          'domain/taotao.qq.com/cgi-bin/emo'+\
          'tion_cgi_msglist_v6?uin='+name+'&ftype=0&s'+\
          'ort=0&pos=0&num=20&replynum=100&g_tk='+hashes+\
          '&callback=_preloadCallback&code_version=1&f'+\
          'ormat=jsonp&need_private_comment=1&qzonetoken='+\
          g_qzonetoken+'&g_tk='+hashes
    page = browser.get(url)
    html = browser.page_source
    undergo.then(html)




