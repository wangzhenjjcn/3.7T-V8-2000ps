# M3-2019-Crawler

------


## 2019-04款
### 基本参数
> * 厂商：[Myazure](https://www.myazure.org/)
> * 级别：中级爬虫
> * 能源类型：纯电动
> * 上市时间：2019.9
> * 最大功率：64*4线程，10兆字节/秒
> * 代码结构：单线程单路管道
> * 0-100页读取速度：33.72秒
> * 初级架构：单线程单路管道

### 核心参数
> * 内核：Chrome
> * 版本：74.0.3729.169（正式版本） （64 位）
> * 交互模式：Http+Https+Socket4/5
> * 驱动模式：ChromeDriver
> * 模式：双模式（包含隐私模式）

### 发动机信息
Python （计算机程序设计语言）
#### Python 
- [ ] 不支持 PY2.x
- [ ] 不支持 Win7Sp1以下系统
- [x] 支持 PY3.0
- [x] 支持 Win10/Win7/Win8/WinServer2008 2012 2016 2019/OSX10.10+/Ubuntu16.04+
- [x] 支持Chrome内核 2.0-2.9/70.0.35*/71.0.35*/72.0.3636/73.0.3683/74.0.3729.6/75.0.3770

#### Require
- [x] os,time,re,json
- [x] requests
- [x] lxml
- [x] bs4
- [x] selenium
- [x] pytesseract

```python
#!/usr/bin/env python
#/usr/bin/python3
#!#/usr/bin/python3
#-*- coding:utf-8 -*-
# author : wangzhen <wangzhenjjcn@gmail.com> since 2019-03-15
import http.cookiejar as cookielib
import json
import os
import re
import sys
import time
import lxml
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import config
```






```gantt
    title 项目开发流程
    section 项目确定
        需求分析       :a1, 2019-06-2, 15d
        可行性报告     :after a1, 5d
        概念验证       : 5d
    section 项目实施
        概要设计      :2019-07-01  , 7d
        详细设计      :2019-07-08, 10d
        编码          :2019-06-11, 35d
        测试          :2019-07-22, 5d
    section 发布验收
        发布: 2d
        验收: 3d
```
 