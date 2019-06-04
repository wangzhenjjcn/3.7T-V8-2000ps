#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import configparser


class Config:
    def __init__(self, path):
        self.path = path
        self.cf = configparser.ConfigParser()
        self.cf.read(self.path,encoding="utf-8")

    def get(self, field, key):
        result = ""
        try:
            result = self.cf.get(field, key)
        except:
            result = ""
        return result

    def set(self, filed, key, value):
        try:
            self.cf.set(field, key, value)
            self.cf.write(open(self.path, 'w',encoding="utf-8"))
        except:
            return False
        return True


def read_config(config_file_path, field, key):
    cf = configparser.ConfigParser()
    try:
        cf.read(config_file_path,encoding="utf-8")
        if field in cf:
            result = cf[field][key]
        else:
            return ''
    except configparser.Error as e:
        print("eeeeeeeeeeeeeeeeeeeer")
        print(e)
        return ''
    return result



def read_configs(config_file_path, field):
    cf = configparser.ConfigParser()
    try:
        cf.read(config_file_path,encoding="utf-8")
        if field in cf:
            result = cf[field]
        else:
            return ''
    except configparser.Error as e:
        return ''
    return result

def write_config(config_file_path, field, key, value):
    cf = configparser.ConfigParser()
    try:
        cf.read(config_file_path,encoding="utf-8")
        if field not in cf:
            cf.add_section(field)
        cf[field][key] = value
        cf.write(open(config_file_path, 'w',encoding="utf-8"))
    except configparser.Error as e:
        return False
    return True


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