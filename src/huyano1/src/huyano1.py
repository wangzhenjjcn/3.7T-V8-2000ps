#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
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
        self.style.configure('VipsLevelAllCheck.TCheckbutton',font=('宋体',9))
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
        self.CopyRightLabel1 = Label(self.Main, text='CopyRight@ 2020 WangZhen <wangzhenjjcn@gmail.com> myazure.org', style='CopyRightLabel1.TLabel')
        self.CopyRightLabel1.place(relx=0.759, rely=0.959, relwidth=0.227, relheight=0.031)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

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
        #TODO, Please finish the function here!
        pass

    def UpdateAndFixCommand_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def LoginAdminAccountCommand_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def ExitRobotCommand_Cmd(self, event=None):
        #TODO, Please finish the function here!
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

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    try: top.destroy()
    except: pass
