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


showweb=True

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
    login_url=config.getConf('登录链接','http://fw9.yyjzt.com/user/login.htm','网址设置')
    search_page_url=config.getConf('搜索页链接','http://fw9.yyjzt.com/','网址设置')
    username_input=config.getConf("用户名输入框",'//*[@id="jzt_username"]',"抓取设置")
    password_input=config.getConf("密码输入框",'//*[@id="jzt_password"]',"抓取设置")
    login_btn=config.getConf("登陆按钮",'//*[@id="login_form_id"]/div[4]/button',"抓取设置")
    login_sucess_name=config.getConf("登陆成功用户名",'/html/body/div[4]/div/div[2]/div[2]/div[1]/a[2]',"抓取设置")
    username=config.getConf("登录用户名",'登录用户名',"账号设置")
    password=config.getConf("登陆密码",'登陆密码',"账号设置")
    if username=="登录用户名" or password=="登陆密码":
        print("用户名密码错误！请输入！")
        username=input("请输入用户名：")
        password=input("请输入密码：")
        config.writeConfig("登录用户名",username,"账号设置")
        config.writeConfig("登录用户名",password,"账号设置")
    search_input=config.getConf("搜索输入框",'//*[@id="searchText"]',"抓取设置")
    search_btn=config.getConf("搜索按钮",'//*[@id="searchMerchandiseBtn"]',"抓取设置")
    search_resault_page_xpath=config.getConf("搜索结果页数",'//*[@id="container_remove"]/div/nav/div/span[1]',"抓取设置")
    search_resault_list_xpath=config.getConf("搜索结果列表",'//*[@id="container_m_search_result_list"]/ul',"抓取设置")
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
     
def doLogin():
    global browser,login_url,username_input,password_input,username,password,login_sucess_name
    try:
        browser.get(login_url)
        time.sleep(5)
        # print("输入用户名")
        browser.find_element_by_xpath(username_input).send_keys(username) 
        time.sleep(0.1)
        # print("密码")
        browser.find_element_by_xpath(password_input).send_keys(password) 
        time.sleep(0.1)
        browser.find_element_by_xpath(login_btn).click()
        time.sleep(3)
        login_name=browser.find_element_by_xpath(login_sucess_name)
        login_name=login_name.text
        print("  登陆成功："+login_name)
        pass
    except Exception as e:
        print(" err in doLogin")
        print(e)

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
        goods["key"]=searchword
        browser.get(search_page_url)
        time.sleep(5)
        browser.find_element_by_xpath(search_input).send_keys(searchword) 
        time.sleep(0.1)
        browser.find_element_by_xpath(search_btn).click()
    time.sleep(2)
    col_=BeautifulSoup(browser.page_source, "lxml").find("div",class_="breadcrumbs m_crumb_search")
    col_ul=col_.find("ul")
    col_lis=col_ul.findAll("li")
    title_str=""
    for li in col_lis:
        title_str+=li.text.replace(" ","").replace("\n","")+"-"
    # print(title_str[:len(title_str)-2])
    goods["key"]=title_str[:len(title_str)-1]
    search_resault_page=0
    try:
        search_resault_page=browser.find_element_by_xpath(search_resault_page_xpath)
        # //*[@id="container_m_search_result_list"]/div/p[2]
        search_resault_page=search_resault_page.text.replace("共计","").replace("页","").replace(" ","")
        search_resault_page=int(search_resault_page)
    except Exception as e:
            print(" err in search_resault_page")
            print(e)

    print("一共{0}页".format(search_resault_page))
    goods_data=[]
    # print(search_resault_page)
    for i in range(1,search_resault_page):
        search_resault_list_ul=BeautifulSoup(browser.page_source, "lxml").find("ul",class_="m_search_lst f_cbli")
        search_resault_lis=search_resault_list_ul.findAll ("li",class_=False) 
        # print(len(search_resault_lis))
        for li in search_resault_lis:
            try:
                good={}
                a_tag = li.find("a",class_="u_img u_goods_img",proid=True)
                if a_tag==None:
                    continue
                _goods_link="http://fw9.yyjzt.com/"+a_tag.attrs["onclick"].split('\'')[1]
                # print("http://fw9.yyjzt.com/"+_goods_link)
                good['link']=_goods_link
                m_goods_action =li.find("div",class_="m_goods_action")
                u_goods_stock=m_goods_action.find("p",class_="u_goods_stock")
                u_goods_stock=u_goods_stock.find("span",class_="u_goods_txt")
                if "无库存" in u_goods_stock.text:
                    # print("商品无库存")
                    continue
                if "无" in u_goods_stock.text:
                    continue
                good['stock']=u_goods_stock.text.replace(" ","").replace("\n","")
                # print("u_goods_stock:"+u_goods_stock.text.replace(" ","").replace("\n",""))
                m_goods_deta =li.find("div",class_="m_goods_deta")
                m_goods_tb=m_goods_deta.find("table",class_="table m_goods_tb")
                m_goods_trs=m_goods_tb.findAll("tr")
                # print(len(m_goods_trs))
                m_goods_tds1=m_goods_trs[0].findAll("td")
               
                image_img=li.find("img")
                image_link=image_img.attrs["src"]
                if image_link!=None and  "http"  in image_link and  ".com"  in image_link:
                    good['img']=image_link
                else:
                    image_link=image_img.attrs["onerror"].split('\'')[1]
                    if image_link.startswith("//"):
                        image_link="http:"+image_link
                    good['img']=image_link

                tr1_a_tag=m_goods_trs[0].find("a")
                good['name']=tr1_a_tag.text.replace(" ","").replace("\n","")
                # print("tr1_a_tag:"+tr1_a_tag.text.replace(" ","").replace("\n",""))
                m_tag=m_goods_trs[0].find("span",class_="m_tag m_tag_kw")
                good['goods_type']=m_tag.text.replace(" ","").replace("\n","")
                # print("m_tag:"+m_tag.text.replace(" ","").replace("\n",""))
                m_tag_kw=m_tag.nextSibling
                good['goods_name']=m_tag_kw.replace(" ","").replace("\n","")
                # print("m_tag_kw:"+m_tag_kw.replace(" ","").replace("\n",""))
                print("读取到新数据："+m_tag_kw.replace(" ","").replace("\n",""))
                u_goods_spec=m_goods_trs[0].find("span",class_="u_goods_spec")
                u_goods_spec_text=u_goods_spec.text.replace(" ","").replace("\n","")
                if u_goods_spec_text.startswith("/"):
                    u_goods_spec_text=u_goods_spec_text[1:]
                good['goods_spec']=u_goods_spec_text
                # print("u_goods_spec:"+u_goods_spec.text.replace(" ","").replace("\n",""))
                u_goods_pric=m_goods_trs[0].find("span",class_="u_goods_pric")
                good['goods_price']=u_goods_pric.text.replace(" ","").replace("\n","")
                # print("u_goods_pric:"+u_goods_pric.text.replace(" ","").replace("\n",""))
                u_goods_unit=m_goods_tds1[1].find("span",class_="u_goods_unit")
                u_goods_unit_text=u_goods_unit.text.replace(" ","").replace("\n","")
                if u_goods_unit_text.startswith("/"):
                    u_goods_unit_text=u_goods_unit_text[1:]
                good['goods_unit']=u_goods_unit_text
                # print("u_goods_unit:"+u_goods_unit.text.replace(" ","").replace("\n",""))
                m_goods_tds2=m_goods_trs[1].findAll("td")

                u_goods_com=m_goods_tds2[0].find("p",class_="u_goods_com")
                good['goods_com']=u_goods_com.text.replace(" ","").replace("\n","")
                # print("u_goods_com:"+u_goods_com.text.replace(" ","").replace("\n",""))
                
                u_goods_suprice=m_goods_tds2[1].find("span",class_="u_goods_field u_goods_suprice")
                if u_goods_suprice!=None:
                    good['goods_suprice']=u_goods_suprice.text.replace(" ","").replace("\n","")
                else:
                    good['goods_suprice']="-"
                # print("u_goods_suprice:"+u_goods_suprice.text.replace(" ","").replace("\n",""))
                
                u_goods_form=m_goods_tds2[2].find("span",class_="u_goods_field")
                good['goods_form']=u_goods_form.text.replace(" ","").replace("\n","")
                # print("m_goods_des:"+u_goods_form.text.replace(" ","").replace("\n",""))

                u_goods_ischailin=m_goods_tds2[2].findAll("span",class_="m_tag m_tag_kw")[0]
                good['goods_ischai']=u_goods_ischailin.text.replace(" ","").replace("\n","")
                # print("m_goods_des:"+u_goods_ischailin.text.replace(" ","").replace("\n",""))
                u_goods_chailin=m_goods_tds2[2].findAll("span",class_="m_tag m_tag_kw")[1]
                good['goods_form2']=u_goods_chailin.text.replace(" ","").replace("\n","")
                # print("m_goods_des:"+u_goods_chailin.text.replace(" ","").replace("\n",""))
                
                m_goods_tds3=m_goods_trs[2].findAll("td")

                u_goods_tags=m_goods_tds3[0].find("p",class_="u_goods_tags")
                if u_goods_tags!=None:
                    good['goods_usage']=u_goods_tags.text.replace(" ","").replace("\n","")
                    # print("u_goods_tags:"+u_goods_tags.text.replace(" ","").replace("\n",""))
                else:
                    good['goods_usage']="-"

                u_goods_exp_start=m_goods_tds3[2].find("span",class_="u_goods_exp_start")
                good['goods_exp_start']=u_goods_exp_start.text.replace(" ","").replace("\n","")
                # print("u_goods_exp_start:"+u_goods_exp_start.text.replace(" ","").replace("\n",""))
                u_goods_exp_end=m_goods_tds3[2].find("span",class_="u_goods_exp_end")
                good['goods_exp_end']=u_goods_exp_end.text.replace(" ","").replace("\n","")
                # print("u_goods_exp_end:"+u_goods_exp_end.text.replace(" ","").replace("\n",""))
                goods_data.append(good)
            except Exception as e:
                print(" err in search")
                print(e)
        if i<search_resault_page:
            print("第{0}页读取成功，一共{1}页".format(i,search_resault_page))
            next_btn=browser.find_element_by_link_text("下一页")
            next_btn.click()
            print("当前结果个数："+str(len(goods_data)))
            time.sleep(3)
            # //*[@id="container_remove"]/div/nav/ul/li[13]/a
            pass
    goods["data"]=goods_data
    print(len(goods_data))
    time.sleep(5)
    
    return goods
 

def saveData(goods):
    with open(goods["key"]+".csv", 'a',encoding='GBK') as f:
        f.write("供应商,药品类别,药品名称,药品规格,生产厂家,价格,推荐售价,功能主治,包装单位,中包装,是否拆零,大包装,近效期,远效期,库存,商品链接,图片"+"\n")
        for good in goods["data"]:
            f.write('{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16}'.format("九州通",good['goods_type'],good['goods_name'],good['goods_spec'],good['goods_com'],good['goods_price'],good['goods_suprice'],good['goods_usage'],good['goods_unit'],good['goods_form'],good['goods_ischai'],good['goods_form2'],good['goods_exp_start'],good['goods_exp_end'],good['stock'],good['link'],good['img'])+"\n")
            print("对关键字的检索结束，已经存为文件。")

def quitBrowser():
    global browser
    browser.quit()

if __name__ == '__main__':
    try:
        showweb=False
        readConfig()
        initWeb()
        doLogin()
        while True:
            keyword=input("输入要搜索的关键字按回车：")
            if keyword!=None and keyword!="":
                goods=doSearch(keyword)
                with open(goods["key"]+".csv", 'a',encoding='GBK') as f:
                    f.write("供应商,药品类别,药品名称,药品规格,生产厂家,价格,推荐售价,功能主治,包装单位,中包装,是否拆零,大包装,近效期,远效期,库存,商品链接,图片"+"\n")
                    for good in goods["data"]:
                        f.write('{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16}'.format("九州通",good['goods_type'],good['goods_name'],good['goods_spec'],good['goods_com'],good['goods_price'],good['goods_suprice'],good['goods_usage'],good['goods_unit'],good['goods_form'],good['goods_ischai'],good['goods_form2'],good['goods_exp_start'],good['goods_exp_end'],good['stock'],good['link'],good['img'])+"\n")
                        print("对关键字的检索结束，已经存为文件。")
    except Exception as e:
        print(" err in main")
        print(e)
    finally:
        browser.quit()