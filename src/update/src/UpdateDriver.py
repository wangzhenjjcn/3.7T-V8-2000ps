#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys,re,time,urllib,lxml,time,requests,zipfile
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
try:
    from tkinter import *
except ImportError:  #Python 2.x
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    from tkMessageBox import *
else:  #Python 3.x
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *



class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('驱动更新程序-WangZHen<wangzhenjjcn@gmail.com>V1.0')
        self.master.geometry('303x246')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('driverframe.TLabelframe',font=('宋体',9))
        self.driverframe = LabelFrame(self.top, text='驱动更新', style='driverframe.TLabelframe')
        self.driverframe.place(relx=0.079, rely=0.033, relwidth=0.822, relheight=0.947)

        self.style.configure('ExitBtn.TButton',font=('宋体',9))
        self.ExitBtn = Button(self.driverframe, text='关闭', command=self.ExitBtn_Cmd, style='ExitBtn.TButton')
        self.ExitBtn.place(relx=0.514, rely=0.721, relwidth=0.39, relheight=0.142)

        self.ProcessBarVar = StringVar(value='')
        self.ProcessBar = Progressbar(self.driverframe, orient='horizontal', maximum=100, variable=self.ProcessBarVar)
        self.ProcessBar.place(relx=0.096, rely=0.584, relwidth=0.807, relheight=0.073)

        self.style.configure('UpdateBtn.TButton',font=('宋体',9))
        self.UpdateBtn = Button(self.driverframe, text='初始化本地驱动', command=self.UpdateBtn_Cmd, style='UpdateBtn.TButton')
        self.UpdateBtn.place(relx=0.096, rely=0.721, relwidth=0.39, relheight=0.142)

        self.style.configure('ChromeVersionLable.TLabel',anchor='w', font=('宋体',9))
        self.ChromeVersionLable = Label(self.driverframe, text='浏览器版本：', style='ChromeVersionLable.TLabel')
        self.ChromeVersionLable.place(relx=0.096, rely=0.412, relwidth=0.293, relheight=0.073)

        self.style.configure('ChromeVersion.TLabel',anchor='w', font=('宋体',9))
        self.ChromeVersion = Label(self.driverframe, text='Unknown', style='ChromeVersion.TLabel')
        self.ChromeVersion.place(relx=0.45, rely=0.412, relwidth=0.486, relheight=0.073)

        self.style.configure('LastVersion.TLabel',anchor='w', font=('宋体',9))
        self.LastVersion = Label(self.driverframe, text='Unknown', style='LastVersion.TLabel')
        self.LastVersion.place(relx=0.45, rely=0.275, relwidth=0.486, relheight=0.073)

        self.style.configure('CurrentVersion.TLabel',anchor='w', font=('宋体',9))
        self.CurrentVersion = Label(self.driverframe, text='Unknown', style='CurrentVersion.TLabel')
        self.CurrentVersion.place(relx=0.45, rely=0.137, relwidth=0.486, relheight=0.073)

        self.style.configure('LastVersionLable.TLabel',anchor='w', font=('宋体',9))
        self.LastVersionLable = Label(self.driverframe, text='最新版本：', style='LastVersionLable.TLabel')
        self.LastVersionLable.place(relx=0.096, rely=0.275, relwidth=0.293, relheight=0.073)

        self.style.configure('CurrentVersionLable.TLabel',anchor='w', font=('宋体',9))
        self.CurrentVersionLable = Label(self.driverframe, text='当前版本：', style='CurrentVersionLable.TLabel')
        self.CurrentVersionLable.place(relx=0.096, rely=0.137, relwidth=0.325, relheight=0.073)

class Application(Application_ui):
    def __init__(self, master=None):
        Application_ui.__init__(self, master)
        self.driver=None
        self.defaultVersion="76.0.3809.12"
        self.sysDir=os.path.dirname(os.path.realpath(sys.argv[0]))
        self.tmpDir=os.path.dirname(os.path.realpath(sys.argv[0]))+"\\tmp"
        self.confFile=os.path.dirname(os.path.realpath(sys.argv[0]))+"\\config.ini"
        self.driverFile=os.path.dirname(os.path.realpath(sys.argv[0]))+"\\driver.exe"
        self.dlDriverFile=self.tmpDir+"\\driver.exe"
        self.errLog=None
        self.version=None #current driver version
        self.dversion=None # download driver version
        self.cversion=None # google version
        self.lversion=None # local file driver version
        self.init_data()
        
    def init_data(self,event=None):
        if not os.path.exists(self.tmpDir):
            print("tmp missing creat...")
            os.makedirs(self.tmpDir) 
            print("tmp missing created!")
            print("tmp inited!")
        if not os.path.exists(self.tmpDir+'\\cache'):
            print("cache missing creat...")
            os.makedirs(self.tmpDir+'\\cache') 
            print("cache missing created!")
            print("tmp cache inited!")
        if not os.path.exists(self.confFile):
            print("Conf Missing!")
            with open(self.confFile, 'w+', encoding='utf_8') as f:
                print("Init Conf...")
                f.flush()
                f.close()
            print("Conf inited!")
            print("Files inited!")
        if not os.path.exists(self.driverFile):
            print("driverFile Missing!")
        else:
            print("driverFile exist!")
            self.version=self.checkLocalDriver()
            print("version is : "+str(self.version))
            if self.version=="Unknown":
                pass
            else:
                self.UpdateBtn['text']="检查并更新驱动"
                pass
            pass
        print("tmp cache Conf Files inited!... ")
        pass

    def ExitBtn_Cmd(self, event=None):
        try: top.destroy()
        except: pass
        pass

    def UpdateBtn_Cmd(self, event=None):

        self.downloadLastRunningVsersion()
        if not os.path.exists(self.driverFile):
            print("driverFile Missing!")
        else:
            print("driverFile exist!")

        if self.UpdateBtn['text']=="更新不匹配驱动":
            versionerr=str(self.lversion).split(".")[0]
            if versionerr == '70':
                    self.downloadDriver("71.0.3578.80")
            elif versionerr == '71':
                self.downloadDriver("72.0.3626.7")
            elif versionerr == '72':
                self.downloadDriver("73.0.3683.68")
            elif versionerr == '73':
                self.downloadDriver("74.0.3729.6")
            elif versionerr == '74':
                self.downloadDriver("75.0.3770.90")
            elif versionerr == '75':
                self.downloadDriver("76.0.3809.68")
            elif versionerr == '76':
                self.downloadDriver("77.0.3865.40")
            elif versionerr == '77':
                self.downloadDriver("78.0.3904.70")
            elif versionerr == '78':
                self.downloadDriver("79.0.3945.36")
            elif versionerr == '79':
                self.downloadDriver("80.0.3987.16")
            elif versionerr == '80':
                self.downloadDriver("81.0.4044.69")
            elif versionerr == '81':
                self.downloadDriver("83.0.4103.14")
            elif versionerr == '82':
                self.downloadDriver("83.0.4103.39")
            elif versionerr == '83':
                self.downloadDriver("83.0.4103.39")

        if self.UpdateBtn['text']=="更新目标驱动":
            self.checkLastDriver()

        if self.UpdateBtn['text']=="更新驱动完成":
            return

 
        pass

    def checkLocalDriver(self,event=None):
        if os.path.exists(self.driverFile):
            localVersion=self.checkDriverVersion(self.driverFile)
            self.version=localVersion
            self.CurrentVersion['text']=localVersion
            return localVersion
        else:
            self.CurrentVersion['text']="Unknown"
            return "Unknown"
        pass
        
    def checkChromeVersion(self,event=None):
        print("Checking local chrome version")
        try:
            chrome_options = webdriver.ChromeOptions()
            user_data_dir=self.tmpDir+"\\"+str(time.time()).replace(".","")+"\\"
            print("set user dir:"+user_data_dir)
            print("current driver file:"+self.driverFile)
            print("tmp:"+self.tmpDir)
            chrome_options.add_argument('--user-data-dir='+user_data_dir)
            chrome_options.add_argument('–disk-cache-dir='+self.tmpDir+"\\cache")
            chrome_options.add_argument('--disable-extensions')
            chrome_options.add_argument('--profile-directory=Default')
            chrome_options.add_argument("--incognito")
            chrome_options.add_argument("--disable-plugins-discovery")
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("-–process-per-tab")
            chrome_options.add_argument('--enable-javascript')
            chrome_options.add_argument('--log-level=3')
            chrome_options.add_argument('--disable-popup-blocking')
            chrome_options.add_argument('--remote-debugging-port=9222')
            chrome_options.add_argument("--proxy-server=127.0.0.1:1080")
            chrome_options.add_argument("--allow-file-access-from-files")
            chrome_options.add_argument("--disable-web-security")
            # chrome_options.add_argument('--headless')
            # chrome_options.add_argument('--disable-gpu')
            if "Unknown" in str(self.version):
                print("驱动错误，停止启动！")
                return "Unknown"
            print("驱动正常，尝试启动Chrome...")
            browser_ = webdriver.Chrome(chrome_options=chrome_options,executable_path=self.driverFile)
            browser_.set_page_load_timeout(3000) 
            try:
                browser_.get("chrome://version/")
            except:
                browser_.execute_script('window.stop()') 
                return "Unknown"   
            version_page=BeautifulSoup(browser_.page_source, "lxml")
            version_td=version_page.find("td",id="version")
            chrome_version=version_td.find("span").text
            print("启动成功 当前 chrome version:"+chrome_version)
            self.ChromeVersion['text']=chrome_version
            self.cversion=chrome_version
            try:
                print("driver running,exiting ...")
                browser_.quit()
                print('driver closed now!')
                pass
            except Exception as e:
                print("in Close driver!")
                print(e)
                try:
                    with open(self.tmpDir+"\\err.log", 'w+', encoding='utf_8') as f:
                        f.write(str(e)+"\n")
                        f.flush()
                        f.close()
 
                except Exception as e:
                    print(str(e))
 
                    pass
            self.UpdateBtn['text']="更新目标驱动"
            return chrome_version
        except Exception as e:
            if "This version of ChromeDriver only supports" in str(e):
                print("chrome driver version not fit")
                self.UpdateBtn['text']="更新不匹配驱动"
                print("version:"+str(self.version))
            try:
                with open(self.tmpDir+"\\err.log", 'w+', encoding='utf_8') as f:
                    f.write(str(e)+"\n")
                    f.flush()
                    f.close()
 
            except Exception as e:
                print(str(e))
 
                pass
        return "Unknown"

    def checkDriverVersion(self,filename,event=None):
        if os.path.exists(filename):
            try:
                versionline=""
                result = os.popen(str(filename) + "  -version")  
                resaulttxt= result.read()
                result.close()
                for line in resaulttxt.splitlines():
                    if "ChromeDriver" in line:
                        versionline=line
                version=".".join(versionline.split("ChromeDriver")[1].split("(")[0].replace(" ","").split("."))
                result.close()
                return version
            except Exception as e:
                print("CheckErr!")
                print(e)
            pass
        else:
            print("file not exist")
            return "Unknown"
        pass

    def downloadDriver(self,driverVersion,event=None):
        try:
            print("try to downloiad driver @ "+driverVersion)
            if  os.path.exists(self.tmpDir+"\\driver_"+driverVersion+".zip"):	
                os.remove(self.tmpDir+"\\driver_"+driverVersion+".zip")
                pass
            url="http://npm.taobao.org/mirrors/chromedriver/"+driverVersion+"/chromedriver_win32.zip"
            headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
                        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Encoding': 'gzip, deflate',
                        'Upgrade-Insecure-Requests':'1'}
            response = requests.get(url, headers=headers)
            print("try to downloiad driver ["+driverVersion+"] with code:"+str(response.status_code))
            with open(self.tmpDir+"\\driver_"+driverVersion+".zip", 'wb') as f:
                f.write(response.content)
                f.flush()
                f.close()
            print("try to unzip driver=="+driverVersion)
            self.ProcessBarVar.set(85)
            if self.driver!=None: 
                try:
                    print("driver running,exiting ...")
                    self.driver.quit()
                    print('driver closed now!')
                    pass
                except Exception as e:
                    print("in Close driver!")
                    print(e)
                    try:
                        with open(self.tmpDir+"\\err.log", 'w+', encoding='utf_8') as f:
                            f.write(str(e)+"\n")
                            f.flush()
                            f.close()
                    except Exception as e:
                        print("in finish logfile!")
                        print(e)
                        pass
                    return
            try:
                zf = zipfile.ZipFile(self.tmpDir+"\\driver_"+driverVersion+".zip")
                if  os.path.exists(self.tmpDir+"\\chromedriver.exe"):	
                    print("=remove current chromedriver exe file")
                    os.remove(self.tmpDir+"\\chromedriver.exe")
                    print("=removed current chromedriver exe file")
                for file in zf.namelist():
                    zf.extract(file,self.tmpDir)
                    print("==unziped driver file:"+file)
                zf.close()
                self.ProcessBarVar.set(89)
                
                if  os.path.exists(self.sysDir+"\\driver.exe"):	
                    
                    os.remove(self.sysDir+"\\driver.exe")
                    print("=remove origin file")
                else:
                    print("=current version to be copy:"+str(driverVersion))
                    pass

                if  os.path.exists(self.tmpDir+"\\chromedriver.exe"):	
                    print("==解压成功")
                else:
                    print("==校验失败")
                    return

                with open(self.tmpDir+"\\chromedriver.exe", 'rb') as f:
                    with open(self.sysDir+"\\driver.exe", 'wb') as t:
                        t.write(f.read())
                        t.flush()
                    t.close()
                f.close()
                self.version=driverVersion
                self.CurrentVersion['text']=driverVersion
                if t.closed and f.closed:
                    print("关闭正常")
                    if  os.path.exists(self.tmpDir+"\\chromedriver.exe"):	
                        print("删除临时文件")
                        try:
                            os.remove(self.tmpDir+"\\chromedriver.exe")
                        except  Exception as e:
                            print("删除临时文件失败")
                            print(e)
                            pass
                else:
                    if not t.closed:
                        print("err close:"+self.sysDir+"\\driver.exe")
                    if not f.closed:
                        print("err close:"+self.tmpDir+"\\chromedriver.exe")
                print("驱动下载成功")
                self.ProcessBarVar.set(100)
                pass
            except RuntimeError as e:
                try:
                    zf.close()
                    with open(self.tmpDir+"\\err.log", 'w+', encoding='utf_8') as f:
                        f.write(str(e)+"\n")
                        f.flush()
                        f.close()
                except Exception as e:
                    print("in finish logfile!")
                    print(e)
                    pass
                print(e)
        except Exception as e:
            print(e)
            try:
                with open(self.tmpDir+"\\err.log", 'w+', encoding='utf_8') as f:
                    f.write(str(e)+"\n")
                    f.flush()
                    f.close()
            except Exception as e:
                print(e)
                pass
            print('驱动下载失败')
        pass

        pass
    
    def downloadLastRunningVsersion(self,event=None):
        download_version=""
        self.init_data()
        self.version=self.checkLocalDriver()
        if "Unknown" in str(self.version) or  str(self.version)=="":
            download_version="71.0.3578.80"
            self.downloadDriver(download_version)
            # self.version=download_version
            if "Unknown" in str(self.version) or  str(self.version)=="":
                return
            pass
        self.checkChromeVersion()
        cvs=self.cversion.split('.')
        dcvs=[]
        for i in range(0,len(cvs)-1):
            dcvs.append(cvs[i])
        dcvss=".".join(dcvs)
        print("bigV:"+dcvss)
        try:
            url="http://npm.taobao.org/mirrors/chromedriver/"
            headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
                        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Encoding': 'gzip, deflate',
                        'Upgrade-Insecure-Requests':'1'}
            response = requests.get(url, headers=headers)
            print("try to check last version driver with code:"+str(response.status_code))
            if str(response.status_code)!="200":
                self.LastVersion['text']="err检测失败！"
                return
            bsObj = BeautifulSoup(response.text, features="lxml")
            astag=bsObj.find(name="div",attrs={"class":"container"}).findAll(name="a",attrs={"href": True})
            lastv=""
            for a in astag:
                if "." in a.text and "_" not in a.text and "/" in a.text and "http" not in a.text and ".." not in a.text:
                    va=str(a.text).replace("/","")
                    if dcvss in a.text:
                        lastv=va
            print(lastv)
            self.LastVersion["text"]=lastv
            self.lversion=lastv
            self.ProcessBarVar.set(50)
            self.downloadDriver(self.lversion)
            self.UpdateBtn['text']="更新驱动完成"
            pass
        except Exception as e:
            print("err!")
            print(e)
            try:
                with open(self.tmpDir+"\\err.log", 'w+', encoding='utf_8') as f:
                    f.write(str(e)+"\n")
                    f.flush()
                    f.close()
            except Exception as e:
                print(e)
                pass


        pass

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    try: top.destroy()
    except: pass
