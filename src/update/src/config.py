#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import os
import sys
import configparser


class Config:
    def __init__(self, path):
        self.path = path
        removeBom(self.path)
        self.cf = configparser.ConfigParser()
        self.cf.read(self.path,encoding='utf_8')

    def get(self, field, key):
        result = ''
        try:
            result = self.cf.get(field, key)
        except:
            result = ''
        return result

    def set(self, filed, key, value):
        try:
            self.cf.set(field, key, value)
            self.cf.write(open(self.path, 'w+',encoding='utf_8'))
        except:
            return False
        return True

def read_config(config_file_path, field, key):
    cf = configparser.ConfigParser()
    try:
        removeBom(config_file_path)
        cf.read(config_file_path,encoding='utf_8')
        if field in cf:
            result = cf[field][key]
        else:
            return ''
    except configparser.Error as e:
        print('eeeeeeeeeeeeeeeeeeeer')
        print(e)
        return ''
    return result
 

def read_configs(config_file_path, field):
    cf = configparser.ConfigParser()
    try:
        removeBom(config_file_path)
        cf.read(config_file_path,encoding='utf_8')
        if field in cf:
            result = cf[field]
        else:
            return []
    except configparser.Error as e:
        print(e)
        return ''
    return result

def write_config(config_file_path, field, key, value):
    cf = configparser.ConfigParser()
    try:
        removeBom(config_file_path)
        cf.read(config_file_path,encoding='utf_8')
        if field not in cf:
            cf.add_section(field)
        cf[field][key] = value
        cf.write(open(config_file_path, 'w+',encoding='utf_8'))
    except configparser.Error as e:
        print(e)
        return False
    return True

def removeBom(file):
      BOM = b'\xef\xbb\xbf'
      existBom = lambda s: True if s==BOM else False
     
      f = open(file, 'rb')
      if existBom( f.read(3) ):
          fbody = f.read()
          #f.close()
          with open(file, 'wb') as f:
              f.write(fbody)


def readConf(confName,path):
    if not os.path.exists(os.path.dirname(os.path.realpath(sys.argv[0]))+'\\config.ini'):
        print("配置文件不存在，创建新配置")
        with open(os.path.dirname(os.path.realpath(sys.argv[0]))+'\\config.ini', 'w+', encoding='utf_8') as f:
            print("初始化空配置文件")
            return ""
    path_=path
    if path==None or path=="":
        path_="通用设置"
    data=''
    try:
        data= read_config(os.path.dirname(os.path.realpath(sys.argv[0]))+'\\config.ini', path_, confName)
    except Exception as e:
        print(e)
        return ''
    return data

def getConf(name,initValue,path):
    if not os.path.exists(os.path.dirname(os.path.realpath(sys.argv[0]))+'\\config.ini'):
        print("配置文件不存在，创建新配置")
        with open(os.path.dirname(os.path.realpath(sys.argv[0]))+'\\config.ini', 'w+', encoding='utf_8') as f:
            print("初始化空配置文件")
            return ""
    path_=path
    if path==None or path=="":
        path_="通用设置"
    data=''
    try:
        data= read_config(os.path.dirname(os.path.realpath(sys.argv[0]))+'\\config.ini', path_, name)

    except Exception as e:
        print(e)
        value= ''
    value= data

    if value==None or value=="":
        tmp_=str(initValue)+""
        if tmp_==None or tmp_=="":
            return None
        writeConf(name,tmp_,path)
        return initValue
    else:
        return value

 
def writeConf(confName,confValue,path):
    path_=path
    if path==None:
        path_="通用设置"
    write_config(os.path.dirname(os.path.realpath(sys.argv[0]))+'\\config.ini', path_, confName,confValue)
    return confValue


if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit(1)

    config_file_path = sys.argv[1]
    field = sys.argv[2]
    key = sys.argv[3]
    if len(sys.argv) == 4:
        print(read_config(config_file_path, field, key))
    else:
        value = sys.argv[4]
        write_config(config_file_path, field, key, value)
