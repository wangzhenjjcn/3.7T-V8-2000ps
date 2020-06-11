VERSION 5.00
Begin VB.Form 虎牙切克闹 
   Caption         =   "虎牙机器人(切克闹)主程序-版本1.0"
   ClientHeight    =   12060
   ClientLeft      =   120
   ClientTop       =   600
   ClientWidth     =   25485
   LinkTopic       =   "Form1"
   MousePointer    =   1  'Arrow
   ScaleHeight     =   12060
   ScaleWidth      =   25485
   Begin VB.Frame Main 
      Caption         =   "程序设置"
      Height          =   12015
      Left            =   0
      TabIndex        =   0
      Top             =   0
      Width           =   25455
      Begin VB.Frame CustomeScheduledSettingsFrame 
         Caption         =   "定时发言"
         Height          =   2535
         Left            =   20280
         TabIndex        =   57
         Top             =   8760
         Width           =   4935
         Begin VB.CommandButton CustomeScheduledSettingsSaveCommand 
            Caption         =   "保存/应用"
            Height          =   375
            Left            =   3480
            TabIndex        =   80
            Top             =   360
            Width           =   1095
         End
         Begin VB.TextBox ScheduledInfoTimeInput 
            Alignment       =   2  'Center
            BeginProperty DataFormat 
               Type            =   1
               Format          =   "0"
               HaveTrueFalseNull=   0
               FirstDayOfWeek  =   0
               FirstWeekOfYear =   0
               LCID            =   2052
               SubFormatType   =   1
            EndProperty
            Height          =   270
            Left            =   3240
            TabIndex        =   61
            Text            =   "5"
            Top             =   1920
            Width           =   1335
         End
         Begin VB.TextBox ScheduledInfoInput 
            Height          =   735
            Left            =   360
            TabIndex        =   59
            Top             =   840
            Width           =   4215
         End
         Begin VB.Label ScheduledInfoTimeLable 
            AutoSize        =   -1  'True
            Caption         =   "发言时间(每X分钟一次):"
            Height          =   300
            Left            =   240
            TabIndex        =   60
            Top             =   1920
            Width           =   2340
         End
         Begin VB.Label ScheduledInfoLabel 
            AutoSize        =   -1  'True
            Caption         =   "发言内容:"
            Height          =   300
            Left            =   120
            TabIndex        =   58
            Top             =   360
            Width           =   1290
         End
      End
      Begin VB.Frame WebInfoFrame 
         Caption         =   "房间信息"
         Height          =   10455
         Left            =   6960
         TabIndex        =   46
         Top             =   840
         Width           =   13095
         Begin VB.ListBox VIPList 
            Height          =   9060
            ItemData        =   "虎牙切克闹.frx":0000
            Left            =   360
            List            =   "虎牙切克闹.frx":0007
            TabIndex        =   51
            Top             =   960
            Width           =   2295
         End
         Begin VB.ListBox FansList 
            Height          =   9060
            ItemData        =   "虎牙切克闹.frx":001D
            Left            =   2760
            List            =   "虎牙切克闹.frx":0024
            TabIndex        =   50
            Top             =   960
            Width           =   2295
         End
         Begin VB.ListBox ChatsList 
            Height          =   9060
            ItemData        =   "虎牙切克闹.frx":003A
            Left            =   5160
            List            =   "虎牙切克闹.frx":0041
            TabIndex        =   49
            Top             =   960
            Width           =   5055
         End
         Begin VB.ListBox NicknameList 
            Height          =   4020
            ItemData        =   "虎牙切克闹.frx":0057
            Left            =   10320
            List            =   "虎牙切克闹.frx":005E
            TabIndex        =   48
            Top             =   960
            Width           =   2295
         End
         Begin VB.ListBox CustomReplyList 
            Height          =   4020
            ItemData        =   "虎牙切克闹.frx":0066
            Left            =   10320
            List            =   "虎牙切克闹.frx":006D
            TabIndex        =   47
            Top             =   6000
            Width           =   2295
         End
         Begin VB.Label WebVipsLable 
            AutoSize        =   -1  'True
            Caption         =   "贵宾席:"
            Height          =   300
            Left            =   360
            TabIndex        =   56
            Top             =   480
            Width           =   1095
         End
         Begin VB.Label WebFansLable 
            AutoSize        =   -1  'True
            Caption         =   "粉丝席:"
            Height          =   300
            Left            =   2760
            TabIndex        =   55
            Top             =   480
            Width           =   1335
         End
         Begin VB.Label WebChatsLable 
            AutoSize        =   -1  'True
            Caption         =   "公屏:"
            Height          =   300
            Left            =   5160
            TabIndex        =   54
            Top             =   480
            Width           =   930
         End
         Begin VB.Label NicknameLable 
            AutoSize        =   -1  'True
            Caption         =   "自定义昵称:"
            Height          =   300
            Left            =   10320
            TabIndex        =   53
            Top             =   480
            Width           =   1575
         End
         Begin VB.Label CustomReplyLabel 
            AutoSize        =   -1  'True
            Caption         =   "自定义回复:"
            Height          =   420
            Left            =   10320
            TabIndex        =   52
            Top             =   5400
            Width           =   1575
         End
      End
      Begin VB.Frame Frame2 
         Caption         =   "机器人设置"
         Height          =   10935
         Left            =   120
         TabIndex        =   20
         Top             =   360
         Width           =   4335
         Begin VB.CheckBox Check1 
            Caption         =   "答谢上电视礼物"
            Height          =   255
            Left            =   1800
            TabIndex        =   83
            Top             =   2400
            Width           =   1575
         End
         Begin VB.TextBox ThanksGiftMoreThanInput 
            Height          =   270
            Left            =   2520
            TabIndex        =   77
            Text            =   "0"
            Top             =   2880
            Width           =   735
         End
         Begin VB.TextBox ThanksGiftInfoFormartInput 
            Height          =   375
            Left            =   360
            TabIndex        =   69
            Text            =   "谢谢[心动]切克闹[送花]的1314个虎牙一号"
            Top             =   10440
            Width           =   3735
         End
         Begin VB.TextBox StartLotteryInfoFormartInput 
            Height          =   375
            Left            =   360
            TabIndex        =   67
            Text            =   "奖品:[心动]【奖品名称】[心动]走一波[心动]"
            Top             =   9240
            Width           =   3735
         End
         Begin VB.TextBox ThanksShareInfoFormartInput 
            Height          =   375
            Left            =   360
            TabIndex        =   65
            Text            =   "谢谢[送花]切克闹[送花]分享直播间"
            Top             =   8040
            Width           =   3735
         End
         Begin VB.TextBox WelcomeVipsInfoFormartInput 
            Height          =   375
            Left            =   360
            TabIndex        =   63
            Text            =   "欢迎[送花]切克闹[送花]"
            Top             =   6840
            Width           =   3735
         End
         Begin VB.TextBox RomIdInput 
            Height          =   375
            Left            =   1800
            TabIndex        =   42
            Text            =   "点击输入房间号"
            Top             =   360
            Width           =   2175
         End
         Begin VB.CheckBox ShowWebViewerCheck 
            Caption         =   "显示直播画面(需要重启机器人)"
            Height          =   375
            Left            =   120
            TabIndex        =   41
            Top             =   5760
            Width           =   2895
         End
         Begin VB.CheckBox ThanksGiftCheck 
            Caption         =   "答谢礼物"
            Height          =   255
            Left            =   120
            TabIndex        =   40
            Top             =   2880
            Width           =   1575
         End
         Begin VB.CheckBox ThanksShareCheck 
            Caption         =   "答谢分享"
            Height          =   255
            Left            =   120
            TabIndex        =   39
            Top             =   2400
            Width           =   1575
         End
         Begin VB.CheckBox WelcomeVipsCheck 
            Caption         =   "欢迎贵宾"
            Height          =   255
            Left            =   120
            TabIndex        =   38
            Top             =   3480
            Width           =   1095
         End
         Begin VB.CheckBox WelcomeFansCheck 
            Caption         =   "欢迎粉丝"
            Height          =   255
            Left            =   120
            TabIndex        =   37
            Top             =   4680
            Width           =   1095
         End
         Begin VB.CheckBox VipsLevelOneCheck 
            Caption         =   "剑士"
            Height          =   255
            Left            =   1440
            TabIndex        =   36
            Top             =   3480
            Width           =   735
         End
         Begin VB.CheckBox VipsLevelTwoCheck 
            Caption         =   "骑士"
            Height          =   255
            Left            =   2760
            TabIndex        =   35
            Top             =   3480
            Width           =   735
         End
         Begin VB.CheckBox VipsLevelThreeCheck 
            Caption         =   "领主"
            Height          =   255
            Left            =   1440
            TabIndex        =   34
            Top             =   3720
            Width           =   735
         End
         Begin VB.CheckBox VipsLevelFourCheck 
            Caption         =   "公爵"
            Height          =   255
            Left            =   2760
            TabIndex        =   33
            Top             =   3720
            Width           =   735
         End
         Begin VB.CheckBox VipsLevelFiveCheck 
            Caption         =   "君王"
            Height          =   255
            Left            =   1440
            TabIndex        =   32
            Top             =   3960
            Width           =   735
         End
         Begin VB.CheckBox VipsLevelSixCheck 
            Caption         =   "帝皇"
            Height          =   255
            Left            =   2760
            TabIndex        =   31
            Top             =   3960
            Width           =   735
         End
         Begin VB.CheckBox VipsLevelSevenCheck 
            Caption         =   "超神"
            Height          =   375
            Left            =   1440
            TabIndex        =   30
            Top             =   4200
            Width           =   735
         End
         Begin VB.CheckBox VipsLevelAllCheck 
            Caption         =   "欢迎所有"
            Height          =   375
            Left            =   2760
            TabIndex        =   29
            Top             =   4200
            Width           =   1095
         End
         Begin VB.CheckBox FansLevelOneCheck 
            Caption         =   "一级"
            Height          =   255
            Left            =   1440
            TabIndex        =   28
            Top             =   4680
            Width           =   735
         End
         Begin VB.CheckBox FansLevelThreeCheck 
            Caption         =   "三级"
            Height          =   255
            Left            =   2760
            TabIndex        =   27
            Top             =   4680
            Width           =   735
         End
         Begin VB.CheckBox FansLevelFiveCheck 
            Caption         =   "五级"
            Height          =   255
            Left            =   1440
            TabIndex        =   26
            Top             =   4920
            Width           =   735
         End
         Begin VB.CheckBox FansLevelSevenCheck 
            Caption         =   "七级"
            Height          =   255
            Left            =   2760
            TabIndex        =   25
            Top             =   4920
            Width           =   735
         End
         Begin VB.CheckBox FansLevelNineCheck 
            Caption         =   "九级"
            Height          =   255
            Left            =   1440
            TabIndex        =   24
            Top             =   5160
            Width           =   735
         End
         Begin VB.CheckBox FansLevelElevenCheck 
            Caption         =   "十一级"
            Height          =   255
            Left            =   2760
            TabIndex        =   23
            Top             =   5160
            Width           =   975
         End
         Begin VB.CheckBox FansLevelAllCheck 
            Caption         =   "所有"
            Height          =   375
            Left            =   1440
            TabIndex        =   22
            Top             =   5400
            Width           =   735
         End
         Begin VB.CheckBox FansLevelPersonalizedCheck 
            Caption         =   "自定义"
            Height          =   375
            Left            =   2760
            TabIndex        =   21
            Top             =   5400
            Width           =   1335
         End
         Begin VB.Label ThanksGiftMoreThanUnitLable 
            Caption         =   "元"
            Height          =   375
            Left            =   3480
            TabIndex        =   79
            Top             =   2880
            Width           =   495
         End
         Begin VB.Label ThanksGiftMoreThanLable 
            Caption         =   "大于:"
            Height          =   375
            Left            =   1800
            TabIndex        =   78
            Top             =   2880
            Width           =   495
         End
         Begin VB.Label BroadcastModelText 
            AutoSize        =   -1  'True
            Caption         =   "启动后显示"
            Height          =   300
            Left            =   1800
            TabIndex        =   76
            Top             =   1920
            Width           =   2100
         End
         Begin VB.Label BroadcastModelLabel 
            AutoSize        =   -1  'True
            Caption         =   "直播模式:"
            Height          =   300
            Left            =   120
            TabIndex        =   75
            Top             =   1920
            Width           =   1410
         End
         Begin VB.Line Line2 
            X1              =   0
            X2              =   4320
            Y1              =   6240
            Y2              =   6240
         End
         Begin VB.Line Line1 
            X1              =   0
            X2              =   4320
            Y1              =   2280
            Y2              =   2280
         End
         Begin VB.Label PodcastNameText 
            AutoSize        =   -1  'True
            Caption         =   "启动后显示"
            Height          =   300
            Left            =   1800
            TabIndex        =   71
            Top             =   960
            Width           =   2100
         End
         Begin VB.Label PodcastNameLable 
            AutoSize        =   -1  'True
            Caption         =   "主播名称:"
            Height          =   255
            Left            =   120
            TabIndex        =   70
            Top             =   960
            Width           =   1215
         End
         Begin VB.Label ThanksGiftInfoFormartLable 
            AutoSize        =   -1  'True
            Caption         =   "答谢礼物信息格式:"
            Height          =   300
            Left            =   120
            TabIndex        =   68
            Top             =   9960
            Width           =   1530
         End
         Begin VB.Label StartLotteryInfoFormartLable 
            AutoSize        =   -1  'True
            Caption         =   "开始抽奖信息格式:"
            Height          =   300
            Left            =   120
            TabIndex        =   66
            Top             =   8760
            Width           =   1530
         End
         Begin VB.Label ThanksShareInfoFormartLable 
            AutoSize        =   -1  'True
            Caption         =   "感谢分享信息格式:"
            Height          =   300
            Left            =   120
            TabIndex        =   64
            Top             =   7560
            Width           =   1530
         End
         Begin VB.Label WelcomeVipsInfoFormartLable 
            AutoSize        =   -1  'True
            Caption         =   "贵宾欢迎信息格式:"
            Height          =   300
            Left            =   120
            TabIndex        =   62
            Top             =   6360
            Width           =   1530
         End
         Begin VB.Label RoomIdLable 
            AutoSize        =   -1  'True
            Caption         =   "房间号:"
            Height          =   255
            Left            =   120
            TabIndex        =   45
            Top             =   480
            Width           =   1215
         End
         Begin VB.Label UserNicknameLabel 
            AutoSize        =   -1  'True
            Caption         =   "房管账号:"
            Height          =   255
            Left            =   120
            TabIndex        =   44
            Top             =   1440
            Width           =   1215
         End
         Begin VB.Label UserNicknameText 
            AutoSize        =   -1  'True
            Caption         =   "登陆后显示"
            Height          =   255
            Left            =   1800
            TabIndex        =   43
            Top             =   1440
            Width           =   2055
         End
      End
      Begin VB.Frame RobotOperationFrame 
         Caption         =   "机器人操作"
         Height          =   10455
         Left            =   4560
         TabIndex        =   15
         Top             =   840
         Width           =   2295
         Begin VB.CommandButton PauseRobotCommand 
            Caption         =   "暂停机器人"
            Height          =   495
            Left            =   360
            TabIndex        =   82
            Top             =   3120
            Width           =   1575
         End
         Begin VB.CommandButton CloseRobotCommand 
            Caption         =   "关闭机器人"
            Height          =   495
            Left            =   360
            TabIndex        =   81
            Top             =   3960
            Width           =   1575
         End
         Begin VB.CommandButton ResetAllSettingsCommand 
            Caption         =   "重置所有设置"
            Height          =   495
            Left            =   360
            TabIndex        =   72
            Top             =   2280
            Width           =   1575
         End
         Begin VB.CommandButton StartRobotCommand 
            Caption         =   "启动机器人"
            Height          =   495
            Left            =   360
            TabIndex        =   19
            Top             =   600
            Width           =   1575
         End
         Begin VB.CommandButton UpdateAndFixCommand 
            Caption         =   "更新及修复"
            Height          =   495
            Left            =   360
            TabIndex        =   18
            Top             =   9600
            Width           =   1575
         End
         Begin VB.CommandButton LoginAdminAccountCommand 
            Caption         =   "登录房管账号"
            Height          =   495
            Left            =   360
            TabIndex        =   17
            Top             =   1440
            Width           =   1575
         End
         Begin VB.CommandButton ExitRobotCommand 
            Caption         =   "退出机器人"
            Height          =   495
            Left            =   360
            TabIndex        =   16
            Top             =   8760
            Width           =   1575
         End
      End
      Begin VB.Frame CustomeReplaySettingsFrame 
         Caption         =   "自定义回复设置"
         Height          =   3855
         Left            =   20280
         TabIndex        =   8
         Top             =   4800
         Width           =   4815
         Begin VB.CommandButton CustomeReplaySettingsDeleteOrRestoreCommand 
            Caption         =   "删除/取消"
            Height          =   495
            Left            =   2400
            TabIndex        =   12
            Top             =   2640
            Width           =   1575
         End
         Begin VB.CommandButton CustomeReplaySettingsAddOrModifyCommand 
            Caption         =   "添加/修改"
            Height          =   495
            Left            =   600
            TabIndex        =   11
            Top             =   2640
            Width           =   1575
         End
         Begin VB.TextBox CustomeReplaySettingsReplyInput 
            Height          =   495
            Left            =   1680
            TabIndex        =   10
            Text            =   "输入自定义回复设置"
            Top             =   1800
            Width           =   2055
         End
         Begin VB.TextBox CustomeReplaySettingsKeyworldInput 
            Height          =   495
            Left            =   1680
            TabIndex        =   9
            Text            =   "输入关键字"
            Top             =   960
            Width           =   2055
         End
         Begin VB.Label CustomeReplaySettingsReplyLable 
            AutoSize        =   -1  'True
            Caption         =   "自定义回复:"
            Height          =   420
            Left            =   360
            TabIndex        =   14
            Top             =   1800
            Width           =   1215
         End
         Begin VB.Label CustomeReplaySettingsKeyworldLabel 
            AutoSize        =   -1  'True
            Caption         =   "关键字:"
            Height          =   300
            Left            =   360
            TabIndex        =   13
            Top             =   960
            Width           =   1095
         End
      End
      Begin VB.Frame CustomeNicknameSettingsFrame 
         Caption         =   "自定义昵称设置"
         Height          =   3855
         Left            =   20280
         TabIndex        =   1
         Top             =   840
         Width           =   4815
         Begin VB.TextBox OriginalNicknameInput 
            Height          =   495
            Left            =   1800
            TabIndex        =   5
            Text            =   "输入昵称或者双击昵称"
            Top             =   960
            Width           =   2055
         End
         Begin VB.TextBox CustomizedNicknameInput 
            Height          =   495
            Left            =   1800
            TabIndex        =   4
            Text            =   "输入自定义昵称"
            Top             =   1800
            Width           =   2055
         End
         Begin VB.CommandButton CustomizedNicknameAddOrModifyCommand 
            Caption         =   "添加/修改"
            Height          =   495
            Left            =   600
            TabIndex        =   3
            Top             =   2640
            Width           =   1575
         End
         Begin VB.CommandButton CustomizedNicknameDeleteOrRestorCommand 
            Caption         =   "删除/取消"
            Height          =   495
            Left            =   2400
            TabIndex        =   2
            Top             =   2640
            Width           =   1575
         End
         Begin VB.Label OriginalNicknameLabel 
            AutoSize        =   -1  'True
            Caption         =   "原始昵称:"
            Height          =   300
            Left            =   360
            TabIndex        =   7
            Top             =   960
            Width           =   1290
         End
         Begin VB.Label CustomizedNicknameLable 
            AutoSize        =   -1  'True
            Caption         =   "自定义昵称:"
            Height          =   300
            Left            =   360
            TabIndex        =   6
            Top             =   1800
            Width           =   1335
         End
      End
      Begin VB.Label LogInfoLable 
         Caption         =   "机器人未启动,房间号未录入,房管号未登录,请先登录房管号并录入房间号启动机器人"
         Height          =   255
         Left            =   4800
         TabIndex        =   74
         Top             =   360
         Width           =   20175
      End
      Begin VB.Label CopyRightLabel1 
         Caption         =   "CopyRight@ 2020 WangZhen <wangzhenjjcn@gmail.com> myazure.org"
         Height          =   375
         Left            =   19320
         TabIndex        =   73
         Top             =   11520
         Width           =   5895
      End
   End
End
Attribute VB_Name = "虎牙切克闹"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub Slider1_Click()

End Sub

Private Sub List4_Click()

End Sub

