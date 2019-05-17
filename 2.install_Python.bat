@echo off
:install
ECHO Start to install python 3
start /wait ./tmp/python-3.7.2.exe 
ECHO install python successfully......
ping 127.1 >nul
:run
echo start to install pip....... 
start /wait  python ./tmp/get-pip.py  
start /wait pip install pyinstaller -i https://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com
echo install pip successfully....... 
ping 127.1 >nul
echo start install requirements...
start /wait pip install -r requirements
pause;