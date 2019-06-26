#!/usr/bin/env python
#/usr/bin/python3
#!#/usr/bin/python3
#-*- coding:utf-8 -*-
 
from aip import AipSpeech
import http.cookiejar as cookielib
import json
# author : wangzhen <wangzhenjjcn@gmail.com> since 2019-03-15
import os
import re
import sys
import hashlib
import pygame
import time
import urllib
import lxml
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import config
import core 


showweb=False

browser=None
login_url=None
search_page_url=None
username=None
password=None
user_data_dir=None
driver_dir=None

username_input=None
password_input=None
login_btn=None
login_sucess_name=None



search_input=None
search_btn=None
search_resault_page_xpath=None
search_resault_page=None
search_resault_list_xpath=None
search_resault_list=None


def readConfig():
    global search_resault_list_xpath,search_resault_page_xpath,login_sucess_name,search_page_url,driver_dir,user_data_dir,username,password,login_url,password_input,username_input,login_btn,search_input,search_btn
    if not os.path.exists("config.ini"):
        print("配置文件不存在，创建新配置")
        with open("config.ini", 'w+', encoding='utf_8') as f:
            print("初始化空配置文件")
    login_url=config.getConf('康明登录链接','http://kmpc.szkm1.suyaool.com/_account/login.shtml','网址设置')
    search_page_url=config.getConf('康明搜索页链接','http://fw9.yyjzt.com/','网址设置')
    username_input=config.getConf("康明用户名输入框",'//*[@id="userName"]',"抓取设置")
    password_input=config.getConf("康明密码输入框",'//*[@id="password"]',"抓取设置")
    login_btn=config.getConf("康明登陆按钮",'//*[@id="btn_sub"]',"抓取设置")
    login_sucess_name=config.getConf("康明登陆成功用户名",'//*[@id="userStateInfo"]/li[4]/div[1]/a',"抓取设置")
    username=config.getConf("康明登录用户名",'登录用户名',"账号设置")
    password=config.getConf("康明登陆密码",'登陆密码',"账号设置")
    if username=="登录用户名" or password=="登陆密码":
        print("康明用户名密码错误！请输入！")
        username=input("请输入康明用户名：")
        password=input("请输入康明密码：")
        config.writeConfig("康明登录用户名",username,"账号设置")
        config.writeConfig("康明登陆密码",password,"账号设置")
    search_input=config.getConf("康明搜索输入框",'//*[@id="searchForm"]/div/input',"抓取设置")
    search_btn=config.getConf("康明搜索按钮",'//*[@id="searchForm"]/div/button[1]',"抓取设置")

    search_resault_page_xpath=config.getConf("康明搜索结果页数",'/html/body/div[2]/div[2]/div[2]/div/table/tbody/tr/td[2]/div[4]/div[1]/div/div[3]/span[2]',"抓取设置")
    search_resault_list_xpath=config.getConf("康明搜索结果列表",'/html/body/div[2]/div[2]/div[2]/div/table/tbody/tr/td[2]/div[4]/div[2]',"抓取设置")
    user_data_dir=config.getConf("谷歌用户目录",'',"目录设置")
    driver_dir=config.getConf("谷歌驱动目录",os.path.dirname(os.path.realpath(sys.argv[0]))+'\\chromedriver.exe',"目录设置")

def initWeb():
    global browser,user_data_dir,driver_dir,showweb
    try:
        chrome_options = webdriver.ChromeOptions()
        if user_data_dir==None:
            user_data_dir=os.getenv('TEMP')+"\\"+"yyjzt"+"\\"+str(time.time()).replace(".","")+"\\"
            config.writeConfig("谷歌用户目录",user_data_dir,"通用设置")
        chrome_options.add_argument('--user-data-dir='+user_data_dir)
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--profile-directory=Default')
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-plugins-discovery")
        chrome_options.add_argument("--start-maximized")
        if showweb:
            print("现在显示打开模式")
        else:
            print("显示处于后台模式")
            # if userwannashowweb==False:
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--enable-javascript')
        chrome_options.add_argument('--log-level=1')
        chrome_options.add_argument('--disable-popup-blocking')
        chrome_options.add_argument('-–single-process')
        chrome_options.add_argument('--ignore-ssl-errors')
        browser = webdriver.Chrome(chrome_options=chrome_options,executable_path=driver_dir)
        # if webpageerr:
        #     print("cookie keep")
        # else:
        #     browser.delete_all_cookies()
        browser.set_page_load_timeout(5000) 
        # browser.get(url)
        return browser
    except Exception as e:
        print("err in getBrowser")
        print(e)
        return None


def saveCookie(browser):
    cookies = browser.get_cookies()
    jsonCookies = json.dumps(cookies)
    with open('kmcookies.json', 'w+', encoding='utf_8') as f:
        f.write(jsonCookies)


def loadCookie(browser):
    print("尝试读取登录历史->登录网站")
    if not os.path.exists('kmcookies.json'):
        print("登录文件不存在，取消历史登录")
        return False
    if browser==None:
        print("Browser None")
        return False
    with open('kmcookies.json', 'r+', encoding='utf_8') as f:
        listCookies = json.loads(f.read())
    
    print("正在添加登录信息，请稍候...")
    for cookie in listCookies:
        browser.add_cookie({
            'domain': cookie['domain'],
            'name':cookie['name'],
            'value':cookie['value'],
            'path':'/',
            'expires':None
        })
    print("登录文件读取成功")
    return True


def wait_login():
    global browser,login_url,username_input,password_input,username,password,login_sucess_name,showweb
    quitBrowser()
    browser=initWeb()
    browser.get(search_page_url)
    while showweb:
        try:
            print("自动登录异常！请手动登录！！！！！！")
            login_name=browser.find_element_by_xpath(login_sucess_name)
            login_name=login_name.text
            print("  登陆成功："+login_name)
            showweb=False
            saveCookie(browser)
            quitBrowser()
            browser=initWeb()
            loadCookie(browser)
        except Exception as e:
            print(" err in wait_login")
            print(e)
            print("10秒后重新校验是否登录成功")
            time.sleep(10)
    
    try:
        login_name=browser.find_element_by_xpath(login_sucess_name)
        login_name=login_name.text
        print("  登陆成功："+login_name)
    except Exception as e:
        print(" err in wait_login")
        print(e)
        print("没有成功登录")
        showweb=True
        wait_login()
        time.sleep(10)


def doLogin():
    global browser,login_url,username_input,password_input,username,password,login_sucess_name,showweb
    try:
        browser.get(login_url)
        time.sleep(3)
        # print("输入用户名")
        print(username_input)
        print(username)
        browser.find_element_by_xpath(username_input).click()
        time.sleep(1)
        browser.find_element_by_xpath(username_input).send_keys(username) 
        time.sleep(1)
        # print("密码")
        print(password_input)
        print(password)
        browser.find_element_by_xpath(password_input).click()
        time.sleep(1)
        browser.find_element_by_xpath(password_input).send_keys(password) 
        time.sleep(1)
        browser.find_element_by_xpath(login_btn).click()
        time.sleep(3)

        login_name=browser.find_element_by_xpath(login_sucess_name)
        login_name=login_name.text
        print("  登陆成功："+login_name)
        pass
    except Exception as e:
        print(" err in doLogin")
        print(e)
        showweb=True
        wait_login()

def doSearch(searchword):
    global showweb,browser,search_input,search_btn,search_resault_page_xpath,search_resault_page,search_resault_list_xpath,search_resault_list,search_page_url
    if browser==None:
        showweb=False
        readConfig()
        initWeb()
        doLogin()
    goods={}
    if "http" in keyword:
        browser.get(keyword)
    else:
        browser.get(search_page_url)
        time.sleep(5)
        browser.find_element_by_xpath(search_input).send_keys(searchword) 
        time.sleep(0.1)
        browser.find_element_by_xpath(search_btn).click()
    time.sleep(5)
    browser.find_element_by_link_text("列表").click()
    time.sleep(2)
    col_=BeautifulSoup(browser.page_source, "lxml").find("div",class_="facetTools-skin")
    col_as=col_.findAll("a")
    col_spans=col_.findAll("span")
    title_str=" "
    for a in col_as:
        title_str+=a.text.replace(" ","").replace("\n","")+"-"
    for span in col_spans:
        title_str+=span.text.replace(" ","").replace("\n","")+"-"
    # print(title_str[:len(title_str)-2])
    goods["key"]=title_str[:len(title_str)-1]
    if "http" in keyword:
        goods["key"]=goods["key"].replace("Home-","").replace("“","").replace("”","").replace("搜索","")
    else:
        goods["key"]=searchword
    search_resault_page=0
    try:
        search_resault_page=BeautifulSoup(browser.page_source, "lxml").find("span",class_="pagenum")
        # //*[@id="container_m_search_result_list"]/div/p[2]
        search_resault_page=search_resault_page.text.replace("共计","").replace("页","").replace(" ","").split('/')[1]
        search_resault_page=int(search_resault_page)
        # print(search_resault_page)
    except Exception as e:
            print(" err in search_resault_page")
            print(e)

    print("一共{0}页结果，开始解析".format(search_resault_page))
    goods_data=[]
    # print(search_resault_page)

 
    for i in range(0,search_resault_page):
        print(i)
        search_resault_list_div=BeautifulSoup(browser.page_source, "lxml").find("div",class_="p-list imgList")
        search_resault_divs=search_resault_list_div.findAll ("div",class_="pl-skin") 
        # print(len(search_resault_lis))
        print("当前第{0}页，此页列表共{1}个结果，解析中...".format(search_resault_page,str(len(search_resault_divs))))

        for div in search_resault_divs:
            try:
                noSellTip=div.find("div",class_="noSellTip")
                if noSellTip!=None:
                    if "商品禁售" in noSellTip.text or "商家尚未定价" in noSellTip.text:
                        p_info=div.find("div",class_="p-info")
                        info=p_info.find("div",class_="info")
                        productName=info.find("div",class_="productName")
                        if productName !=None:
                            productName_a=productName.find("a")
                            print("品名:"+productName_a.text.replace(" ","").replace("\n","").strip())
                        if "商品禁售" in noSellTip.text :
                            print("商品禁售")
                        if "商家尚未定价" in noSellTip.text :
                            print("商家尚未定价") 
 
                        continue



                good={}
          
 
                a_tag = div.find("div",class_="p-caption").find("a")
                if a_tag==None:
                    continue
                # print(a_tag.text)
                _goods_link="http://kmpc.szkm1.suyaool.com/"+a_tag.attrs["href"]
                # print("http://fw9.yyjzt.com/"+_goods_link)
                good['商品链接']=_goods_link

                good['图片链接']=""
                image_img=div.find("img")
                image_link=image_img.attrs["src"]
                if image_link!=None and  "http"  in image_link and  ".com"  in image_link:
                    good['图片链接']=image_link
                
                
                p_info=div.find("div",class_="p-info")
                # print(p_info.text)
                info=p_info.find("div",class_="info")
                #品名
                good['品名']=""
                productName=info.find("div",class_="productName")
                if productName !=None:
                    productName_a=productName.find("a")
                    good['品名']=productName_a.text.replace(" ","").replace("\n","").strip()
                    # print("品名:"+productName_a.text.replace(" ","").replace("\n","").strip())
                    
                #通用名
                good['通用名']=""
                generalName=info.find("div",class_="generalName")
                if generalName !=None:
                    generalName_value=generalName.find("span",class_="fieldValue")
                    good['通用名']=generalName_value.text.replace(" ","").replace("\n","").strip()
                    # print("通用名:"+generalName_value.text.replace(" ","").replace("\n","").strip())

                #规格
                good['规格']=""
                spec=info.find("div",class_="spec")
                if spec !=None:
                    spec_value=spec.find("span",class_="fieldValue")
                    good['规格']=spec_value.text.replace(" ","").replace("\n","").strip()
                    # print("规格:"+spec_value.text.replace(" ","").replace("\n","").strip())
                
                #单位
                good['单位']=""
                units=info.find("div",class_="units")
                if units !=None:
                    units_value=units.find("span",class_="fieldValue")
                    good['单位']=units_value.text.replace(" ","").replace("\n","").strip()
                    # print("单位:"+units_value.text.replace(" ","").replace("\n","").strip())

                #生产厂商
                good['生产厂商']=""
                factoryName=info.find("div",class_="factoryName")
                if factoryName !=None:
                    factoryName_value=factoryName.find("span",class_="fieldValue")
                    good['生产厂商']=factoryName_value.text.replace(" ","").replace("\n","").replace(";&nbsp","").strip()
                    # print("生产厂商:"+factoryName_value.text.replace(" ","").replace("\n","").replace(";&nbsp","").strip())

                #剂型
                good['剂型']=""
                dosageForm=info.find("div",class_="dosageForm")
                if dosageForm !=None:
                    dosageForm_value=dosageForm.find("span",class_="fieldValue")
                    good['剂型']=dosageForm_value.text.replace(" ","").replace("\n","").strip()
                    # print("剂型:"+dosageForm_value.text.replace(" ","").replace("\n","").strip())

                # 批准文号
                good['批准文号']=""
                approvalNO=info.find("div",class_="approvalNO")
                if approvalNO !=None:
                    approvalNO_value=approvalNO.find("span",class_="fieldValue")
                    good['批准文号']=approvalNO_value.text.replace(" ","").replace("\n","").strip()
                    # print("批准文号:"+approvalNO_value.text.replace(" ","").replace("\n","").strip())
                        
                # 品牌
                good['生产厂商']=""
                brandName=info.find("div",class_="brandName")
                if brandName !=None:
                    brandName_value=brandName.find("span",class_="fieldValue")
                    good['生产厂商']=brandName_value.text.replace(" ","").replace("\n","").strip()
                    # print("生产厂商:"+brandName_value.text.replace(" ","").replace("\n","").strip())
                        
                # 处方药
                good['处方药']=""
                isOTC=info.find("div",class_="isOTC")
                if isOTC !=None:
                    isOTC_value=isOTC.find("span",class_="fieldValue")
                    good['处方药']=isOTC_value.text.replace(" ","").replace("\n","").strip()
                    # print("处方药:"+isOTC_value.text.replace(" ","").replace("\n","").strip())
                packDesc=p_info.find("div",class_="packDesc")   
                packkagetype=packDesc.find("span")   
                # print(packkagetype.text)
                pakage=packkagetype.find("i")
                pakage_big=""
                pakage_mid=""


                good['大包装']=""
                good['中包装']=""
                if pakage!=None:
                    if "大包装" in  pakage.text :
                        pakage_big=pakage.text.split("大包装")[1].split(" ")[0].replace(":","").replace("：","") 
                        good['大包装']=""+pakage_big
                        # print("大包装:"+pakage_big)
                    if "中包装"  in  pakage.text:
                        pakage_mid=pakage.text.split("中包装")[1].split(" ")[0].replace(":","").replace("：","") 
                        good['中包装']=""+pakage_mid
                        # print("中包装:"+pakage_mid)
                
                p_priceInfo=div.find("div",class_="p-priceInfo")
                
                price=p_priceInfo.find("span",class_="price")
                good['价格']=price.text.replace(" ","").replace("\n","").replace("/","").strip()
                # print("--价格:"+price.text.replace(" ","").replace("\n","").replace("/","").strip())
                
                packUnits=p_priceInfo.find("span",class_="packUnits")
                good['单位']=packUnits.text.replace(" ","").replace("\n","").replace("/","").strip()
                # print("--单位:"+packUnits.text.replace(" ","").replace("\n","").replace("/","").strip())
                
                priceTip=p_priceInfo.find("span",class_="priceTip")
                priceTip=priceTip.text.split("：")
                good['建议价格']=priceTip[len(priceTip)-1].replace(" ","").replace("\n","").strip()
                # print("--建议价格:"+priceTip[len(priceTip)-1].replace(" ","").replace("\n","").strip())
                
                good['仓储状态']=""
                good['最近效期']=""
                stockState_a=p_priceInfo.find("a")
                stockState_i=stockState_a.find("i",class_=False)
                if stockState_i==None:
                    # print("--仓储状态:无货")
                    good['仓储状态']="无货"
                elif "有货" in stockState_i.text and "最近效期" in stockState_i.text:
                    # print("--仓储状态:有货")
                    good['仓储状态']="有货"
                    good['最近效期']=stockState_i.text.split("最近效期")[1].replace(":","").replace(" ","").replace("：","").replace(")","").replace("）","").replace("\n","").strip()
                    # print("最近效期："+stockState_i.text.split("最近效期")[1].replace(":","").replace(" ","").replace("：","").replace(")","").replace("）","").replace("\n","").strip())
                    # print("--仓储状态:"+stockState_i.text.replace(" ","").replace("\n","").strip())


                good['打折信息']=""
                saleTag=p_info.find("div",class_="saleTag-desc")
                if saleTag!=None:
                    good['打折信息']=saleTag.text
                goods_data.append(good)
            except Exception as e:
                print(" err in search")
                print(e)
        
        print("当前结果个数："+str(len(goods_data)))
        print("第{0}页读取成功，一共{1}页".format(i,search_resault_page))
        try:
            if i<search_resault_page:
                next_btn=browser.find_element_by_link_text("下一页")
                next_btn.click()
                time.sleep(3)
                pass
            pass
        except  Exception as e:
            print(" err in search find_element_by_link_text 下一页" )
            print(e)
    print("关键字："+goods["key"])
    print("结果个数："+str(len(goods_data)))
    goods["data"]=goods_data
    return goods
 

def saveData(goods):
    try:
        if len(goods["data"])<1:
            return
        with open(goods["key"]+".csv", 'a',encoding='GBK') as f:
            firstLine=""
            for key in goods["data"][0].keys():
                firstLine+=key+","
            firstLine=firstLine[:len(firstLine)-1]
            f.write(firstLine+"\n")
            for data in goods["data"]:
                dataLine=""
                for key in data.keys():
                    dataLine+=data[key]+","
                dataLine=dataLine[:len(dataLine)-1]
                f.write(dataLine+"\n")
            print("对关键字的检索结束，已经存为文件。")
    
    except Exception as e:
        print(" err in saveData")
        print(e) 

  
def quitBrowser():
    global browser
    if browser==None:
        return
    try:
        browser.quit()
    except Exception as e:
        print(" err in quitBrowser")
        print(e)


if __name__ == '__main__':
    try:
        showweb=True
        readConfig()
        initWeb()
        doLogin()
        while True:
            keyword=input("输入要搜索的关键字按回车：")
            if keyword!=None and keyword!="":
                goods=doSearch(keyword)
                print(goods["key"])
                saveData(goods)
    except Exception as e:
        print(" err in main")
        print(e)
        quitBrowser()
    finally:
        quitBrowser()