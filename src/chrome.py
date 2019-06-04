#!/usr/bin/env python
#/usr/bin/python3
#!#/usr/bin/python3
#-*- coding:utf-8 -*-
# author : wangzhen <wangzhenjjcn@gmail.com> since 2019-03-15
 
import os
import sys
import time

from selenium import webdriver



class Chrome():
    def __init__(self, path):
        self.path = path
        self.browser=None
        self.chrome_options = None
        self.timeout=5000

    def initBrowser(self,tmp_path,driver_path):
        self.chrome_options = webdriver.ChromeOptions()
        try:
            if self.path!=None:
                self.chrome_options.add_argument('--user-data-dir='+tmp_path+"\\"+str(time.time()).replace(".","")+"\\")
                # chrome_options.add_argument('--user-data-dir='+self.path+"\\"+str(time.time()).replace(".","")+"\\")
            self.chrome_options.add_argument('--disable-extensions')
            self.chrome_options.add_argument('--profile-directory=Default')
            self.chrome_options.add_argument("--incognito")
            self.chrome_options.add_argument("--disable-plugins-discovery");
            self.chrome_options.add_argument("--start-maximized")
            self.chrome_options.add_argument('--headless')
            self.chrome_options.add_argument('--disable-gpu')
            self.chrome_options.add_argument('--ignore-certificate-errors')
            self.chrome_options.add_argument('--no-sandbox')
            self.chrome_options.add_argument('--enable-javascript')
            self.chrome_options.add_argument('--log-level=3')
            self.chrome_options.add_argument('--disable-popup-blocking')
            self.chrome_options.add_argument('-–single-process')
            self.chrome_options.add_argument('--ignore-ssl-errors')
            self.browser = webdriver.Chrome(chrome_options=self.chrome_options,executable_path=driver_path)
            # browser = webdriver.Chrome(chrome_options=chrome_options,executable_path=self.path+"./chromedriver.exe")
            self.browser.delete_all_cookies()
            self.browser.set_page_load_timeout(self.timeout) 
            return self.browser
        except Exception as e:
            print("err getBrowser")
            print(e)
            return None

    def getBrowser(self):
        return self.browser

    def setTimeOut(self,timeout):
        self.timeout=timeout
        self.browser.set_page_load_timeout(self.timeout) 
    
    def cleanLoginInfo(self):
        self.browser.delete_all_cookies()
