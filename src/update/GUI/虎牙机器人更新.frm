VERSION 5.00
Object = "{831FDD16-0C5C-11D2-A9FC-0000F8754DA1}#2.2#0"; "MSCOMCTL.OCX"
Begin VB.Form ���³��� 
   Caption         =   "�������³���"
   ClientHeight    =   3690
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   4545
   LinkTopic       =   "Form1"
   ScaleHeight     =   3690
   ScaleWidth      =   4545
   StartUpPosition =   3  '����ȱʡ
   Begin VB.Frame driverframe 
      Caption         =   "��������"
      Height          =   3495
      Left            =   360
      TabIndex        =   0
      Top             =   120
      Width           =   3735
      Begin VB.CommandButton ExitBtn 
         Caption         =   "�ر�"
         Height          =   495
         Left            =   1920
         TabIndex        =   5
         Top             =   2520
         Width           =   1455
      End
      Begin MSComctlLib.ProgressBar ProcessBar 
         Height          =   255
         Index           =   15
         Left            =   360
         TabIndex        =   4
         Top             =   2040
         Width           =   3015
         _ExtentX        =   5318
         _ExtentY        =   450
         _Version        =   393216
         Appearance      =   1
      End
      Begin VB.CommandButton UpdateBtn 
         Caption         =   "��������"
         Height          =   495
         Left            =   360
         TabIndex        =   3
         Top             =   2520
         Width           =   1455
      End
      Begin VB.Label ChromeVersionLable 
         Caption         =   "������汾��"
         Height          =   255
         Left            =   360
         TabIndex        =   9
         Top             =   1440
         Width           =   1095
      End
      Begin VB.Label ChromeVersion 
         Caption         =   "Unknown"
         Height          =   255
         Left            =   1680
         TabIndex        =   8
         Top             =   1440
         Width           =   1815
      End
      Begin VB.Label LastVersion 
         Caption         =   "Unknown"
         Height          =   255
         Left            =   1680
         TabIndex        =   7
         Top             =   960
         Width           =   1815
      End
      Begin VB.Label CurrentVersion 
         Caption         =   "0.0.0.0"
         Height          =   255
         Left            =   1680
         TabIndex        =   6
         Top             =   480
         Width           =   1815
      End
      Begin VB.Label LastVersionLable 
         Caption         =   "���°汾��"
         Height          =   255
         Left            =   360
         TabIndex        =   2
         Top             =   960
         Width           =   1095
      End
      Begin VB.Label CurrentVersionLable 
         Caption         =   "��ǰ�汾��"
         Height          =   255
         Left            =   360
         TabIndex        =   1
         Top             =   480
         Width           =   1215
      End
   End
End
Attribute VB_Name = "���³���"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
