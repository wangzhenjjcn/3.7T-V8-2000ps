#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys,re,time,urllib,lxml,threading,time,requests,base64,json,ast

try:
    from tkinter import *
except ImportError:  #Python 2.x
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()



import config

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('虎牙机器人(切克闹)主程序-版本1.0')
        self.master.geometry('1699x804')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('Main.TLabelframe',font=('宋体',9))
        self.Main = LabelFrame(self.top, text='程序设置', style='Main.TLabelframe')
        self.Main.place(relx=0., rely=0., relwidth=0.999, relheight=0.996)

        self.style.configure('CustomeScheduledSettingsFrame.TLabelframe',font=('宋体',9))
        self.CustomeScheduledSettingsFrame = LabelFrame(self.Main, text='定时发言', style='CustomeScheduledSettingsFrame.TLabelframe')
        self.CustomeScheduledSettingsFrame.place(relx=0.797, rely=0.729, relwidth=0.194, relheight=0.211)

        self.style.configure('CustomeScheduledSettingsSaveCommand.TButton',font=('宋体',9))
        self.CustomeScheduledSettingsSaveCommand = Button(self.CustomeScheduledSettingsFrame, text='保存/应用', command=self.CustomeScheduledSettingsSaveCommand_Cmd, style='CustomeScheduledSettingsSaveCommand.TButton')
        self.CustomeScheduledSettingsSaveCommand.place(relx=0.705, rely=0.142, relwidth=0.222, relheight=0.148)

        self.ScheduledInfoTimeInputVar = StringVar(value='5')
        self.ScheduledInfoTimeInput = Entry(self.CustomeScheduledSettingsFrame, text='5', textvariable=self.ScheduledInfoTimeInputVar, font=('宋体',9))
        self.ScheduledInfoTimeInput.place(relx=0.657, rely=0.757, relwidth=0.271, relheight=0.107)

        self.ScheduledInfoInputVar = StringVar(value='')
        self.ScheduledInfoInput = Entry(self.CustomeScheduledSettingsFrame, textvariable=self.ScheduledInfoInputVar, font=('宋体',9))
        self.ScheduledInfoInput.place(relx=0.073, rely=0.331, relwidth=0.854, relheight=0.29)

        self.style.configure('ScheduledInfoTimeLable.TLabel',anchor='w', font=('宋体',9))
        self.ScheduledInfoTimeLable = Label(self.CustomeScheduledSettingsFrame, text='发言时间(每X分钟一次):', style='ScheduledInfoTimeLable.TLabel')
        self.ScheduledInfoTimeLable.place(relx=0.049, rely=0.757, relwidth=0.474, relheight=0.118)

        self.style.configure('ScheduledInfoLabel.TLabel',anchor='w', font=('宋体',9))
        self.ScheduledInfoLabel = Label(self.CustomeScheduledSettingsFrame, text='发言内容:', style='ScheduledInfoLabel.TLabel')
        self.ScheduledInfoLabel.place(relx=0.024, rely=0.142, relwidth=0.261, relheight=0.118)

        self.style.configure('WebInfoFrame.TLabelframe',font=('宋体',9))
        self.WebInfoFrame = LabelFrame(self.Main, text='房间信息', style='WebInfoFrame.TLabelframe')
        self.WebInfoFrame.place(relx=0.273, rely=0.07, relwidth=0.514, relheight=0.87)

        self.VIPListVar = StringVar(value='启动机器人后显示')
        self.VIPListFont = Font(font=('宋体',9))
        self.VIPList = Listbox(self.WebInfoFrame, listvariable=self.VIPListVar, font=self.VIPListFont)
        self.VIPList.place(relx=0.027, rely=0.092, relwidth=0.175, relheight=0.867)

        self.FansListVar = StringVar(value='启动机器人后显示')
        self.FansListFont = Font(font=('宋体',9))
        self.FansList = Listbox(self.WebInfoFrame, listvariable=self.FansListVar, font=self.FansListFont)
        self.FansList.place(relx=0.211, rely=0.092, relwidth=0.175, relheight=0.867)

        self.ChatsListVar = StringVar(value='启动机器人后显示')
        self.ChatsListFont = Font(font=('宋体',9))
        self.ChatsList = Listbox(self.WebInfoFrame, listvariable=self.ChatsListVar, font=self.ChatsListFont)
        self.ChatsList.place(relx=0.394, rely=0.092, relwidth=0.386, relheight=0.867)

        self.NicknameListVar = StringVar(value='空')
        self.NicknameListFont = Font(font=('宋体',9))
        self.NicknameList = Listbox(self.WebInfoFrame, listvariable=self.NicknameListVar, font=self.NicknameListFont)
        self.NicknameList.place(relx=0.788, rely=0.092, relwidth=0.175, relheight=0.385)

        self.CustomReplyListVar = StringVar(value='空')
        self.CustomReplyListFont = Font(font=('宋体',9))
        self.CustomReplyList = Listbox(self.WebInfoFrame, listvariable=self.CustomReplyListVar, font=self.CustomReplyListFont)
        self.CustomReplyList.place(relx=0.788, rely=0.574, relwidth=0.175, relheight=0.385)

        self.style.configure('WebVipsLable.TLabel',anchor='w', foreground='#000000', font=('宋体',9))
        self.WebVipsLable = Label(self.WebInfoFrame, text='贵宾席:', style='WebVipsLable.TLabel')
        self.WebVipsLable.place(relx=0.027, rely=0.046, relwidth=0.084, relheight=0.029)

        self.style.configure('WebFansLable.TLabel',anchor='w', foreground='#000000', font=('宋体',9))
        self.WebFansLable = Label(self.WebInfoFrame, text='粉丝席:', style='WebFansLable.TLabel')
        self.WebFansLable.place(relx=0.211, rely=0.046, relwidth=0.102, relheight=0.029)

        self.style.configure('WebChatsLable.TLabel',anchor='w', foreground='#000000', font=('宋体',9))
        self.WebChatsLable = Label(self.WebInfoFrame, text='公屏:', style='WebChatsLable.TLabel')
        self.WebChatsLable.place(relx=0.394, rely=0.046, relwidth=0.071, relheight=0.029)

        self.style.configure('NicknameLable.TLabel',anchor='w', font=('宋体',9))
        self.NicknameLable = Label(self.WebInfoFrame, text='自定义昵称:', style='NicknameLable.TLabel')
        self.NicknameLable.place(relx=0.788, rely=0.046, relwidth=0.12, relheight=0.029)

        self.style.configure('CustomReplyLabel.TLabel',anchor='w', font=('宋体',9))
        self.CustomReplyLabel = Label(self.WebInfoFrame, text='自定义回复:', style='CustomReplyLabel.TLabel')
        self.CustomReplyLabel.place(relx=0.788, rely=0.516, relwidth=0.12, relheight=0.04)

        self.style.configure('Frame2.TLabelframe',font=('宋体',9))
        self.Frame2 = LabelFrame(self.Main, text='机器人设置', style='Frame2.TLabelframe')
        self.Frame2.place(relx=0.005, rely=0.03, relwidth=0.17, relheight=0.91)

        self.ThanksOnTVGiftCheckVar = StringVar(value='0')
        self.style.configure('ThanksOnTVGiftCheck.TCheckbutton',font=('宋体',9))
        self.ThanksOnTVGiftCheck = Checkbutton(self.Frame2, text='答谢上电视礼物', variable=self.ThanksOnTVGiftCheckVar, style='ThanksOnTVGiftCheck.TCheckbutton')
        self.ThanksOnTVGiftCheck.place(relx=0.415, rely=0.219, relwidth=0.502, relheight=0.034)

        self.ThanksGiftMoreThanInputVar = StringVar(value='0')
        self.ThanksGiftMoreThanInput = Entry(self.Frame2, text='0', textvariable=self.ThanksGiftMoreThanInputVar, font=('宋体',9))
        self.ThanksGiftMoreThanInput.place(relx=0.581, rely=0.274, relwidth=0.17, relheight=0.025)

        self.ThanksGiftInfoFormartInputVar = StringVar(value='谢谢[心动]切克闹[送花]的1314个虎牙一号')
        self.ThanksGiftInfoFormartInput = Entry(self.Frame2, text='谢谢[心动]切克闹[送花]的1314个虎牙一号', textvariable=self.ThanksGiftInfoFormartInputVar, font=('宋体',9))
        self.ThanksGiftInfoFormartInput.place(relx=0.083, rely=0.955, relwidth=0.862, relheight=0.034)

        self.StartLotteryInfoFormartInputVar = StringVar(value='奖品:[心动]【奖品名称】[心动]走一波[心动]')
        self.StartLotteryInfoFormartInput = Entry(self.Frame2, text='奖品:[心动]【奖品名称】[心动]走一波[心动]', textvariable=self.StartLotteryInfoFormartInputVar, font=('宋体',9))
        self.StartLotteryInfoFormartInput.place(relx=0.083, rely=0.845, relwidth=0.862, relheight=0.034)

        self.ThanksShareInfoFormartInputVar = StringVar(value='谢谢[送花]切克闹[送花]分享直播间')
        self.ThanksShareInfoFormartInput = Entry(self.Frame2, text='谢谢[送花]切克闹[送花]分享直播间', textvariable=self.ThanksShareInfoFormartInputVar, font=('宋体',9))
        self.ThanksShareInfoFormartInput.place(relx=0.083, rely=0.735, relwidth=0.862, relheight=0.034)

        self.WelcomeVipsInfoFormartInputVar = StringVar(value='欢迎[送花]切克闹[送花]')
        self.WelcomeVipsInfoFormartInput = Entry(self.Frame2, text='欢迎[送花]切克闹[送花]', textvariable=self.WelcomeVipsInfoFormartInputVar, font=('宋体',9))
        self.WelcomeVipsInfoFormartInput.place(relx=0.083, rely=0.626, relwidth=0.862, relheight=0.034)

        self.RomIdInputVar = StringVar(value='点击输入房间号')
        self.RomIdInput = Entry(self.Frame2, text='点击输入房间号', textvariable=self.RomIdInputVar, font=('宋体',9))
        self.RomIdInput.place(relx=0.415, rely=0.033, relwidth=0.502, relheight=0.034)

        self.ShowWebViewerCheckVar = StringVar(value='0')
        self.style.configure('ShowWebViewerCheck.TCheckbutton',font=('宋体',9))
        self.ShowWebViewerCheck = Checkbutton(self.Frame2, text='显示直播画面(需要重启机器人)', variable=self.ShowWebViewerCheckVar, style='ShowWebViewerCheck.TCheckbutton')
        self.ShowWebViewerCheck.place(relx=0.028, rely=0.527, relwidth=0.668, relheight=0.034)

        self.ThanksGiftCheckVar = StringVar(value='0')
        self.style.configure('ThanksGiftCheck.TCheckbutton',font=('宋体',9))
        self.ThanksGiftCheck = Checkbutton(self.Frame2, text='答谢礼物', variable=self.ThanksGiftCheckVar, style='ThanksGiftCheck.TCheckbutton')
        self.ThanksGiftCheck.place(relx=0.028, rely=0.263, relwidth=0.363, relheight=0.034)

        self.ThanksShareCheckVar = StringVar(value='0')
        self.style.configure('ThanksShareCheck.TCheckbutton',font=('宋体',9))
        self.ThanksShareCheck = Checkbutton(self.Frame2, text='答谢分享', variable=self.ThanksShareCheckVar, style='ThanksShareCheck.TCheckbutton')
        self.ThanksShareCheck.place(relx=0.028, rely=0.219, relwidth=0.363, relheight=0.034)

        self.WelcomeVipsCheckVar = StringVar(value='0')
        self.style.configure('WelcomeVipsCheck.TCheckbutton',font=('宋体',9))
        self.WelcomeVipsCheck = Checkbutton(self.Frame2, text='欢迎贵宾', variable=self.WelcomeVipsCheckVar, style='WelcomeVipsCheck.TCheckbutton')
        self.WelcomeVipsCheck.place(relx=0.028, rely=0.307, relwidth=0.253, relheight=0.034)

        self.WelcomeFansCheckVar = StringVar(value='0')
        self.style.configure('WelcomeFansCheck.TCheckbutton',font=('宋体',9))
        self.WelcomeFansCheck = Checkbutton(self.Frame2, text='欢迎粉丝', variable=self.WelcomeFansCheckVar, style='WelcomeFansCheck.TCheckbutton')
        self.WelcomeFansCheck.place(relx=0.028, rely=0.417, relwidth=0.253, relheight=0.034)

        self.VipsLevelOneCheckVar = StringVar(value='0')
        self.style.configure('VipsLevelOneCheck.TCheckbutton',font=('宋体',9))
        self.VipsLevelOneCheck = Checkbutton(self.Frame2, text='剑士', variable=self.VipsLevelOneCheckVar, style='VipsLevelOneCheck.TCheckbutton')
        self.VipsLevelOneCheck.place(relx=0.332, rely=0.318, relwidth=0.17, relheight=0.023)

        self.VipsLevelTwoCheckVar = StringVar(value='0')
        self.style.configure('VipsLevelTwoCheck.TCheckbutton',font=('宋体',9))
        self.VipsLevelTwoCheck = Checkbutton(self.Frame2, text='骑士', variable=self.VipsLevelTwoCheckVar, style='VipsLevelTwoCheck.TCheckbutton')
        self.VipsLevelTwoCheck.place(relx=0.637, rely=0.318, relwidth=0.17, relheight=0.023)

        self.VipsLevelThreeCheckVar = StringVar(value='0')
        self.style.configure('VipsLevelThreeCheck.TCheckbutton',font=('宋体',9))
        self.VipsLevelThreeCheck = Checkbutton(self.Frame2, text='领主', variable=self.VipsLevelThreeCheckVar, style='VipsLevelThreeCheck.TCheckbutton')
        self.VipsLevelThreeCheck.place(relx=0.332, rely=0.34, relwidth=0.17, relheight=0.023)

        self.VipsLevelFourCheckVar = StringVar(value='0')
        self.style.configure('VipsLevelFourCheck.TCheckbutton',font=('宋体',9))
        self.VipsLevelFourCheck = Checkbutton(self.Frame2, text='公爵', variable=self.VipsLevelFourCheckVar, style='VipsLevelFourCheck.TCheckbutton')
        self.VipsLevelFourCheck.place(relx=0.637, rely=0.34, relwidth=0.17, relheight=0.023)

        self.VipsLevelFiveCheckVar = StringVar(value='0')
        self.style.configure('VipsLevelFiveCheck.TCheckbutton',font=('宋体',9))
        self.VipsLevelFiveCheck = Checkbutton(self.Frame2, text='君王', variable=self.VipsLevelFiveCheckVar, style='VipsLevelFiveCheck.TCheckbutton')
        self.VipsLevelFiveCheck.place(relx=0.332, rely=0.362, relwidth=0.17, relheight=0.023)

        self.VipsLevelSixCheckVar = StringVar(value='0')
        self.style.configure('VipsLevelSixCheck.TCheckbutton',font=('宋体',9))
        self.VipsLevelSixCheck = Checkbutton(self.Frame2, text='帝皇', variable=self.VipsLevelSixCheckVar, style='VipsLevelSixCheck.TCheckbutton')
        self.VipsLevelSixCheck.place(relx=0.637, rely=0.362, relwidth=0.17, relheight=0.023)

        self.VipsLevelSevenCheckVar = StringVar(value='0')
        self.style.configure('VipsLevelSevenCheck.TCheckbutton',font=('宋体',9))
        self.VipsLevelSevenCheck = Checkbutton(self.Frame2, text='超神', variable=self.VipsLevelSevenCheckVar, style='VipsLevelSevenCheck.TCheckbutton')
        self.VipsLevelSevenCheck.place(relx=0.332, rely=0.384, relwidth=0.17, relheight=0.034)

        self.VipsLevelAllCheckVar = StringVar(value='0')
        self.style.configure('VipsLevelAllCheck.TCheckbutton',foreground='#000000', font=('宋体',9))
        self.VipsLevelAllCheck = Checkbutton(self.Frame2, text='欢迎所有', variable=self.VipsLevelAllCheckVar, style='VipsLevelAllCheck.TCheckbutton')
        self.VipsLevelAllCheck.place(relx=0.637, rely=0.384, relwidth=0.253, relheight=0.034)

        self.FansLevelOneCheckVar = StringVar(value='0')
        self.style.configure('FansLevelOneCheck.TCheckbutton',font=('宋体',9))
        self.FansLevelOneCheck = Checkbutton(self.Frame2, text='一级', variable=self.FansLevelOneCheckVar, style='FansLevelOneCheck.TCheckbutton')
        self.FansLevelOneCheck.place(relx=0.332, rely=0.428, relwidth=0.17, relheight=0.023)

        self.FansLevelThreeCheckVar = StringVar(value='0')
        self.style.configure('FansLevelThreeCheck.TCheckbutton',font=('宋体',9))
        self.FansLevelThreeCheck = Checkbutton(self.Frame2, text='三级', variable=self.FansLevelThreeCheckVar, style='FansLevelThreeCheck.TCheckbutton')
        self.FansLevelThreeCheck.place(relx=0.637, rely=0.428, relwidth=0.17, relheight=0.023)

        self.FansLevelFiveCheckVar = StringVar(value='0')
        self.style.configure('FansLevelFiveCheck.TCheckbutton',font=('宋体',9))
        self.FansLevelFiveCheck = Checkbutton(self.Frame2, text='五级', variable=self.FansLevelFiveCheckVar, style='FansLevelFiveCheck.TCheckbutton')
        self.FansLevelFiveCheck.place(relx=0.332, rely=0.45, relwidth=0.17, relheight=0.023)

        self.FansLevelSevenCheckVar = StringVar(value='0')
        self.style.configure('FansLevelSevenCheck.TCheckbutton',font=('宋体',9))
        self.FansLevelSevenCheck = Checkbutton(self.Frame2, text='七级', variable=self.FansLevelSevenCheckVar, style='FansLevelSevenCheck.TCheckbutton')
        self.FansLevelSevenCheck.place(relx=0.637, rely=0.45, relwidth=0.17, relheight=0.023)

        self.FansLevelNineCheckVar = StringVar(value='0')
        self.style.configure('FansLevelNineCheck.TCheckbutton',font=('宋体',9))
        self.FansLevelNineCheck = Checkbutton(self.Frame2, text='九级', variable=self.FansLevelNineCheckVar, style='FansLevelNineCheck.TCheckbutton')
        self.FansLevelNineCheck.place(relx=0.332, rely=0.472, relwidth=0.17, relheight=0.023)

        self.FansLevelElevenCheckVar = StringVar(value='0')
        self.style.configure('FansLevelElevenCheck.TCheckbutton',font=('宋体',9))
        self.FansLevelElevenCheck = Checkbutton(self.Frame2, text='十一级', variable=self.FansLevelElevenCheckVar, style='FansLevelElevenCheck.TCheckbutton')
        self.FansLevelElevenCheck.place(relx=0.637, rely=0.472, relwidth=0.225, relheight=0.023)

        self.FansLevelAllCheckVar = StringVar(value='0')
        self.style.configure('FansLevelAllCheck.TCheckbutton',font=('宋体',9))
        self.FansLevelAllCheck = Checkbutton(self.Frame2, text='所有', variable=self.FansLevelAllCheckVar, style='FansLevelAllCheck.TCheckbutton')
        self.FansLevelAllCheck.place(relx=0.332, rely=0.494, relwidth=0.17, relheight=0.034)

        self.FansLevelPersonalizedCheckVar = StringVar(value='0')
        self.style.configure('FansLevelPersonalizedCheck.TCheckbutton',font=('宋体',9))
        self.FansLevelPersonalizedCheck = Checkbutton(self.Frame2, text='自定义', variable=self.FansLevelPersonalizedCheckVar, style='FansLevelPersonalizedCheck.TCheckbutton')
        self.FansLevelPersonalizedCheck.place(relx=0.637, rely=0.494, relwidth=0.308, relheight=0.034)

        self.style.configure('ThanksGiftMoreThanUnitLable.TLabel',anchor='w', font=('宋体',9))
        self.ThanksGiftMoreThanUnitLable = Label(self.Frame2, text='元', style='ThanksGiftMoreThanUnitLable.TLabel')
        self.ThanksGiftMoreThanUnitLable.place(relx=0.803, rely=0.274, relwidth=0.114, relheight=0.034)

        self.style.configure('ThanksGiftMoreThanLable.TLabel',anchor='w', font=('宋体',9))
        self.ThanksGiftMoreThanLable = Label(self.Frame2, text='大于:', style='ThanksGiftMoreThanLable.TLabel')
        self.ThanksGiftMoreThanLable.place(relx=0.415, rely=0.274, relwidth=0.114, relheight=0.034)

        self.style.configure('BroadcastModelText.TLabel',anchor='w', font=('宋体',9))
        self.BroadcastModelText = Label(self.Frame2, text='启动后显示', style='BroadcastModelText.TLabel')
        self.BroadcastModelText.place(relx=0.415, rely=0.176, relwidth=0.484, relheight=0.027)

        self.style.configure('BroadcastModelLabel.TLabel',anchor='w', font=('宋体',9))
        self.BroadcastModelLabel = Label(self.Frame2, text='直播模式:', style='BroadcastModelLabel.TLabel')
        self.BroadcastModelLabel.place(relx=0.028, rely=0.176, relwidth=0.325, relheight=0.027)

        self.style.configure('Line2.TSeparator',background='#000000')
        self.Line2 = Separator(self.Frame2, orient='horizontal', style='Line2.TSeparator')
        self.Line2.place(relx=0., rely=0.571, relwidth=0.997, relheight=0.0014)

        self.style.configure('Line1.TSeparator',background='#000000')
        self.Line1 = Separator(self.Frame2, orient='horizontal', style='Line1.TSeparator')
        self.Line1.place(relx=0., rely=0.209, relwidth=0.997, relheight=0.0014)

        self.style.configure('PodcastNameText.TLabel',anchor='w', font=('宋体',9))
        self.PodcastNameText = Label(self.Frame2, text='启动后显示', style='PodcastNameText.TLabel')
        self.PodcastNameText.place(relx=0.415, rely=0.088, relwidth=0.484, relheight=0.027)

        self.style.configure('PodcastNameLable.TLabel',anchor='w', font=('宋体',9))
        self.PodcastNameLable = Label(self.Frame2, text='主播名称:', style='PodcastNameLable.TLabel')
        self.PodcastNameLable.place(relx=0.028, rely=0.088, relwidth=0.28, relheight=0.023)

        self.style.configure('ThanksGiftInfoFormartLable.TLabel',anchor='w', font=('宋体',9))
        self.ThanksGiftInfoFormartLable = Label(self.Frame2, text='答谢礼物信息格式:', style='ThanksGiftInfoFormartLable.TLabel')
        self.ThanksGiftInfoFormartLable.place(relx=0.028, rely=0.911, relwidth=0.353, relheight=0.027)

        self.style.configure('StartLotteryInfoFormartLable.TLabel',anchor='w', font=('宋体',9))
        self.StartLotteryInfoFormartLable = Label(self.Frame2, text='开始抽奖信息格式:', style='StartLotteryInfoFormartLable.TLabel')
        self.StartLotteryInfoFormartLable.place(relx=0.028, rely=0.801, relwidth=0.353, relheight=0.027)

        self.style.configure('ThanksShareInfoFormartLable.TLabel',anchor='w', font=('宋体',9))
        self.ThanksShareInfoFormartLable = Label(self.Frame2, text='感谢分享信息格式:', style='ThanksShareInfoFormartLable.TLabel')
        self.ThanksShareInfoFormartLable.place(relx=0.028, rely=0.691, relwidth=0.353, relheight=0.027)

        self.style.configure('WelcomeVipsInfoFormartLable.TLabel',anchor='w', font=('宋体',9))
        self.WelcomeVipsInfoFormartLable = Label(self.Frame2, text='贵宾欢迎信息格式:', style='WelcomeVipsInfoFormartLable.TLabel')
        self.WelcomeVipsInfoFormartLable.place(relx=0.028, rely=0.582, relwidth=0.353, relheight=0.027)

        self.style.configure('RoomIdLable.TLabel',anchor='w', foreground='#000000', font=('宋体',9))
        self.RoomIdLable = Label(self.Frame2, text='房间号:', style='RoomIdLable.TLabel')
        self.RoomIdLable.place(relx=0.028, rely=0.044, relwidth=0.28, relheight=0.023)

        self.style.configure('UserNicknameLabel.TLabel',anchor='w', font=('宋体',9))
        self.UserNicknameLabel = Label(self.Frame2, text='房管账号:', style='UserNicknameLabel.TLabel')
        self.UserNicknameLabel.place(relx=0.028, rely=0.132, relwidth=0.28, relheight=0.023)

        self.style.configure('UserNicknameText.TLabel',anchor='w', font=('宋体',9))
        self.UserNicknameText = Label(self.Frame2, text='登陆后显示', style='UserNicknameText.TLabel')
        self.UserNicknameText.place(relx=0.415, rely=0.132, relwidth=0.474, relheight=0.023)

        self.style.configure('RobotOperationFrame.TLabelframe',font=('宋体',9))
        self.RobotOperationFrame = LabelFrame(self.Main, text='机器人操作', style='RobotOperationFrame.TLabelframe')
        self.RobotOperationFrame.place(relx=0.179, rely=0.07, relwidth=0.09, relheight=0.87)

        self.style.configure('PauseRobotCommand.TButton',font=('宋体',9))
        self.PauseRobotCommand = Button(self.RobotOperationFrame, text='暂停机器人', command=self.PauseRobotCommand_Cmd, style='PauseRobotCommand.TButton')
        self.PauseRobotCommand.place(relx=0.157, rely=0.298, relwidth=0.686, relheight=0.047)

        self.style.configure('CloseRobotCommand.TButton',font=('宋体',9))
        self.CloseRobotCommand = Button(self.RobotOperationFrame, text='关闭机器人', command=self.CloseRobotCommand_Cmd, style='CloseRobotCommand.TButton')
        self.CloseRobotCommand.place(relx=0.157, rely=0.379, relwidth=0.686, relheight=0.047)

        self.style.configure('ResetAllSettingsCommand.TButton',font=('宋体',9))
        self.ResetAllSettingsCommand = Button(self.RobotOperationFrame, text='重置所有设置', command=self.ResetAllSettingsCommand_Cmd, style='ResetAllSettingsCommand.TButton')
        self.ResetAllSettingsCommand.place(relx=0.157, rely=0.218, relwidth=0.686, relheight=0.047)

        self.style.configure('StartRobotCommand.TButton',font=('宋体',9))
        self.StartRobotCommand = Button(self.RobotOperationFrame, text='启动机器人', command=self.StartRobotCommand_Cmd, style='StartRobotCommand.TButton')
        self.StartRobotCommand.place(relx=0.157, rely=0.057, relwidth=0.686, relheight=0.047)

        self.style.configure('UpdateAndFixCommand.TButton',font=('宋体',9))
        self.UpdateAndFixCommand = Button(self.RobotOperationFrame, text='更新及修复', command=self.UpdateAndFixCommand_Cmd, style='UpdateAndFixCommand.TButton')
        self.UpdateAndFixCommand.place(relx=0.157, rely=0.918, relwidth=0.686, relheight=0.047)

        self.style.configure('LoginAdminAccountCommand.TButton',font=('宋体',9))
        self.LoginAdminAccountCommand = Button(self.RobotOperationFrame, text='登录房管账号', command=self.LoginAdminAccountCommand_Cmd, style='LoginAdminAccountCommand.TButton')
        self.LoginAdminAccountCommand.place(relx=0.157, rely=0.138, relwidth=0.686, relheight=0.047)

        self.style.configure('ExitRobotCommand.TButton',font=('宋体',9))
        self.ExitRobotCommand = Button(self.RobotOperationFrame, text='退出机器人', command=self.ExitRobotCommand_Cmd, style='ExitRobotCommand.TButton')
        self.ExitRobotCommand.place(relx=0.157, rely=0.838, relwidth=0.686, relheight=0.047)

        self.style.configure('CustomeReplaySettingsFrame.TLabelframe',font=('宋体',9))
        self.CustomeReplaySettingsFrame = LabelFrame(self.Main, text='自定义回复设置', style='CustomeReplaySettingsFrame.TLabelframe')
        self.CustomeReplaySettingsFrame.place(relx=0.797, rely=0.4, relwidth=0.189, relheight=0.321)

        self.style.configure('CustomeReplaySettingsDeleteOrRestoreCommand.TButton',font=('宋体',9))
        self.CustomeReplaySettingsDeleteOrRestoreCommand = Button(self.CustomeReplaySettingsFrame, text='删除/取消', command=self.CustomeReplaySettingsDeleteOrRestoreCommand_Cmd, style='CustomeReplaySettingsDeleteOrRestoreCommand.TButton')
        self.CustomeReplaySettingsDeleteOrRestoreCommand.place(relx=0.498, rely=0.685, relwidth=0.327, relheight=0.128)

        self.style.configure('CustomeReplaySettingsAddOrModifyCommand.TButton',font=('宋体',9))
        self.CustomeReplaySettingsAddOrModifyCommand = Button(self.CustomeReplaySettingsFrame, text='添加/修改', command=self.CustomeReplaySettingsAddOrModifyCommand_Cmd, style='CustomeReplaySettingsAddOrModifyCommand.TButton')
        self.CustomeReplaySettingsAddOrModifyCommand.place(relx=0.125, rely=0.685, relwidth=0.327, relheight=0.128)

        self.CustomeReplaySettingsReplyInputVar = StringVar(value='输入自定义回复设置')
        self.CustomeReplaySettingsReplyInput = Entry(self.CustomeReplaySettingsFrame, text='输入自定义回复设置', textvariable=self.CustomeReplaySettingsReplyInputVar, font=('宋体',9))
        self.CustomeReplaySettingsReplyInput.place(relx=0.349, rely=0.467, relwidth=0.427, relheight=0.128)

        self.CustomeReplaySettingsKeyworldInputVar = StringVar(value='输入关键字')
        self.CustomeReplaySettingsKeyworldInput = Entry(self.CustomeReplaySettingsFrame, text='输入关键字', textvariable=self.CustomeReplaySettingsKeyworldInputVar, font=('宋体',9))
        self.CustomeReplaySettingsKeyworldInput.place(relx=0.349, rely=0.249, relwidth=0.427, relheight=0.128)

        self.style.configure('CustomeReplaySettingsReplyLable.TLabel',anchor='w', font=('宋体',9))
        self.CustomeReplaySettingsReplyLable = Label(self.CustomeReplaySettingsFrame, text='自定义回复:', style='CustomeReplaySettingsReplyLable.TLabel')
        self.CustomeReplaySettingsReplyLable.place(relx=0.075, rely=0.467, relwidth=0.252, relheight=0.109)

        self.style.configure('CustomeReplaySettingsKeyworldLabel.TLabel',anchor='w', font=('宋体',9))
        self.CustomeReplaySettingsKeyworldLabel = Label(self.CustomeReplaySettingsFrame, text='关键字:', style='CustomeReplaySettingsKeyworldLabel.TLabel')
        self.CustomeReplaySettingsKeyworldLabel.place(relx=0.075, rely=0.249, relwidth=0.227, relheight=0.078)

        self.style.configure('CustomeNicknameSettingsFrame.TLabelframe',font=('宋体',9))
        self.CustomeNicknameSettingsFrame = LabelFrame(self.Main, text='自定义昵称设置', style='CustomeNicknameSettingsFrame.TLabelframe')
        self.CustomeNicknameSettingsFrame.place(relx=0.797, rely=0.07, relwidth=0.189, relheight=0.321)

        self.OriginalNicknameInputVar = StringVar(value='输入昵称或者双击昵称')
        self.OriginalNicknameInput = Entry(self.CustomeNicknameSettingsFrame, text='输入昵称或者双击昵称', textvariable=self.OriginalNicknameInputVar, font=('宋体',9))
        self.OriginalNicknameInput.place(relx=0.374, rely=0.249, relwidth=0.427, relheight=0.128)

        self.CustomizedNicknameInputVar = StringVar(value='输入自定义昵称')
        self.CustomizedNicknameInput = Entry(self.CustomeNicknameSettingsFrame, text='输入自定义昵称', textvariable=self.CustomizedNicknameInputVar, font=('宋体',9))
        self.CustomizedNicknameInput.place(relx=0.374, rely=0.467, relwidth=0.427, relheight=0.128)

        self.style.configure('CustomizedNicknameAddOrModifyCommand.TButton',font=('宋体',9))
        self.CustomizedNicknameAddOrModifyCommand = Button(self.CustomeNicknameSettingsFrame, text='添加/修改', command=self.CustomizedNicknameAddOrModifyCommand_Cmd, style='CustomizedNicknameAddOrModifyCommand.TButton')
        self.CustomizedNicknameAddOrModifyCommand.place(relx=0.125, rely=0.685, relwidth=0.327, relheight=0.128)

        self.style.configure('CustomizedNicknameDeleteOrRestorCommand.TButton',font=('宋体',9))
        self.CustomizedNicknameDeleteOrRestorCommand = Button(self.CustomeNicknameSettingsFrame, text='删除/取消', command=self.CustomizedNicknameDeleteOrRestorCommand_Cmd, style='CustomizedNicknameDeleteOrRestorCommand.TButton')
        self.CustomizedNicknameDeleteOrRestorCommand.place(relx=0.498, rely=0.685, relwidth=0.327, relheight=0.128)

        self.style.configure('OriginalNicknameLabel.TLabel',anchor='w', font=('宋体',9))
        self.OriginalNicknameLabel = Label(self.CustomeNicknameSettingsFrame, text='原始昵称:', style='OriginalNicknameLabel.TLabel')
        self.OriginalNicknameLabel.place(relx=0.075, rely=0.249, relwidth=0.268, relheight=0.078)

        self.style.configure('CustomizedNicknameLable.TLabel',anchor='w', font=('宋体',9))
        self.CustomizedNicknameLable = Label(self.CustomeNicknameSettingsFrame, text='自定义昵称:', style='CustomizedNicknameLable.TLabel')
        self.CustomizedNicknameLable.place(relx=0.075, rely=0.467, relwidth=0.277, relheight=0.078)

        self.style.configure('LogInfoLable.TLabel',anchor='w', foreground='#FF0000', font=('宋体',9))
        self.LogInfoLable = Label(self.Main, text='机器人未启动,房间号未录入,房管号未登录,请先登录房管号并录入房间号启动机器人', style='LogInfoLable.TLabel')
        self.LogInfoLable.place(relx=0.189, rely=0.03, relwidth=0.793, relheight=0.021)

        self.style.configure('CopyRightLabel1.TLabel',anchor='w', foreground='#6D6D6D', font=('宋体',9))
        self.CopyRightLabel1 = Label(self.Main, text='CopyRight@ 2020 WangZhen <wangzhenjjcn@gmail.com> Myazure.org', style='CopyRightLabel1.TLabel')
        self.CopyRightLabel1.place(relx=0.759, rely=0.959, relwidth=0.227, relheight=0.031)

        #function behind:
        self.ThanksShareCheck.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="ThanksShareCheck",item=self.ThanksShareCheckVar,option="<Button-1>",item_type="check",log="",data=""))
        self.ThanksOnTVGiftCheck.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="ThanksOnTVGiftCheck" ,option="<Button-1>",item=self.ThanksOnTVGiftCheckVar,item_type="check",log="",data=""))
        self.ThanksGiftCheck.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="ThanksGiftCheck",item=self.ThanksGiftCheckVar,option="<Button-1>",item_type="check",log="",data=""))
        self.WelcomeVipsCheck.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="WelcomeVipsCheck",item=self.WelcomeVipsCheckVar,option="<Button-1>",item_type="check",log="",data=""))
        self.WelcomeFansCheck.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="WelcomeFansCheck",item=self.WelcomeFansCheckVar,option="<Button-1>",item_type="check",log="",data="欢迎粉丝"))
        self.FansLevelOneCheck.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="FansLevelOneCheck",item=self.FansLevelOneCheckVar,option="<Button-1>",item_type="check",log="",data="一级粉丝"))
        self.FansLevelThreeCheck.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="FansLevelThreeCheck",item=self.FansLevelThreeCheckVar,option="<Button-1>",item_type="check",log="",data="三级粉丝"))
        self.FansLevelFiveCheck.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="FansLevelFiveCheck",item=self.FansLevelFiveCheckVar,option="<Button-1>",item_type="check",log="",data="五级粉丝"))
        self.FansLevelSevenCheck.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="FansLevelSevenCheck",item=self.FansLevelSevenCheckVar,option="<Button-1>",item_type="check",log="",data="七级粉丝"))
        self.FansLevelNineCheck.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="FansLevelNineCheck",item=self.FansLevelNineCheckVar,option="<Button-1>",item_type="check",log="",data="九级粉丝"))
        self.FansLevelElevenCheck.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="FansLevelElevenCheck",item=self.FansLevelElevenCheckVar,option="<Button-1>",item_type="check",log="",data="十一级粉丝"))
        self.FansLevelAllCheck.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="FansLevelAllCheck",item=self.FansLevelAllCheckVar,option="<Button-1>",item_type="check",log="",data="所有等级粉丝"))
        self.FansLevelPersonalizedCheck.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="FansLevelPersonalizedCheck",item=self.FansLevelPersonalizedCheckVar,option="<Button-1>",item_type="check",log="",data=""))
        self.VipsLevelOneCheck.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="VipsLevelOneCheck",item=self.VipsLevelOneCheckVar,option="<Button-1>",item_type="check",log="",data="剑士"))
        self.VipsLevelTwoCheck.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="VipsLevelTwoCheck",item=self.VipsLevelTwoCheckVar,option="<Button-1>",item_type="check",log="",data="骑士"))
        self.VipsLevelThreeCheck.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="VipsLevelThreeCheck",item=self.VipsLevelThreeCheckVar,option="<Button-1>",item_type="check",log="",data="领主"))
        self.VipsLevelFourCheck.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="VipsLevelFourCheck",item=self.VipsLevelFourCheckVar,option="<Button-1>",item_type="check",log="",data="公爵"))
        self.VipsLevelFiveCheck.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="VipsLevelFiveCheck",item=self.VipsLevelFiveCheckVar,option="<Button-1>",item_type="check",log="",data="君王"))
        self.VipsLevelSixCheck.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="VipsLevelSixCheck",item=self.VipsLevelSixCheckVar,option="<Button-1>",item_type="check",log="",data="帝皇"))
        self.VipsLevelSevenCheck.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="VipsLevelSevenCheck",item=self.VipsLevelSevenCheckVar,option="<Button-1>",item_type="check",log="",data="超神"))
        self.VipsLevelAllCheck.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="VipsLevelAllCheck",item=self.VipsLevelAllCheckVar,option="<Button-1>",item_type="check",log="",data="所有等级"))
        self.ShowWebViewerCheck.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="ShowWebViewerCheck",item=self.ShowWebViewerCheckVar,option="<Button-1>",item_type="check",log="",data="显示直播画面"))

        self.ThanksShareCheck.bind(sequence='<Key-space>', func=self.handler_adaptor(self.handler, name="ThanksShareCheck",item=self.ThanksShareCheckVar,option="<Button-1>",item_type="check",log="",data=""))
        self.ThanksOnTVGiftCheck.bind(sequence='<Key-space>', func=self.handler_adaptor(self.handler, name="ThanksOnTVGiftCheck" ,option="<Button-1>",item=self.ThanksOnTVGiftCheckVar,item_type="check",log="",data=""))
        self.ThanksGiftCheck.bind(sequence='<Key-space>', func=self.handler_adaptor(self.handler, name="ThanksGiftCheck",item=self.ThanksGiftCheckVar,option="<Button-1>",item_type="check",log="",data=""))
        self.WelcomeVipsCheck.bind(sequence='<Key-space>', func=self.handler_adaptor(self.handler, name="WelcomeVipsCheck",item=self.WelcomeVipsCheckVar,option="<Button-1>",item_type="check",log="",data=""))
        self.WelcomeFansCheck.bind(sequence='<Key-space>', func=self.handler_adaptor(self.handler, name="WelcomeFansCheck",item=self.WelcomeFansCheckVar,option="<Button-1>",item_type="check",log="",data=""))
        self.FansLevelOneCheck.bind(sequence='<Key-space>', func=self.handler_adaptor(self.handler, name="FansLevelOneCheck",item=self.FansLevelOneCheckVar,option="<Button-1>",item_type="check",log="",data="一级粉丝"))
        self.FansLevelThreeCheck.bind(sequence='<Key-space>', func=self.handler_adaptor(self.handler, name="FansLevelThreeCheck",item=self.FansLevelThreeCheckVar,option="<Button-1>",item_type="check",log="",data=""))
        self.FansLevelFiveCheck.bind(sequence='<Key-space>', func=self.handler_adaptor(self.handler, name="FansLevelFiveCheck",item=self.FansLevelFiveCheckVar,option="<Button-1>",item_type="check",log="",data=""))
        self.FansLevelSevenCheck.bind(sequence='<Key-space>', func=self.handler_adaptor(self.handler, name="FansLevelSevenCheck",item=self.FansLevelSevenCheckVar,option="<Button-1>",item_type="check",log="",data=""))
        self.FansLevelNineCheck.bind(sequence='<Key-space>', func=self.handler_adaptor(self.handler, name="FansLevelNineCheck",item=self.FansLevelNineCheckVar,option="<Button-1>",item_type="check",log="",data=""))
        self.FansLevelElevenCheck.bind(sequence='<Key-space>', func=self.handler_adaptor(self.handler, name="FansLevelElevenCheck",item=self.FansLevelElevenCheckVar,option="<Button-1>",item_type="check",log="",data=""))
        self.FansLevelAllCheck.bind(sequence='<Key-space>', func=self.handler_adaptor(self.handler, name="FansLevelAllCheck",item=self.FansLevelAllCheckVar,option="<Button-1>",item_type="check",log="",data=""))
        self.FansLevelPersonalizedCheck.bind(sequence='<Key-space>', func=self.handler_adaptor(self.handler, name="FansLevelPersonalizedCheck",item=self.FansLevelPersonalizedCheckVar,option="<Button-1>",item_type="check",log="",data=""))
        self.VipsLevelOneCheck.bind(sequence='<Key-space>', func=self.handler_adaptor(self.handler, name="VipsLevelOneCheck",item=self.VipsLevelOneCheckVar,option="<Button-1>",item_type="check",log="",data=""))
        self.VipsLevelTwoCheck.bind(sequence='<Key-space>', func=self.handler_adaptor(self.handler, name="VipsLevelTwoCheck",item=self.VipsLevelTwoCheckVar,option="<Button-1>",item_type="check",log="",data=""))
        self.VipsLevelThreeCheck.bind(sequence='<Key-space>', func=self.handler_adaptor(self.handler, name="VipsLevelThreeCheck",item=self.VipsLevelThreeCheckVar,option="<Button-1>",item_type="check",log="",data=""))
        self.VipsLevelFourCheck.bind(sequence='<Key-space>', func=self.handler_adaptor(self.handler, name="VipsLevelFourCheck",item=self.VipsLevelFourCheckVar,option="<Button-1>",item_type="check",log="",data=""))
        self.VipsLevelFiveCheck.bind(sequence='<Key-space>', func=self.handler_adaptor(self.handler, name="VipsLevelFiveCheck",item=self.VipsLevelFiveCheckVar,option="<Button-1>",item_type="check",log="",data=""))
        self.VipsLevelSixCheck.bind(sequence='<Key-space>', func=self.handler_adaptor(self.handler, name="VipsLevelSixCheck",item=self.VipsLevelSixCheckVar,option="<Button-1>",item_type="check",log="",data=""))
        self.VipsLevelSevenCheck.bind(sequence='<Key-space>', func=self.handler_adaptor(self.handler, name="VipsLevelSevenCheck",item=self.VipsLevelSevenCheckVar,option="<Button-1>",item_type="check",log="",data=""))
        self.VipsLevelAllCheck.bind(sequence='<Key-space>', func=self.handler_adaptor(self.handler, name="VipsLevelAllCheck",item=self.VipsLevelAllCheckVar,option="<Button-1>",item_type="check",log="",data=""))
        self.ShowWebViewerCheck.bind(sequence='<Key-space>', func=self.handler_adaptor(self.handler, name="ShowWebViewerCheck",item=self.ShowWebViewerCheckVar,option="<Button-1>",item_type="check",log="",data=""))

        self.RomIdInput.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="RomIdInput",item=self.RomIdInputVar,option="<Button-1>",item_type="input",log="在这里输入被控虎牙房间号(或者是主播的频道名称例如直播间地址是http://www.huya.com/naoye999可以输入naoye999作为房间号)",data="点击输入房间号"))
        self.ThanksGiftMoreThanInput.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="ThanksGiftMoreThanInput",item=self.ThanksGiftMoreThanInputVar,option="<Button-1>",item_type="input",log="",data="0"))
        self.WelcomeVipsInfoFormartInput.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="WelcomeVipsInfoFormartInput",item=self.WelcomeVipsInfoFormartInputVar,option="<Button-1>",item_type="input",log="",data="欢迎[送花]切克闹[送花]"))
        self.ThanksShareInfoFormartInput.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="ThanksShareInfoFormartInput",item=self.ThanksShareInfoFormartInputVar,option="<Button-1>",item_type="input",log="",data="谢谢[送花]切克闹[送花]分享直播间"))
        self.StartLotteryInfoFormartInput.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="StartLotteryInfoFormartInput",item=self.StartLotteryInfoFormartInputVar,option="<Button-1>",item_type="input",log="",data="奖品:[心动]【奖品名称】[心动]走一波[心动]"))
        self.ThanksGiftInfoFormartInput.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="ThanksGiftInfoFormartInput",item=self.ThanksGiftInfoFormartInputVar,option="<Button-1>",item_type="input",log="",data="谢谢[心动]切克闹[送花]的1314个虎牙一号"))
        self.OriginalNicknameInput.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="OriginalNicknameInput",item=self.OriginalNicknameInputVar,option="<Button-1>",item_type="input",log="",data="输入昵称或者双击昵称"))
        self.CustomizedNicknameInput.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="CustomizedNicknameInput",item=self.CustomizedNicknameInputVar,option="<Button-1>",item_type="input",log="",data="输入自定义昵称"))
        self.CustomeReplaySettingsKeyworldInput.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="CustomeReplaySettingsKeyworldInput",item=self.CustomeReplaySettingsKeyworldInputVar,option="<Button-1>",item_type="input",log="",data="输入关键字"))
        self.CustomeReplaySettingsReplyInput.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="CustomeReplaySettingsReplyInput",item=self.CustomeReplaySettingsReplyInputVar,option="<Button-1>",item_type="input",log="",data="输入自定义回复设置"))
        self.ScheduledInfoInput.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="ScheduledInfoInput",item=self.ScheduledInfoInputVar,option="<Button-1>",item_type="input",log="",data=""))
        self.ScheduledInfoTimeInput.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="ScheduledInfoTimeInput",item=self.ScheduledInfoTimeInputVar,option="<Button-1>",item_type="input",log="",data="5"))

        self.RomIdInput.bind(sequence='<FocusIn>', func=self.handler_adaptor(self.handler, name="RomIdInput",item=self.RomIdInputVar,option="<Button-1>",item_type="input",log="在这里输入被控虎牙房间号(或者是主播的频道名称例如直播间地址是http://www.huya.com/naoye999可以输入naoye999作为房间号)",data="点击输入房间号"))
        self.ThanksGiftMoreThanInput.bind(sequence='<FocusIn>', func=self.handler_adaptor(self.handler, name="ThanksGiftMoreThanInput",item=self.ThanksGiftMoreThanInputVar,option="<Button-1>",item_type="input",log="",data="0"))
        self.WelcomeVipsInfoFormartInput.bind(sequence='<FocusIn>', func=self.handler_adaptor(self.handler, name="WelcomeVipsInfoFormartInput",item=self.WelcomeVipsInfoFormartInputVar,option="<Button-1>",item_type="input",log="",data="欢迎[送花]切克闹[送花]"))
        self.ThanksShareInfoFormartInput.bind(sequence='<FocusIn>', func=self.handler_adaptor(self.handler, name="ThanksShareInfoFormartInput",item=self.ThanksShareInfoFormartInputVar,option="<Button-1>",item_type="input",log="",data="谢谢[送花]切克闹[送花]分享直播间"))
        self.StartLotteryInfoFormartInput.bind(sequence='<FocusIn>', func=self.handler_adaptor(self.handler, name="StartLotteryInfoFormartInput",item=self.StartLotteryInfoFormartInputVar,option="<Button-1>",item_type="input",log="",data="奖品:[心动]【奖品名称】[心动]走一波[心动]"))
        self.ThanksGiftInfoFormartInput.bind(sequence='<FocusIn>', func=self.handler_adaptor(self.handler, name="ThanksGiftInfoFormartInput",item=self.ThanksGiftInfoFormartInputVar,option="<Button-1>",item_type="input",log="",data="谢谢[心动]切克闹[送花]的1314个虎牙一号"))
        self.OriginalNicknameInput.bind(sequence='<FocusIn>', func=self.handler_adaptor(self.handler, name="OriginalNicknameInput",item=self.OriginalNicknameInputVar,option="<Button-1>",item_type="input",log="",data="输入昵称或者双击昵称"))
        self.CustomizedNicknameInput.bind(sequence='<FocusIn>', func=self.handler_adaptor(self.handler, name="CustomizedNicknameInput",item=self.CustomizedNicknameInputVar,option="<Button-1>",item_type="input",log="",data="输入自定义昵称"))
        self.CustomeReplaySettingsKeyworldInput.bind(sequence='<FocusIn>', func=self.handler_adaptor(self.handler, name="CustomeReplaySettingsKeyworldInput",item=self.CustomeReplaySettingsKeyworldInputVar,option="<Button-1>",item_type="input",log="",data="输入关键字"))
        self.CustomeReplaySettingsReplyInput.bind(sequence='<FocusIn>', func=self.handler_adaptor(self.handler, name="CustomeReplaySettingsReplyInput",item=self.CustomeReplaySettingsReplyInputVar,option="<Button-1>",item_type="input",log="",data="输入自定义回复设置"))
        self.ScheduledInfoInput.bind(sequence='<FocusIn>', func=self.handler_adaptor(self.handler, name="ScheduledInfoInput",item=self.ScheduledInfoInputVar,option="<FocusIn>",item_type="input",log="",data=""))
        self.ScheduledInfoTimeInput.bind(sequence='<FocusIn>', func=self.handler_adaptor(self.handler, name="ScheduledInfoTimeInput",item=self.ScheduledInfoTimeInputVar,option="<FocusIn>",item_type="input",log="",data="5"))


        self.RomIdInput.bind(sequence='<FocusOut>', func=self.handler_adaptor(self.handler, name="RomIdInput",item=self.RomIdInputVar,option="<FocusOut>",item_type="input",log="",data="点击输入房间号"))
        self.ThanksGiftMoreThanInput.bind(sequence='<FocusOut>', func=self.handler_adaptor(self.handler, name="ThanksGiftMoreThanInput",item=self.ThanksGiftMoreThanInputVar,option="<FocusOut>",item_type="input",log="",data="0"))
        self.WelcomeVipsInfoFormartInput.bind(sequence='<FocusOut>', func=self.handler_adaptor(self.handler, name="WelcomeVipsInfoFormartInput",item=self.WelcomeVipsInfoFormartInputVar,option="<FocusOut>",item_type="input",log="",data="欢迎[送花]切克闹[送花]"))
        self.ThanksShareInfoFormartInput.bind(sequence='<FocusOut>', func=self.handler_adaptor(self.handler, name="ThanksShareInfoFormartInput",item=self.ThanksShareInfoFormartInputVar,option="<FocusOut>",item_type="input",log="",data="谢谢[送花]切克闹[送花]分享直播间"))
        self.StartLotteryInfoFormartInput.bind(sequence='<FocusOut>', func=self.handler_adaptor(self.handler, name="StartLotteryInfoFormartInput",item=self.StartLotteryInfoFormartInputVar,option="<FocusOut>",item_type="input",log="",data="奖品:[心动]【奖品名称】[心动]走一波[心动]"))
        self.ThanksGiftInfoFormartInput.bind(sequence='<FocusOut>', func=self.handler_adaptor(self.handler, name="ThanksGiftInfoFormartInput",item=self.ThanksGiftInfoFormartInputVar,option="<FocusOut>",item_type="input",log="",data="谢谢[心动]切克闹[送花]的1314个虎牙一号"))
        self.OriginalNicknameInput.bind(sequence='<FocusOut>', func=self.handler_adaptor(self.handler, name="OriginalNicknameInput",item=self.OriginalNicknameInputVar,option="<FocusOut>",item_type="input",log="",data="输入昵称或者双击昵称"))
        self.CustomizedNicknameInput.bind(sequence='<FocusOut>', func=self.handler_adaptor(self.handler, name="CustomizedNicknameInput",item=self.CustomizedNicknameInputVar,option="<FocusOut>",item_type="input",log="",data="输入自定义昵称"))
        self.CustomeReplaySettingsKeyworldInput.bind(sequence='<FocusOut>', func=self.handler_adaptor(self.handler, name="CustomeReplaySettingsKeyworldInput",item=self.CustomeReplaySettingsKeyworldInputVar,option="<FocusOut>",item_type="input",log="",data="输入关键字"))
        self.CustomeReplaySettingsReplyInput.bind(sequence='<FocusOut>', func=self.handler_adaptor(self.handler, name="CustomeReplaySettingsReplyInput",item=self.CustomeReplaySettingsReplyInputVar,option="<FocusOut>",item_type="input",log="",data="输入自定义回复设置"))
        self.ScheduledInfoInput.bind(sequence='<FocusOut>', func=self.handler_adaptor(self.handler, name="ScheduledInfoInput",item=self.ScheduledInfoInputVar,option="<FocusOut>",item_type="input",log="",data=""))
        self.ScheduledInfoTimeInput.bind(sequence='<FocusOut>', func=self.handler_adaptor(self.handler, name="ScheduledInfoTimeInput",item=self.ScheduledInfoTimeInputVar,option="<FocusOut>",item_type="input",log="",data="5"))


        self.RomIdInput.bind(sequence='<KeyRelease>', func=self.handler_adaptor(self.handler, name="RomIdInput",item=self.RomIdInputVar,option="<KeyRelease>",item_type="input",log="",data="点击输入房间号"))
        self.ThanksGiftMoreThanInput.bind(sequence='<KeyRelease>', func=self.handler_adaptor(self.handler, name="ThanksGiftMoreThanInput",item=self.ThanksGiftMoreThanInputVar,option="<KeyRelease>",item_type="input",log="",data="0"))
        self.WelcomeVipsInfoFormartInput.bind(sequence='<KeyRelease>', func=self.handler_adaptor(self.handler, name="WelcomeVipsInfoFormartInput",item=self.WelcomeVipsInfoFormartInputVar,option="<KeyRelease>",item_type="input",log="",data="欢迎[送花]切克闹[送花]"))
        self.ThanksShareInfoFormartInput.bind(sequence='<KeyRelease>', func=self.handler_adaptor(self.handler, name="ThanksShareInfoFormartInput",item=self.ThanksShareInfoFormartInputVar,option="<KeyRelease>",item_type="input",log="",data="谢谢[送花]切克闹[送花]分享直播间"))
        self.StartLotteryInfoFormartInput.bind(sequence='<KeyRelease>', func=self.handler_adaptor(self.handler, name="StartLotteryInfoFormartInput",item=self.StartLotteryInfoFormartInputVar,option="<KeyRelease>",item_type="input",log="",data="奖品:[心动]【奖品名称】[心动]走一波[心动]"))
        self.ThanksGiftInfoFormartInput.bind(sequence='<KeyRelease>', func=self.handler_adaptor(self.handler, name="ThanksGiftInfoFormartInput",item=self.ThanksGiftInfoFormartInputVar,option="<KeyRelease>",item_type="input",log="",data="谢谢[心动]切克闹[送花]的1314个虎牙一号"))
        self.OriginalNicknameInput.bind(sequence='<KeyRelease>', func=self.handler_adaptor(self.handler, name="OriginalNicknameInput",item=self.OriginalNicknameInputVar,option="<KeyRelease>",item_type="input",log="",data="输入昵称或者双击昵称"))
        self.CustomizedNicknameInput.bind(sequence='<KeyRelease>', func=self.handler_adaptor(self.handler, name="CustomizedNicknameInput",item=self.CustomizedNicknameInputVar,option="<KeyRelease>",item_type="input",log="",data="输入自定义昵称"))
        self.CustomeReplaySettingsKeyworldInput.bind(sequence='<KeyRelease>', func=self.handler_adaptor(self.handler, name="CustomeReplaySettingsKeyworldInput",item=self.CustomeReplaySettingsKeyworldInputVar,option="<KeyRelease>",item_type="input",log="",data="输入关键字"))
        self.CustomeReplaySettingsReplyInput.bind(sequence='<KeyRelease>', func=self.handler_adaptor(self.handler, name="CustomeReplaySettingsReplyInput",item=self.CustomeReplaySettingsReplyInputVar,option="<KeyRelease>",item_type="input",log="",data="输入自定义回复设置"))
        self.ScheduledInfoInput.bind(sequence='<KeyRelease>', func=self.handler_adaptor(self.handler, name="ScheduledInfoInput",item=self.ScheduledInfoInputVar,option="<KeyRelease>",item_type="input",log="",data=""))
        self.ScheduledInfoTimeInput.bind(sequence='<KeyRelease>', func=self.handler_adaptor(self.handler, name="ScheduledInfoTimeInput",item=self.ScheduledInfoTimeInputVar,option="<KeyRelease>",item_type="input",log="",data="5"))

        self.CloseRobotCommand.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="CloseRobotCommand",item=self.CloseRobotCommand,option="<Button-1>",item_type="command",log="",data=""))
        self.CustomeReplaySettingsAddOrModifyCommand.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="CustomeReplaySettingsAddOrModifyCommand",item=self.CustomeReplaySettingsAddOrModifyCommand,option="<Button-1>",item_type="command",log="",data=""))
        self.CustomeReplaySettingsDeleteOrRestoreCommand.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="CustomeReplaySettingsDeleteOrRestoreCommand",item=self.CustomeReplaySettingsDeleteOrRestoreCommand,option="<Button-1>",item_type="command",log="",data=""))
        self.CustomeScheduledSettingsSaveCommand.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="CustomeScheduledSettingsSaveCommand",item=self.CustomeScheduledSettingsSaveCommand,option="<Button-1>",item_type="command",log="",data=""))
        self.CustomizedNicknameAddOrModifyCommand.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="CustomizedNicknameAddOrModifyCommand",item=self.CustomizedNicknameAddOrModifyCommand,option="<Button-1>",item_type="command",log="",data=""))
        self.CustomizedNicknameDeleteOrRestorCommand.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="CustomizedNicknameDeleteOrRestorCommand",item=self.CustomizedNicknameDeleteOrRestorCommand,option="<Button-1>",item_type="command",log="",data=""))
        self.ExitRobotCommand.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="ExitRobotCommand",item=self.ExitRobotCommand,option="<Button-1>",item_type="command",log="",data=""))
        self.LoginAdminAccountCommand.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="LoginAdminAccountCommand",item=self.LoginAdminAccountCommand,option="<Button-1>",item_type="command",log="",data=""))
        self.PauseRobotCommand.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="PauseRobotCommand",item=self.PauseRobotCommand,option="<Button-1>",item_type="command",log="",data=""))
        self.ResetAllSettingsCommand.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="ResetAllSettingsCommand",item=self.ResetAllSettingsCommand,option="<Button-1>",item_type="command",log="",data=""))
        self.StartRobotCommand.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="StartRobotCommand",item=self.StartRobotCommand,option="<Button-1>",item_type="command",log="",data=""))
        self.UpdateAndFixCommand.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="UpdateAndFixCommand",item=self.UpdateAndFixCommand,option="<Button-1>",item_type="command",log="",data=""))
        

        self.ChatsList.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="ChatsList",item=self.ChatsList,option="<Button-1>",item_type="list",log="",data=""))  
        self.CustomReplyList.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="CustomReplyList",item=self.CustomReplyList,option="<Button-1>",item_type="list",log="",data=""))  
        self.FansList.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="FansList",item=self.FansList,option="<Button-1>",item_type="list",log="",data=""))  
        self.NicknameList.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="NicknameList",item=self.NicknameList,option="<Button-1>",item_type="list",log="",data=""))  
        self.VIPList.bind(sequence='<Button-1>', func=self.handler_adaptor(self.handler, name="VIPList",item=self.VIPList,option="<Button-1>",item_type="list",log="",data=""))  
        
        self.ChatsList.bind(sequence='<Double-Button-1>', func=self.handler_adaptor(self.handler, name="ChatsList",item=self.ChatsList,option="<Double-Button-1>",item_type="list",log="",data=""))  
        self.CustomReplyList.bind(sequence='<Double-Button-1>', func=self.handler_adaptor(self.handler, name="CustomReplyList",item=self.CustomReplyList,option="<Double-Button-1>",item_type="list",log="",data=""))  
        self.FansList.bind(sequence='<Double-Button-1>', func=self.handler_adaptor(self.handler, name="FansList",item=self.FansList,option="<Double-Button-1>",item_type="list",log="",data=""))  
        self.NicknameList.bind(sequence='<Double-Button-1>', func=self.handler_adaptor(self.handler, name="NicknameList",item=self.NicknameList,option="<Double-Button-1>",item_type="list",log="",data=""))  
        self.VIPList.bind(sequence='<Double-Button-1>', func=self.handler_adaptor(self.handler, name="VIPList",item=self.VIPList,option="<Double-Button-1>",item_type="list",log="",data=""))  
        

class Application(Application_ui):
    def __init__(self, master=None):
        Application_ui.__init__(self, master)
        self.InitRuntime()
        self.InitUi()
       

    def InitRuntime(self,event=None):
        #runtime
        print("Initing >>>>>>")
        self.pLog("系统启动中>>>")
        self.loginName=""
        self.broadcastModel=""
        self.originalNickname=""
        self.customizedNickname=""
        self.customeReplaySettingsKeyworld=""
        self.customeReplaySettingsReply=""
        self.broadcaster=""
        self.delayPrint=False
        self.path=os.path.dirname(os.path.realpath(sys.argv[0]))
        print("Current Path:%s"%(self.path))
        self.configFilepath=self.path+"\\config.ini"
        print("ConfigFileCheck Path:%s"%(self.configFilepath))
        self.readVipsRank=False
        self.readFansRank=False
        self.readChatsList=False
        self.vipsList={}
        self.fansList={}
        self.chatList={}
        self.aLog("检测配置文件>>>")
        if os.path.exists(self.configFilepath):
            print("Config File inited")
            self.aLog("初始化配置文件>>>")
        else:
            print("Config File Missing CreatingPath...")
            # os.makedirs(self.configFilepath) 
            with open(self.configFilepath, 'w+', encoding='utf_8') as f:
                print("Config File Missing CreatingFile...")
                f.flush()
                f.close()
            print("Config File inited")
        self.aLog("读取配置文件>>>")
        #setting configuration
        self.roomId=config.read_config(self.configFilepath,"默认设置","roomId")
        self.path=str(self.roomId)+"-Settings"
        print("roomId :%s"%(self.roomId))     
        self.thanksShareStatus=str2Bool(config.read_config(self.configFilepath,self.path,"thanksShareStatus"))
        self.thanksOnTVGiftStatus=str2Bool(config.read_config(self.configFilepath,self.path,"thanksOnTVGiftStatus"))        
        self.thanksGiftStatus=str2Bool(config.read_config(self.configFilepath,self.path,"thanksGiftStatus"))        
        self.welcomeVipsStatus=str2Bool(config.read_config(self.configFilepath,self.path,"welcomeVipsStatus"))        
        self.welcomeFansStatus=str2Bool(config.read_config(self.configFilepath,self.path,"welcomeFansStatus"))        
        self.showWebViewerStatus=str2Bool(config.read_config(self.configFilepath,self.path,"showWebViewerStatus"))        
        self.thanksGiftValueYuan=str2Int(config.read_config(self.configFilepath,self.path,"thanksGiftValueYuan"))        
        self.welcomeVipsList=ast.literal_eval(str(config.read_config(self.configFilepath,self.path,"welcomeVipsList")))        
        self.welcomeFansList=ast.literal_eval(str(config.read_config(self.configFilepath,self.path,"welcomeFansList")))        
        self.welcomeVipsInfoFormartStr=config.read_config(self.configFilepath,self.path,"welcomeVipsInfoFormartStr")        
        self.thanksShareInfoFormartStr=config.read_config(self.configFilepath,self.path,"thanksShareInfoFormartStr")        
        self.startLotteryInfoFormartStr=config.read_config(self.configFilepath,self.path,"startLotteryInfoFormartStr")        
        self.thanksGiftInfoFormartStr=config.read_config(self.configFilepath,self.path,"thanksGiftInfoFormartStr")        
        self.scheduledInfo=config.read_config(self.configFilepath,self.path,"scheduledInfo")        
        self.scheduledInfoTime=config.read_config(self.configFilepath,self.path,"scheduledInfoTime")        
        self.customReplyList=json.loads(config.read_config(self.configFilepath,self.path,"customReplyList"))
        self.customeNicknameList=json.loads(config.read_config(self.configFilepath,self.path,"customeNicknameList"))     
        self.pLog("初始化参数>>>")
        
      
    def ReadRoomSettings(self,event=None):
        if self.roomId==0 or self.roomId=="0":
            pass
        else:
            CDKEY=config.read_config(self.configFilepath,self.roomId,"CD-KEY")
            if CDKEY=="" or len(str(CDKEY))<1:
                pass
            else:
                pass
            pass
        pass

    def InitUi(self,event=None):
        self.ThanksShareCheckVar.set('0')
        self.ThanksOnTVGiftCheckVar.set('0')
        self.ThanksGiftCheckVar.set('0')
        self.WelcomeVipsCheckVar.set('0')
        self.WelcomeFansCheckVar.set('0')
        self.ShowWebViewerCheckVar.set('0')
        self.VipsLevelOneCheckVar.set('0')
        self.VipsLevelTwoCheckVar.set('0')
        self.VipsLevelThreeCheckVar.set('0')
        self.VipsLevelFourCheckVar.set('0')
        self.VipsLevelFiveCheckVar.set('0')
        self.VipsLevelSixCheckVar.set('0')
        self.VipsLevelSevenCheckVar.set('0')
        self.FansLevelAllCheckVar.set('0')
        self.FansLevelOneCheckVar.set('0')
        self.FansLevelThreeCheckVar.set('0')
        self.FansLevelFiveCheckVar.set('0')
        self.FansLevelSevenCheckVar.set('0')
        self.FansLevelNineCheckVar.set('0')
        self.FansLevelElevenCheckVar.set('0')
        self.FansLevelPersonalizedCheckVar.set('0')
        self.ThanksGiftMoreThanInputVar.set(self.thanksGiftValueYuan)
        self.WelcomeVipsInfoFormartInputVar.set(self.welcomeVipsInfoFormartStr)
        self.ThanksShareInfoFormartInputVar.set(self.thanksShareInfoFormartStr)
        self.StartLotteryInfoFormartInputVar.set(self.startLotteryInfoFormartStr)
        self.ThanksGiftInfoFormartInputVar.set(self.thanksGiftInfoFormartStr)
        self.ScheduledInfoInputVar.set(self.scheduledInfo)
        self.ScheduledInfoTimeInputVar.set(self.scheduledInfoTime)
        if self.roomId==0 or self.roomId=="0":
            pass
        else:
            self.RomIdInputVar.set(self.roomId)
        if self.thanksShareStatus:
            self.ThanksShareCheckVar.set('1')
        if self.thanksOnTVGiftStatus:
            self.ThanksOnTVGiftCheckVar.set('1')
        if self.thanksGiftStatus:
            self.ThanksGiftCheckVar.set('1')
        if self.welcomeVipsStatus:
            self.WelcomeVipsCheckVar.set('1')
        if self.welcomeFansStatus:
            self.WelcomeFansCheckVar.set('1')
        if self.showWebViewerStatus:
            self.ShowWebViewerCheckVar.set('1')
        for vipslevel in self.welcomeVipsList:
            if vipslevel==1 or vipslevel=="1":
                self.VipsLevelOneCheckVar.set('1')
            if vipslevel==2 or vipslevel=="2":
                self.VipsLevelTwoCheckVar.set('1')
            if vipslevel==3 or vipslevel=="3":
                self.VipsLevelThreeCheckVar.set('1')
            if vipslevel==4 or vipslevel=="4":
                self.VipsLevelFourCheckVar.set('1')
            if vipslevel==5 or vipslevel=="5":
                self.VipsLevelFiveCheckVar.set('1')
            if vipslevel==6 or vipslevel=="6":
                self.VipsLevelSixCheckVar.set('1')
            if vipslevel==7 or vipslevel=="7":
                self.VipsLevelSevenCheckVar.set('1')
        if self.VipsLevelOneCheckVar.get()=='1' and self.VipsLevelTwoCheckVar.get()=='1' and self.VipsLevelThreeCheckVar.get()=='1'and self.VipsLevelFourCheckVar.get()=='1' and self.VipsLevelFiveCheckVar.get()=='1' and self.VipsLevelSixCheckVar.get()=='1' and self.VipsLevelSevenCheckVar.get()=='1':
            self.VipsLevelAllCheckVar.set(1)
        for fanslevel in self.welcomeFansList:
            if fanslevel==1 or fanslevel=="1":
                self.FansLevelOneCheckVar.set('1')
            if fanslevel==3 or fanslevel=="3":
                self.FansLevelThreeCheckVar.set('1')
            if fanslevel==5 or fanslevel=="5":
                self.FansLevelFiveCheckVar.set('1')
            if fanslevel==7 or fanslevel=="7":
                self.FansLevelSevenCheckVar.set('1')
            if fanslevel==9 or fanslevel=="9":
                self.FansLevelNineCheckVar.set('1')
            if fanslevel==11 or fanslevel=="11":
                self.FansLevelElevenCheckVar.set('1')
            if fanslevel=="Customer":
                self.FansLevelPersonalizedCheckVar.set('1')
            if  self.FansLevelAllCheckVar.get()=='1' and self.FansLevelOneCheckVar.get()=='1' and self.FansLevelThreeCheckVar.get()=='1' and self.FansLevelFiveCheckVar.get()=='1' and self.FansLevelSevenCheckVar.get()=='1' and self.FansLevelNineCheckVar.get()=='1'  and self.FansLevelElevenCheckVar.get()=='1' and self.FansLevelPersonalizedCheckVar.get()=='1':
                self.FansLevelAllCheckVar.set('1')
        self.CustomReplyList.delete(0,END)
        for customReplyKey in self.customReplyList.keys():
            customReplyData=str(customReplyKey)+">>>>>"+str(self.customReplyList[customReplyKey])
            self.CustomReplyList.insert(END,customReplyData)
            print(customReplyKey)
            pass
        self.NicknameList.delete(0,END)
        for customeNicknameKey in self.customeNicknameList.keys():
            customeNicknameData=str(customeNicknameKey)+">>>>>"+str(self.customeNicknameList[customeNicknameKey])
            self.NicknameList.insert(END,customeNicknameData)
            print(customeNicknameKey)
            pass
        for vipName in self.vipsList.keys():
            print(vipName)
            pass
        for fanName in self.fansList.keys():
            print(fanName)
            pass
        for chatNum in self.chatList.keys():
            print(chatNum)
            pass



    def reFreshUiData(self,event=None):
        print("data to reload")
        pass








    def CustomeScheduledSettingsSaveCommand_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def PauseRobotCommand_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def CloseRobotCommand_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def ResetAllSettingsCommand_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def StartRobotCommand_Cmd(self, event=None):
        self.LogInfoLable["text"]="启动机器人中,请稍候,开始检测登录账号>"
        d = threading.Thread(target=self.CheckLoginThenStartRobot)
        d.start()
        pass

    def UpdateAndFixCommand_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def LoginAdminAccountCommand_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def ExitRobotCommand_Cmd(self, event=None):
        self.LogInfoLable["text"]="保存设置中,请稍候>"
        d = threading.Thread(target=self.SaveAndExitPrograme)
        d.start()
        
        pass

    def CustomeReplaySettingsDeleteOrRestoreCommand_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def CustomeReplaySettingsAddOrModifyCommand_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def CustomizedNicknameAddOrModifyCommand_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def CustomizedNicknameDeleteOrRestorCommand_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def CheckLoginThenStartRobot(self,event=None):
        self.LogInfoLable["text"]="开始启动机器人,请稍候."
        self.delayPrint=True
        logT = threading.Thread(target=self.DelayLogPrint, args=(), name="CheckLoginThenStartRobotLog")
        logT.setDaemon(True) 
        logT.start()
        print("check account")
        time.sleep(15)
        self.LogInfoLable["text"]=self.LogInfoLable["text"]+"启动成功,设置中"
        time.sleep(15)
        self.delayPrint=False
        print("end process")
        time.sleep(9)
        if logT.isAlive():
            print("log is alive")
        else:
            print("log not alive")
        logT.join(1)
        print("CheckLoginThenStartRobot END")
        self.LogInfoLable["text"]=self.LogInfoLable["text"]+"启动完成"
    
    def SaveAndExitPrograme(self,event=None):
        self.delayPrint=True
        logT = threading.Thread(target=self.DelayLogPrint, args=(), name="CheckLoginThenStartRobotLog")
        logT.setDaemon(True) 
        logT.start()
        time.sleep(9)
        self.delayPrint=False
        time.sleep(3)
        logT.join(1)
        os._exit(1)

    def DelayLogPrint(self,event=None):
        while self.delayPrint:
            self.LogInfoLable["text"]=self.LogInfoLable["text"]+">"
            time.sleep(3)
        print("DelayLogPrint End")

    def CheckClickBindCommand(self,event=None):
        # .bind('<Button-1>',self.CheckClickBindCommand)
        pass

    def handler_adaptor(self, fun,  **kwds):
        return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)

    def handler(self, event, name, item,option,item_type,data,log):
        print("UI交互:控件["+name+"]类型["+item_type+"]操作["+option+"]数据["+str(data)+"]提示信息["+str(log)+"]")#logmax 133
        _log=log
        path=(str(self.RomIdInputVar.get())+"-Settings").replace("点击输入房间号","default")
        switch="尚未开启"        
        if item_type=="input":
            if option== '<Button-1>' and item.get()==data:
                if name=="ThanksShareInfoFormartInput" or name=="WelcomeVipsInfoFormartInput" or name=="StartLotteryInfoFormartInput" or name=="ThanksGiftInfoFormartInput":
                    pass
                else:
                    item.set("")
            if option== '<FocusOut>'and (str(item.get())=="" or item.get()==data or len(str(item.get()))<1 or item.get()==None):
                item.set(data)
            if name=="ThanksShareInfoFormartInput" and (option== '<KeyRelease>' or option=='<FocusOut>') :
                if self.ThanksShareCheckVar.get()=="1":
                    switch="已经开启"
                self.thanksShareInfoFormartStr=self.ThanksShareInfoFormartInputVar.get()
                config.write_config(self.configFilepath,path,"thanksShareInfoFormartStr",self.thanksShareInfoFormartStr)
                _log="您%s答谢分享功能,启动后按照格式答谢:>%s<   ,比如张三:  %s   如果测试数据有误请修改格式包含[切克闹]作为测试者关键字"%(switch,self.ThanksShareInfoFormartInputVar.get(),str(self.ThanksShareInfoFormartInputVar.get()).replace("切克闹","张三"))
            if name=="WelcomeVipsInfoFormartInput" and (option== '<KeyRelease>' or option=='<FocusOut>') :
                if self.WelcomeVipsCheckVar.get()=="1":
                    switch="已经开启"
                self.welcomeVipsInfoFormartStr=self.WelcomeVipsInfoFormartInputVar.get()
                config.write_config(self.configFilepath,path,"welcomeVipsInfoFormartStr",self.welcomeVipsInfoFormartStr)
                _log="您%s欢迎贵宾功能,启动后按照格式欢迎:>%s<   ,比如张三:  %s   如果测试数据有误请修改格式包含[切克闹]作为测试者关键字"%(switch,self.WelcomeVipsInfoFormartInputVar.get(),str(self.WelcomeVipsInfoFormartInputVar.get()).replace("切克闹","张三"))
            if name=="StartLotteryInfoFormartInput" and (option== '<KeyRelease>' or option=='<FocusOut>') :
                if self.ThanksOnTVGiftCheckVar.get()=="1":
                    switch="已经开启"
                self.startLotteryInfoFormartStr=self.StartLotteryInfoFormartInputVar.get()
                config.write_config(self.configFilepath,path,"startLotteryInfoFormartStr",self.startLotteryInfoFormartStr)
                _log="您%s答谢上电视功能,启动后按照格式开奖:>%s<   ,比如张三获得测试奖品:  %s   如果测试数据有误请修改格式包含[切克闹][奖品名称]作为测试者关键字"%(switch,self.StartLotteryInfoFormartInputVar.get(),str(self.StartLotteryInfoFormartInputVar.get()).replace("切克闹","张三").replace("奖品名称","一个测试奖品"))
            if name=="ThanksGiftInfoFormartInput" and (option== '<KeyRelease>' or option=='<FocusOut>') :
                if self.ThanksGiftCheckVar.get()=="1":
                    switch="已经开启"
                self.thanksGiftInfoFormartStr=self.ThanksGiftInfoFormartInputVar.get()
                config.write_config(self.configFilepath,path,"thanksGiftInfoFormartStr",self.thanksGiftInfoFormartStr)
                _log="您%s欢迎答谢礼品功能,启动后按照格式答谢:>%s<   ,比如张三送五个虎牙一号:  %s   如果测试数据有误请修改格式包含[切克闹][礼品名称][礼品数量]作为测试者关键字"%(switch,self.ThanksGiftInfoFormartInputVar.get(),str(self.ThanksGiftInfoFormartInputVar.get()).replace("切克闹","张三").replace("礼品名称","虎牙一号").replace("礼品数量","五连击"))
            if name=="RomIdInput" and (option== '<KeyRelease>' or option=='<FocusOut>') :
                self.roomId=self.RomIdInputVar.get()
                if option== '<KeyRelease>' :             
                    config.write_config(self.configFilepath,"默认设置","roomId",self.roomId)
                print("RomId is %s"%(self.roomId))
            if name=="ThanksGiftMoreThanInput" and (option== '<KeyRelease>' or option=='<FocusOut>') :
                try:
                    self.thanksGiftValueYuan=str(int(str(self.ThanksGiftMoreThanInputVar.get())))
                    config.write_config(self.configFilepath,path,"thanksGiftValueYuan",self.thanksGiftValueYuan)
                except Exception as e:
                    self.thanksGiftValueYuan="0"
                    config.write_config(self.configFilepath,path,"thanksGiftValueYuan",self.thanksGiftValueYuan)
                    print(e)
                    self.pLog("请输入正确的礼物价值数目,仅支持纯数字,请勿输入中文等其他字符...")
                print("thanksGiftValueYuan is %s"%(str(self.thanksGiftValueYuan)))
            if name=="ScheduledInfoTimeInput" and (option== '<KeyRelease>' or option=='<FocusOut>') :
                try:
                    self.scheduledInfoTime=str(int(self.ScheduledInfoTimeInputVar.get()))
                    config.write_config(self.configFilepath,path,"scheduledInfoTime",self.scheduledInfoTime)
                except Exception as e:
                    print(e)
                    self.scheduledInfoTime="5"
                    config.write_config(self.configFilepath,path,"scheduledInfoTime",self.scheduledInfoTime)
                    self.pLog("请输入正确的发言时间,仅支持纯数字,请勿输入中文等其他字符...")
                print("scheduledInfoTime is %s"%(str(self.scheduledInfoTime)))
            if name=="OriginalNicknameInput" and (option== '<KeyRelease>' or option=='<FocusOut>') :
                if self.OriginalNicknameInputVar.get()==data  or  self.OriginalNicknameInputVar.get()=="":
                    pass
                else:
                    self.originalNickname=self.OriginalNicknameInputVar.get()
            if name=="CustomizedNicknameInput" and (option== '<KeyRelease>' or option=='<FocusOut>'):
                if self.OriginalNicknameInputVar.get()==data or self.OriginalNicknameInputVar.get()=="":
                    pass
                else:
                    self.customizedNickname=self.OriginalNicknameInputVar.get()
            if name=="CustomeReplaySettingsKeyworldInput" and (option== '<KeyRelease>' or option=='<FocusOut>') :
                if self.OriginalNicknameInputVar.get()==data:
                    pass
                else:
                    self.customeReplaySettingsKeyworld=self.OriginalNicknameInputVar.get()
            if name=="CustomeReplaySettingsReplyInput" and (option== '<KeyRelease>' or option=='<FocusOut>') :
                if self.OriginalNicknameInputVar.get()==data:
                    pass
                else:
                    self.customeReplaySettingsReply=self.OriginalNicknameInputVar.get()
        if item_type=="check":
            if name=="ThanksShareCheck":
                if str(item.get())=="0":
                    self.thanksShareStatus=True
                    switch="已经开启"
                else:
                    self.thanksShareStatus=False
                _log="您%s答谢分享功能,启动后按照格式答谢:>%s<   ,比如张三:  %s   如果测试数据有误请修改格式包含[切克闹]作为测试者关键字"%(switch,self.ThanksShareInfoFormartInputVar.get(),str(self.ThanksShareInfoFormartInputVar.get()).replace("切克闹","张三"))
            if name=="ThanksOnTVGiftCheck":
                if str(item.get())=="0":
                    self.thanksOnTVGiftStatus=True
                    switch="已经开启"
                else:
                    self.thanksOnTVGiftStatus=False
                _log="您%s答谢上电视功能,启动后按照格式开奖:>%s<   ,比如张三获得测试奖品:  %s   如果测试数据有误请修改格式包含[切克闹][奖品名称]作为测试者关键字"%(switch,self.StartLotteryInfoFormartInputVar.get(),str(self.StartLotteryInfoFormartInputVar.get()).replace("切克闹","张三").replace("奖品名称","一个测试奖品"))
            if name=="ThanksGiftCheck":
                if str(item.get())=="0":
                    self.thanksGiftStatus=True
                    switch="已经开启"
                else:
                    self.thanksGiftStatus=False
                _log="您%s欢迎答谢礼品功能,启动后按照格式答谢:>%s<   ,比如张三送五个虎牙一号:  %s   如果测试数据有误请修改格式包含[切克闹][礼品名称][礼品数量]作为测试者关键字"%(switch,self.ThanksGiftInfoFormartInputVar.get(),str(self.ThanksGiftInfoFormartInputVar.get()).replace("切克闹","张三").replace("礼品名称","虎牙一号").replace("礼品数量","五连击"))          
            if name=="WelcomeVipsCheck":
                if str(item.get())=="0":
                    self.welcomeVipsStatus=True
                    switch="已经开启"
                else:
                    self.welcomeVipsStatus=False
                _log="您%s欢迎贵宾功能,启动后按照格式欢迎:>%s<   ,比如张三:  %s   如果测试数据有误请修改格式包含[切克闹]作为测试者关键字"%(switch,self.WelcomeVipsInfoFormartInputVar.get(),str(self.WelcomeVipsInfoFormartInputVar.get()).replace("切克闹","张三"))           
            if name=="WelcomeFansCheck":
                if str(item.get())=="0":
                    self.welcomeFansStatus=True
                    switch="已经开启"
                else:
                    self.welcomeFansStatus=False
                _log="您%s欢迎粉丝功能,启动后按照格式欢迎:>%s<   ,比如张三:  %s   如果测试数据有误请修改格式包含[切克闹]作为测试者关键字"%(switch,self.WelcomeVipsInfoFormartInputVar.get(),str(self.WelcomeVipsInfoFormartInputVar.get()).replace("切克闹","张三"))        
            if name=="FansLevelOneCheck":
                if str(item.get())=="0" :
                    if self.WelcomeFansCheckVar.get()=="1":
                        switch="已经开启"
                        self.welcomeFansList.append('1')
                else:
                    if self.welcomeFansList.count('1')>0:
                        self.welcomeFansList.remove('1')
                    self.FansLevelAllCheckVar.set('0')
                _log="您%s欢迎%s粉丝的功能,启动后按照格式欢迎:>%s<   ,比如张三:  %s   如果测试数据有误请修改格式包含[切克闹]作为测试者关键字"%(switch,data,self.WelcomeVipsInfoFormartInputVar.get(),str(self.WelcomeVipsInfoFormartInputVar.get()).replace("切克闹","张三"))        
            if name=="FansLevelThreeCheck":
                if str(item.get())=="0" :
                    if self.WelcomeFansCheckVar.get()=="1":
                        switch="已经开启"
                        self.welcomeFansList.append('3')
                else:
                    if self.welcomeFansList.count('3')>0:
                        self.welcomeFansList.remove('3')
                    self.FansLevelAllCheckVar.set('0')
                _log="您%s欢迎%s粉丝的功能,启动后按照格式欢迎:>%s<   ,比如张三:  %s   如果测试数据有误请修改格式包含[切克闹]作为测试者关键字"%(switch,data,self.WelcomeVipsInfoFormartInputVar.get(),str(self.WelcomeVipsInfoFormartInputVar.get()).replace("切克闹","张三"))        
            if name=="FansLevelFiveCheck" :
                if str(item.get())=="0":
                    if self.WelcomeFansCheckVar.get()=="1":
                        switch="已经开启"
                        self.welcomeFansList.append('5')
                else:
                    if self.welcomeFansList.count('5')>0:
                        self.welcomeFansList.remove('5')
                    self.FansLevelAllCheckVar.set('0')
                _log="您%s欢迎%s粉丝的功能,启动后按照格式欢迎:>%s<   ,比如张三:  %s   如果测试数据有误请修改格式包含[切克闹]作为测试者关键字"%(switch,data,self.WelcomeVipsInfoFormartInputVar.get(),str(self.WelcomeVipsInfoFormartInputVar.get()).replace("切克闹","张三"))        
            if name=="FansLevelSevenCheck" :
                if str(item.get())=="0":
                    if self.WelcomeFansCheckVar.get()=="1":
                        switch="已经开启"
                        self.welcomeFansList.append('7')
                else:
                    if self.welcomeFansList.count('7')>0:
                        self.welcomeFansList.remove('7')
                    self.FansLevelAllCheckVar.set('0')
                _log="您%s欢迎%s粉丝的功能,启动后按照格式欢迎:>%s<   ,比如张三:  %s   如果测试数据有误请修改格式包含[切克闹]作为测试者关键字"%(switch,data,self.WelcomeVipsInfoFormartInputVar.get(),str(self.WelcomeVipsInfoFormartInputVar.get()).replace("切克闹","张三"))        
            if name=="FansLevelNineCheck" :
                if str(item.get())=="0":
                    if self.WelcomeFansCheckVar.get()=="1":
                        switch="已经开启"
                        self.welcomeFansList.append('9')
                else:
                    if self.welcomeFansList.count('9')>0:
                        self.welcomeFansList.remove('9')
                    self.FansLevelAllCheckVar.set('0')
                _log="您%s欢迎%s粉丝的功能,启动后按照格式欢迎:>%s<   ,比如张三:  %s   如果测试数据有误请修改格式包含[切克闹]作为测试者关键字"%(switch,data,self.WelcomeVipsInfoFormartInputVar.get(),str(self.WelcomeVipsInfoFormartInputVar.get()).replace("切克闹","张三"))        
            if name=="FansLevelElevenCheck" :
                if str(item.get())=="0":
                    if self.WelcomeFansCheckVar.get()=="1":
                        switch="已经开启"
                        self.welcomeFansList.append('11')
                else:
                    if self.welcomeFansList.count('11')>0:
                        self.welcomeFansList.remove('11')
                    self.FansLevelAllCheckVar.set('0')
                _log="您%s欢迎%s粉丝的功能,启动后按照格式欢迎:>%s<   ,比如张三:  %s   如果测试数据有误请修改格式包含[切克闹]作为测试者关键字"%(switch,data,self.WelcomeVipsInfoFormartInputVar.get(),str(self.WelcomeVipsInfoFormartInputVar.get()).replace("切克闹","张三"))        
            if name=="FansLevelAllCheck":
                if str(item.get())=="0":
                    if self.WelcomeFansCheckVar.get()=="1":
                        switch="已经开启"
                    self.FansLevelOneCheckVar.set('1')
                    self.FansLevelThreeCheckVar.set('1')
                    self.FansLevelFiveCheckVar.set('1')
                    self.FansLevelSevenCheckVar.set('1')
                    self.FansLevelNineCheckVar.set('1')
                    self.FansLevelElevenCheckVar.set('1')
                    self.FansLevelPersonalizedCheckVar.set('1')
                    self.fansList=['1','3','5','7','9','11','Customer']
                else:
                    self.FansLevelOneCheckVar.set('0')
                    self.FansLevelThreeCheckVar.set('0')
                    self.FansLevelFiveCheckVar.set('0')
                    self.FansLevelSevenCheckVar.set('0')
                    self.FansLevelNineCheckVar.set('0')
                    self.FansLevelElevenCheckVar.set('0')
                    self.FansLevelPersonalizedCheckVar.set('0')
                    self.fansList=[]
            if name=="FansLevelPersonalizedCheck":
                if str(item.get())=="0":
                    if self.WelcomeFansCheckVar.get()=="1":
                        switch="已经开启"
                        self.welcomeFansList.append('Customer')
                else:
                    if self.welcomeFansList.count('Customer')>0:
                        self.welcomeFansList.remove('Customer')
                    self.FansLevelAllCheckVar.set('0')
                _log="您%s欢迎%s粉丝的功能,启动后按照格式欢迎:>%s<   ,比如张三:  %s   如果测试数据有误请修改格式包含[切克闹]作为测试者关键字"%(switch,data,self.WelcomeVipsInfoFormartInputVar.get(),str(self.WelcomeVipsInfoFormartInputVar.get()).replace("切克闹","张三"))
            if name=="VipsLevelOneCheck":
                if str(item.get())=="0":
                    if self.WelcomeVipsCheckVar.get()=="1":
                        switch="已经开启"
                        self.welcomeVipsList.append('1')
                else:
                    if self.welcomeVipsList.count('1')>0:
                        self.welcomeVipsList.remove('1')
                    self.VipsLevelAllCheckVar.set('0')
                _log="您%s欢迎%s粉丝的功能,启动后按照格式欢迎:>%s<   ,比如张三:  %s   如果测试数据有误请修改格式包含[切克闹]作为测试者关键字"%(switch,data,self.WelcomeVipsInfoFormartInputVar.get(),str(self.WelcomeVipsInfoFormartInputVar.get()).replace("切克闹","张三"))
            if name=="VipsLevelTwoCheck":
                if str(item.get())=="0":
                    if self.WelcomeVipsCheckVar.get()=="1":
                        switch="已经开启"
                        self.welcomeVipsList.append('2')
                else:
                    if self.welcomeVipsList.count('2')>0:
                        self.welcomeVipsList.remove('2')
                    self.VipsLevelAllCheckVar.set('0')
                _log="您%s欢迎%s粉丝的功能,启动后按照格式欢迎:>%s<   ,比如张三:  %s   如果测试数据有误请修改格式包含[切克闹]作为测试者关键字"%(switch,data,self.WelcomeVipsInfoFormartInputVar.get(),str(self.WelcomeVipsInfoFormartInputVar.get()).replace("切克闹","张三"))
            if name=="VipsLevelThreeCheck":
                if str(item.get())=="0":
                    if self.WelcomeVipsCheckVar.get()=="1":
                        switch="已经开启"
                        self.welcomeVipsList.append('3')
                else:
                    if self.welcomeVipsList.count('3')>0:
                        self.welcomeVipsList.remove('3')
                    self.VipsLevelAllCheckVar.set('0')
                _log="您%s欢迎%s粉丝的功能,启动后按照格式欢迎:>%s<   ,比如张三:  %s   如果测试数据有误请修改格式包含[切克闹]作为测试者关键字"%(switch,data,self.WelcomeVipsInfoFormartInputVar.get(),str(self.WelcomeVipsInfoFormartInputVar.get()).replace("切克闹","张三"))           
            if name=="VipsLevelFourCheck":
                if str(item.get())=="0":
                    if self.WelcomeVipsCheckVar.get()=="1":
                        switch="已经开启"
                        self.welcomeVipsList.append('4')
                else:
                    if self.welcomeVipsList.count('4')>0:
                        self.welcomeVipsList.remove('4')
                    self.VipsLevelAllCheckVar.set('0')
                _log="您%s欢迎%s粉丝的功能,启动后按照格式欢迎:>%s<   ,比如张三:  %s   如果测试数据有误请修改格式包含[切克闹]作为测试者关键字"%(switch,data,self.WelcomeVipsInfoFormartInputVar.get(),str(self.WelcomeVipsInfoFormartInputVar.get()).replace("切克闹","张三"))          
            if name=="VipsLevelFiveCheck":
                if str(item.get())=="0":
                    if self.WelcomeVipsCheckVar.get()=="1":
                        switch="已经开启"
                        self.welcomeVipsList.append('5')
                else:
                    if self.welcomeVipsList.count('5')>0:
                        self.welcomeVipsList.remove('5')
                    self.VipsLevelAllCheckVar.set('0')
                _log="您%s欢迎%s粉丝的功能,启动后按照格式欢迎:>%s<   ,比如张三:  %s   如果测试数据有误请修改格式包含[切克闹]作为测试者关键字"%(switch,data,self.WelcomeVipsInfoFormartInputVar.get(),str(self.WelcomeVipsInfoFormartInputVar.get()).replace("切克闹","张三"))
            if name=="VipsLevelSixCheck":
                if str(item.get())=="0":
                    if self.WelcomeVipsCheckVar.get()=="1":
                        switch="已经开启"
                        self.welcomeVipsList.append('6')
                else:
                    if self.welcomeVipsList.count('6')>0:
                        self.welcomeVipsList.remove('6')
                    self.VipsLevelAllCheckVar.set('0')
                _log="您%s欢迎%s粉丝的功能,启动后按照格式欢迎:>%s<   ,比如张三:  %s   如果测试数据有误请修改格式包含[切克闹]作为测试者关键字"%(switch,data,self.WelcomeVipsInfoFormartInputVar.get(),str(self.WelcomeVipsInfoFormartInputVar.get()).replace("切克闹","张三"))
            if name=="VipsLevelSevenCheck":
                if str(item.get())=="0":
                    if self.WelcomeVipsCheckVar.get()=="1":
                        switch="已经开启"
                        self.welcomeVipsList.append('7')
                else:
                    if self.welcomeVipsList.count('7')>0:
                        self.welcomeVipsList.remove('7')
                    self.VipsLevelAllCheckVar.set('0')
                _log="您%s欢迎%s粉丝的功能,启动后按照格式欢迎:>%s<   ,比如张三:  %s   如果测试数据有误请修改格式包含[切克闹]作为测试者关键字"%(switch,data,self.WelcomeVipsInfoFormartInputVar.get(),str(self.WelcomeVipsInfoFormartInputVar.get()).replace("切克闹","张三"))
            if name=="VipsLevelAllCheck":
                if str(item.get())=="0":
                    if self.WelcomeVipsCheckVar.get()=="1":
                        switch="已经开启"
                        self.vipsList=['1','2','3','4','5','6','7']
                    self.VipsLevelOneCheckVar.set('1')
                    self.VipsLevelTwoCheckVar.set('1')
                    self.VipsLevelThreeCheckVar.set('1')
                    self.VipsLevelFourCheckVar.set('1')
                    self.VipsLevelFiveCheckVar.set('1')
                    self.VipsLevelSixCheckVar.set('1')
                    self.VipsLevelSevenCheckVar.set('1')
                else:
                    self.VipsLevelOneCheckVar.set('0')
                    self.VipsLevelTwoCheckVar.set('0')
                    self.VipsLevelThreeCheckVar.set('0')
                    self.VipsLevelFourCheckVar.set('0')
                    self.VipsLevelFiveCheckVar.set('0')
                    self.VipsLevelSixCheckVar.set('0')
                    self.VipsLevelSevenCheckVar.set('0')
                    self.vipsList.clear()

                _log="您%s欢迎%s粉丝的功能,启动后按照格式欢迎:>%s<   ,比如张三:  %s   如果测试数据有误请修改格式包含[切克闹]作为测试者关键字"%(switch,data,self.WelcomeVipsInfoFormartInputVar.get(),str(self.WelcomeVipsInfoFormartInputVar.get()).replace("切克闹","张三"))
            if name=="ShowWebViewerCheck":
                if str(item.get())=="0":
                    switch="已经开启"
                    self.showWebViewerStatus=True
                else:
                    self.showWebViewerStatus=False
                self.FansLevelAllCheckVar.set('0')
                _log="您%s显示监控画面的功能,您若关闭监控画面,则机器人也相应会一起中断,若您不想显示监控画面时请勿勾选此选项."%(switch)
        if item_type=="command" and option== '<Button-1>' :
            if name=="CustomizedNicknameAddOrModifyCommand":
                print("Try to add a New Option Nickname:[%s] CustomeName:[%s]"%(self.OriginalNicknameInputVar.get(),self.CustomizedNicknameInputVar.get()))
                path=self.RomIdInputVar.get()+"-NicknameSetting"
                if (self.RomIdInputVar.get()=="点击输入房间号"):
                    path="default-NicknameSetting"
                if config.write_config(self.configFilepath,path,self.OriginalNicknameInputVar.get(),self.CustomizedNicknameInputVar.get()):
                    self.reFreshUiData()
            pass
        # self.StartRobotButton.config(state="NORMAL")
        if item_type=="list" and option== '<Double-Button-1>' :
            if name=="NicknameList":
                select_index=self.NicknameList.curselection()[0]
                select_value=self.NicknameList.get(select_index)
                key=str(select_value).split(">>>>>")[0]
                value=str(select_value).split(">>>>>")[1]
                self.OriginalNicknameInputVar.set(key)
                self.CustomizedNicknameInputVar.set(value)
            if name=="CustomReplyList":
                select_index=self.CustomReplyList.curselection()[0]
                select_value=self.CustomReplyList.get(select_index)
                key=str(select_value).split(">>>>>")[0]
                value=str(select_value).split(">>>>>")[1]
                self.CustomeReplaySettingsKeyworldInputVar.set(key)
                self.CustomeReplaySettingsReplyInputVar.set(value)
 
            if name=="VIPList":
                pass
            if name=="FansList":
                pass
            if name=="ChatsList":
                pass
            pass    
        self.pLog(_log)

    def pLog(self,_log,event=None):
        if str(_log)=="" or len(str(_log))<1:
            pass
        else:
            self.LogInfoLable['text']=_log

    def aLog(self,_log,event=None):
        if str(_log)=="" or len(str(_log))<1:
            pass
        else:
            if len(self.LogInfoLable['text'])>133:
                self.LogInfoLable['text']="...>>>>>"
            self.LogInfoLable['text']=self.LogInfoLable['text']+_log

def str2Bool(str):
    if str==None or str=="":
        return False
    return str.lower() in ("yes","true","t","1")

def str2Int(str):
    if str==None or str=="":
        return 0
    return int(str)

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    try: top.destroy()
    except: pass
