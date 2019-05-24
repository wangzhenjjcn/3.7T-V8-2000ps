#!/usr/bin/env python
#/usr/bin/python3
#!#/usr/bin/python3
#-*- coding:utf-8 -*-
# web crawler for artstation
# author : wangzhen <wangzhenjjcn@gmail.com> since 2019-03-15
import http.cookiejar as cookielib
import json
import logging
import math
import os
import random
import re
import sys
import threading
import time
from concurrent import futures
# import argparse
# import urllib.request
# import urllib.error
# import unicodedata
# from concurrent.futures import ThreadPoolExecutor
# from functools import partial
from multiprocessing import cpu_count
from urllib.parse import urlparse
import lxml
import js2py
import pafy
import requests
from bs4 import BeautifulSoup




class Web:

    def log(self, message):

        print(message)

    def __init__(self,log_print=None):
        if log_print:
            global print
            # print = log_print
        self.session = requests.session()
        
        self.session.cookies = None

        self.defaultHeader = {
            'upgrade-insecure-requests': "1",
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
            'dnt': "1",
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            'accept-encoding': "gzip, deflate",
            'accept-language': "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6",
            'cache-control': "no-cache"}

        self.ajaxheaders = {
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        'dnt': "1",
        'accept-encoding': "gzip, deflate, br",
        'x-requested-with': "XMLHttpRequest",
        'accept-language': "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6",
        'cache-control': "no-cache",
        'accept': "application/json, text/plain, */*; q=0.01",}

        self.defaultDedirectory=None
        
    def get(self,url):
        print("getting:"+url)
        if self.defaultDedirectory ==None:
            print("dri err")
            self.defaultDedirectory="D:\\aaa"
        print(self.defaultDedirectory)
        return  self.getWithHeaderWithCookiesToDirectory(url,self.defaultDedirectory,self.defaultHeader)

    def getWithHeader(self,url,header):
        return  self.getWithHeaderWithCookiesToDirectory(url,self.defaultDedirectory,header)


    def getWithHeaderWithCookiesToDirectory(self,url,directory,header):
        # print("directory:"+directory)
        sessionfile_full_path = os.path.join(directory, self.getURI(url)+"_cookie.txt")
        if os.path.exists(sessionfile_full_path):
            pass
            # print('[Exist][cookie][{}]'.format(sessionfile_full_path))
        else:
            # print("creat Cookie File:"+sessionfile_full_path)
            os.makedirs(directory, exist_ok=True)
        self.session.cookies = cookielib.LWPCookieJar(filename=sessionfile_full_path)
         
        # print("Open:"+url)
        try:
            responseRes=self.session.get(url,  headers = header ) 
            # print(responseRes)
            pass
        except Exception as e:
            print(e)
            return None
        finally:
            self.session.cookies.save()
        if not responseRes.ok:
            print("ERR CODE:"+str(responseRes.status_code))
            return self.getWithHeaderWithCookiesToDirectory(url,directory,header) 
        return responseRes


    def post(self,url,directory,header,data):
        sessionfile_full_path = os.path.join(directory, self.getURI(url)+"_cookie.txt")
        if os.path.exists(self.defaultDedirectory):
            print('[Exist][cookie][{}]'.format(self.defaultDedirectory))
        else:
            os.makedirs(self.defaultDedirectory, exist_ok=True)
        self.session.cookies = cookielib.LWPCookieJar(filename=sessionfile_full_path)
    
        print("Open:"+url)
        responseRes = self.session.post(url, data = data, headers = header  )
        self.session.cookies.save()
        if not responseRes.ok:
            print("ERR CODE:"+str(responseRes.status_code))
            return responseRes
        return responseRes


    def getURI(self,url):
        if "http" not in url:
            if "." not in url:
                return ""
            else:
                if "/" not in url:
                    return url
                else:
                    strs=url.split('/')
                    return strs[0]
        else:
            strs=url.split('://')
            return strs[1].split('/')[0]
        return ""


    def downloadJavascriptFiles(self,url,directory,header):
        # print("start read:"+url)
        _dir=directory+"/"+self.getURI(url)+"/"
        data=self.getWithHeaderWithCookiesToDirectory(url,_dir,header)
        text=data.text
        srcs=re.findall(r'<script.*?src="(.*?)"',text)
        print(srcs)
        datas=[]
        names=[]
        for src in srcs:
            link=src.replace('//','/').replace("http:/","http://").replace("https:/","https://")
            if link.startswith("//"):
                link=src.replace('//','http://')
                datas.append(link)
                name=src.split('/')
                names.append(name[len(name)-1])
                self.downloadfile(link,_dir,name[len(name)-1])
                continue
            if "http" not in link:
                link="http://"+self.getURI(url)+"/"+src
                datas.append(link)
                name=src.split('/')
                names.append(name[len(name)-1])
                self.downloadfile(link,_dir,name[len(name)-1])
                continue
            if ".js" in link:
                datas.append(link)
                name=src.split('/')
                names.append(name[len(name)-1])
                self.downloadfile(link,_dir,name[len(name)-1])
        # print(text)
        print(names)
        return text


    def checkFlooder(self, directory):
        # print("checking {} ...".format(str(directory).split()))
        if os.path.exists(str(directory)):
            return
            # print('[Exist][directory][{}]'.format(str(directory)))
        else:
            # print("creat directory :"+str(directory))
            os.makedirs(str(directory), exist_ok=True)

    def downloadfile(self,url,directory,filename):
        print("downloading URL:"+url+" as filename: "+filename +" into "+directory)
        _filename = (directory+'/'+re.sub(r'[\/:*?"<>|]','-',filename)).replace('//','/')
        try:
            response = requests.get(url, headers=self.defaultHeader)
            
            with open(_filename.encode('UTF-8').decode("UTF-8"), 'wb') as f:
                f.write(response.content)
                f.flush()
                f.close()
                return 1
        except Exception as e:
            print(e)
            return 0
        finally:
            f.close()
        return 0

    def processJavascriptFuction(self,html,sripts):
        print("transfer javasripts with " + html)

def main():
    web=Web()
    url=input("URL:")
    js=web.downloadJavascriptFiles(url,"D:/sss/",web.defaultHeader)

    
 
if __name__ == '__main__':
    main()

# \ 做为转意，即通常在"\"后面的字符不按原来意义解释，如/b/匹配字符"b"，当b前面加了反斜杆后/\b/，转意为匹配一个单词的边界。 
# -或- 
# 对正则表达式功能字符的还原，如"*"匹配它前面元字符0次或多次，/a*/将匹配a,aa,aaa，加了"\"后，/a\*/将只匹配"a*"。 

# ^ 匹配一个输入或一行的开头，/^a/匹配"an A"，而不匹配"An a" 
# $ 匹配一个输入或一行的结尾，/a$/匹配"An a"，而不匹配"an A" 
# * 匹配前面元字符0次或多次，/ba*/将匹配b,ba,baa,baaa 
# + 匹配前面元字符1次或多次，/ba*/将匹配ba,baa,baaa 
# ? 匹配前面元字符0次或1次，/ba*/将匹配b,ba 
# (x) 匹配x保存x在名为$1...$9的变量中 
# x|y 匹配x或y 
# {n} 精确匹配n次 
# {n,} 匹配n次以上 
# {n,m} 匹配n-m次 
# [xyz] 字符集(character set)，匹配这个集合中的任一一个字符(或元字符) 
# [^xyz] 不匹配这个集合中的任何一个字符 
# [\b] 匹配一个退格符 
# \b 匹配一个单词的边界 
# \B 匹配一个单词的非边界 
# \cX 这儿，X是一个控制符，/\cM/匹配Ctrl-M 
# \d 匹配一个字数字符，/\d/ = /[0-9]/ 
# \D 匹配一个非字数字符，/\D/ = /[^0-9]/ 
# \n 匹配一个换行符 
# \r 匹配一个回车符 
# \s 匹配一个空白字符，包括\n,\r,\f,\t,\v等 
# \S 匹配一个非空白字符，等于/[^\n\f\r\t\v]/ 
# \t 匹配一个制表符 
# \v 匹配一个重直制表符 
# \w 匹配一个可以组成单词的字符(alphanumeric，这是我的意译，含数字)，包括下划线，如[\w]匹配"$5.98"中的5，等于[a-zA-Z0-9] 
# \W 匹配一个不可以组成单词的字符，如[\W]匹配"$5.98"中的$，等于[^a-zA-Z0-9]。