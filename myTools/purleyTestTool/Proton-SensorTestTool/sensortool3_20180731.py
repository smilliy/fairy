# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import os, subprocess, re, threading, time, queue, random, sys
from wx.lib.pubsub import setupkwargs


from wx.lib.pubsub import pub
from threading import Thread


SDR_ELIST=queue.Queue()
Threshold_LNC = queue.Queue()
Threshold_LC = queue.Queue()
Threshold_LNR = queue.Queue()
Threshold_UNC = queue.Queue()
Threshold_UC = queue.Queue()
Threshold_UNR = queue.Queue()
Start_Stop_Stress = ''
IPMItool_Path = 'ipmitool'

###########################################################################
## Class MyFrame1
###########################################################################


class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sensor Test Tool -- Version 2018.07.31", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.Size( 800,600 ), wx.Size( 800,600 ) )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
        
        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 600,-1 ), wx.TAB_TRAVERSAL )
        self.m_panel5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
        self.m_panel5.SetMinSize( wx.Size( 600,-1 ) )
        self.m_panel5.SetMaxSize( wx.Size( 600,-1 ) )
        
        bSizer8 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText3 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Test CMD Result:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer8.Add( self.m_staticText3, 0, wx.ALL, 5 )
        
        self.m_text_TestResult = wx.TextCtrl( self.m_panel5, wx.ID_ANY, u"###########################Start###########################\n\nChecking IPMItool version on your system:\n", wx.DefaultPosition, wx.Size( 580,230 ), wx.TE_LEFT|wx.TE_MULTILINE|wx.TE_WORDWRAP )
        self.m_text_TestResult.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

        
        bSizer8.Add( self.m_text_TestResult, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_staticline5 = wx.StaticLine( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer8.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )
        
        bSizer20 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_notebook1 = wx.Notebook( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_notebook1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
        
        self.m_panel13 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer131 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_panel151 = wx.Panel( self.m_panel13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel151.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
        
        bSizer141 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_radio_SensorName_Discrete = wx.RadioButton( self.m_panel151, wx.ID_ANY, u"Enter Sensor Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer141.Add( self.m_radio_SensorName_Discrete, 0, wx.ALL, 5 )
        
        self.m_text_SensorName_Discrete = wx.TextCtrl( self.m_panel151, wx.ID_ANY, u"<Sensor Name>", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer141.Add( self.m_text_SensorName_Discrete, 0, wx.ALL, 5 )
        
        self.m_staticText7 = wx.StaticText( self.m_panel151, wx.ID_ANY, u"EventOffsetValue:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        bSizer141.Add( self.m_staticText7, 0, wx.ALL, 5 )
        
        m_combo_EventOffsetValue_DiscreteChoices = []
        self.m_combo_EventOffsetValue_Discrete = wx.ComboBox( self.m_panel151, wx.ID_ANY, u"De-Assert", wx.DefaultPosition, wx.DefaultSize, m_combo_EventOffsetValue_DiscreteChoices, 0 )
        self.m_combo_EventOffsetValue_Discrete.SetForegroundColour( wx.Colour( 255, 0, 0 ) ) 
        
        bSizer141.Add( self.m_combo_EventOffsetValue_Discrete, 0, wx.ALL, 5 )
        
        
        self.m_panel151.SetSizer( bSizer141 )
        self.m_panel151.Layout()
        bSizer141.Fit( self.m_panel151 )
        bSizer131.Add( self.m_panel151, 1, wx.ALL, 5 )
        
        self.m_panel161 = wx.Panel( self.m_panel13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer151 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_radio_SensorID_Discrete = wx.RadioButton( self.m_panel161, wx.ID_ANY, u"Enter Sensor ID", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer151.Add( self.m_radio_SensorID_Discrete, 0, wx.ALL, 5 )
        
        self.m_text_SensorID_Discrete = wx.TextCtrl( self.m_panel161, wx.ID_ANY, u"<Sensor ID>", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer151.Add( self.m_text_SensorID_Discrete, 0, wx.ALL, 5 )
        
        self.m_staticText9 = wx.StaticText( self.m_panel161, wx.ID_ANY, u"EventData:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        bSizer151.Add( self.m_staticText9, 0, wx.ALL, 5 )
        
        m_combo_EventData_DiscreteChoices = []
        self.m_combo_EventData_Discrete = wx.ComboBox( self.m_panel161, wx.ID_ANY, u"De-Assert", wx.DefaultPosition, wx.DefaultSize, m_combo_EventData_DiscreteChoices, 0 )
        self.m_combo_EventData_Discrete.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
        
        bSizer151.Add( self.m_combo_EventData_Discrete, 0, wx.ALL, 5 )
        
        
        self.m_panel161.SetSizer( bSizer151 )
        self.m_panel161.Layout()
        bSizer151.Fit( self.m_panel161 )
        bSizer131.Add( self.m_panel161, 1, wx.ALL, 5 )
        
        self.m_panel17 = wx.Panel( self.m_panel13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer161 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_radio_SensorList_Discrete = wx.RadioButton( self.m_panel17, wx.ID_ANY, u"Select From List", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer161.Add( self.m_radio_SensorList_Discrete, 0, wx.ALL, 5 )
        
        m_combo_SensorList_DiscreteChoices = []
        self.m_combo_SensorList_Discrete = wx.ComboBox( self.m_panel17, wx.ID_ANY, u"<Sensor List> :", wx.DefaultPosition, wx.DefaultSize, m_combo_SensorList_DiscreteChoices, style = wx.CB_READONLY )
        bSizer161.Add( self.m_combo_SensorList_Discrete, 0, wx.ALL, 5 )
        
        self.m_staticText11 = wx.StaticText( self.m_panel17, wx.ID_ANY, u"Run Sensor Test:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        bSizer161.Add( self.m_staticText11, 0, wx.ALL, 5 )
        
        self.m_button_RunDiscreteSensorTest = wx.Button( self.m_panel17, wx.ID_ANY, u"Run", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer161.Add( self.m_button_RunDiscreteSensorTest, 0, wx.ALL, 5 )
        
        
        self.m_panel17.SetSizer( bSizer161 )
        self.m_panel17.Layout()
        bSizer161.Fit( self.m_panel17 )
        bSizer131.Add( self.m_panel17, 1, wx.ALL, 5 )
        
        
        self.m_panel13.SetSizer( bSizer131 )
        self.m_panel13.Layout()
        bSizer131.Fit( self.m_panel13 )
        self.m_notebook1.AddPage( self.m_panel13, u"Discrete Sensor", True )
        self.m_panel14 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer142 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel131 = wx.Panel( self.m_panel14, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer152 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_panel141 = wx.Panel( self.m_panel131, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer162 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_radio_SensorName_Threshoold = wx.RadioButton( self.m_panel141, wx.ID_ANY, u"Enter Sensor Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer162.Add( self.m_radio_SensorName_Threshoold, 0, wx.ALL, 5 )
        
        self.m_text_SensorName_Threshold = wx.TextCtrl( self.m_panel141, wx.ID_ANY, u"Sys Brd 3.3V", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer162.Add( self.m_text_SensorName_Threshold, 0, wx.ALL, 5 )
        
        self.m_text_LNC_Threeshold = wx.TextCtrl( self.m_panel141, wx.ID_ANY, u"LNC:", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer162.Add( self.m_text_LNC_Threeshold, 0, wx.ALL, 5 )
        
        self.m_textCtr_UNC_Assert_Threshold = wx.TextCtrl( self.m_panel141, wx.ID_ANY, u"UNC:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtr_UNC_Assert_Threshold.SetForegroundColour( wx.Colour( 0, 0, 255 ) )
        
        bSizer162.Add( self.m_textCtr_UNC_Assert_Threshold, 0, wx.ALL, 5 )
        
        self.m_checkBox_InputManually = wx.StaticText( self.m_panel141, wx.ID_ANY, u"Input the sensor reading value:", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer162.Add( self.m_checkBox_InputManually, 0, wx.ALL|wx.ALIGN_RIGHT|wx.EXPAND, 5 )
        
        
        self.m_panel141.SetSizer( bSizer162 )
        self.m_panel141.Layout()
        bSizer162.Fit( self.m_panel141 )
        bSizer152.Add( self.m_panel141, 1, wx.EXPAND|wx.ALL, 5 )
        
        self.m_panel152 = wx.Panel( self.m_panel131, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer17 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_radioBtn_SensorID_Threshold = wx.RadioButton( self.m_panel152, wx.ID_ANY, u"Enter Sensor ID:", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer17.Add( self.m_radioBtn_SensorID_Threshold, 0, wx.ALL, 5 )
        
        self.m_textCtrl_SenSorID_Thresshold = wx.TextCtrl( self.m_panel152, wx.ID_ANY, u"0x32", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer17.Add( self.m_textCtrl_SenSorID_Thresshold, 0, wx.ALL, 5 )
        
        self.m_textCtrl_LC_Threshold = wx.TextCtrl( self.m_panel152, wx.ID_ANY, u"LC:", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer17.Add( self.m_textCtrl_LC_Threshold, 0, wx.ALL, 5 )
        
        self.m_textCtrl_UC_Threshold = wx.TextCtrl( self.m_panel152, wx.ID_ANY, u"UC:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl_UC_Threshold.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
        
        bSizer17.Add( self.m_textCtrl_UC_Threshold, 0, wx.ALL, 5 )
        
        self.m_textCtrl_Input_Threshold = wx.TextCtrl( self.m_panel152, wx.ID_ANY, u"0xdd", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl_Input_Threshold.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
        bSizer17.Add( self.m_textCtrl_Input_Threshold, 0, wx.ALL, 5 )
        
        
        self.m_panel152.SetSizer( bSizer17 )
        self.m_panel152.Layout()
        bSizer17.Fit( self.m_panel152 )
        bSizer152.Add( self.m_panel152, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel16 = wx.Panel( self.m_panel131, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer181 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_radioBtn_SensorList_Threshold = wx.RadioButton( self.m_panel16, wx.ID_ANY, u"Select From List:", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer181.Add( self.m_radioBtn_SensorList_Threshold, 0, wx.ALL, 5 )
        
        m_comboBox_SensorList_ThresholdChoices = []
        self.m_comboBox_SensorList_Threshold = wx.ComboBox( self.m_panel16, wx.ID_ANY, u"<Sensor List> :", wx.DefaultPosition, wx.DefaultSize, m_comboBox_SensorList_ThresholdChoices, style = wx.CB_READONLY )
        bSizer181.Add( self.m_comboBox_SensorList_Threshold, 0, wx.ALL, 5 )
        
        self.m_textctrl_LNR_Threshold = wx.TextCtrl( self.m_panel16, wx.ID_ANY, u"LNR:", wx.DefaultPosition, wx.DefaultSize, style = wx.RB_GROUP)
        bSizer181.Add( self.m_textctrl_LNR_Threshold, 0, wx.ALL, 5 )
        
        self.m_textCtr_UCR_Threshold = wx.TextCtrl( self.m_panel16, wx.ID_ANY, u"UCR:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtr_UCR_Threshold.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
        
        bSizer181.Add( self.m_textCtr_UCR_Threshold, 0, wx.ALL, 5 )
        
        bSizer30 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button_Test_Threshold = wx.Button( self.m_panel16, wx.ID_ANY, u"Get Threshold", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer30.Add( self.m_button_Test_Threshold, 0, wx.ALL, 5 )
        
        self.m_button_Run_Threshold = wx.Button( self.m_panel16, wx.ID_ANY, u"Run", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer30.Add( self.m_button_Run_Threshold, 0, wx.ALL, 5 )
        
        
        bSizer181.Add( bSizer30, 1, wx.EXPAND, 5 )
        
        
        self.m_panel16.SetSizer( bSizer181 )
        self.m_panel16.Layout()
        bSizer181.Fit( self.m_panel16 )
        bSizer152.Add( self.m_panel16, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.m_panel131.SetSizer( bSizer152 )
        self.m_panel131.Layout()
        bSizer152.Fit( self.m_panel131 )
        bSizer142.Add( self.m_panel131, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.m_panel14.SetSizer( bSizer142 )
        self.m_panel14.Layout()
        bSizer142.Fit( self.m_panel14 )
        self.m_notebook1.AddPage( self.m_panel14, u"Threshold Sensor", False )
        self.m_panel15 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer19 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel18 = wx.Panel( self.m_panel15, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer201 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText12 = wx.StaticText( self.m_panel18, wx.ID_ANY, u"Enter Your IPMI CMD:  ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )
        bSizer201.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
        
        self.m_textCtrl_RawData_TriaggerrCMD = wx.TextCtrl( self.m_panel18, wx.ID_ANY, u"raw 0x06 0x01", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer201.Add( self.m_textCtrl_RawData_TriaggerrCMD, 1, wx.ALL|wx.ALIGN_BOTTOM, 5 )
        
        
        self.m_panel18.SetSizer( bSizer201 )
        self.m_panel18.Layout()
        bSizer201.Fit( self.m_panel18 )
        bSizer19.Add( self.m_panel18, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel19 = wx.Panel( self.m_panel15, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer21 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_button_Send_TriaggerCMD = wx.Button( self.m_panel19, wx.ID_ANY, u"Send", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer21.Add( self.m_button_Send_TriaggerCMD, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
        
        
        self.m_panel19.SetSizer( bSizer21 )
        self.m_panel19.Layout()
        bSizer21.Fit( self.m_panel19 )
        bSizer19.Add( self.m_panel19, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.m_panel15.SetSizer( bSizer19 )
        self.m_panel15.Layout()
        bSizer19.Fit( self.m_panel15 )
        self.m_notebook1.AddPage( self.m_panel15, u"Triagger CMD", False )
        self.m_panel20 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer22 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_panel21 = wx.Panel( self.m_panel20, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer23 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_checkBox_PowerOnoff_stress = wx.CheckBox( self.m_panel21, wx.ID_ANY, u"Power off/on", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_checkBox_PowerOnoff_stress.SetValue(True) 
        bSizer23.Add( self.m_checkBox_PowerOnoff_stress, 0, wx.ALL, 5 )
        
        self.m_checkBox6 = wx.CheckBox( self.m_panel21, wx.ID_ANY, u"Power Cycle", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer23.Add( self.m_checkBox6, 0, wx.ALL, 5 )
        
        self.m_checkBox7 = wx.CheckBox( self.m_panel21, wx.ID_ANY, u"Power Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer23.Add( self.m_checkBox7, 0, wx.ALL, 5 )
        
        self.m_checkBox8 = wx.CheckBox( self.m_panel21, wx.ID_ANY, u"BMC Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer23.Add( self.m_checkBox8, 0, wx.ALL, 5 )
        
        
        self.m_panel21.SetSizer( bSizer23 )
        self.m_panel21.Layout()
        bSizer23.Fit( self.m_panel21 )
        bSizer22.Add( self.m_panel21, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_panel22 = wx.Panel( self.m_panel20, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer24 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText13 = wx.StaticText( self.m_panel22, wx.ID_ANY, u"Power on time:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )
        bSizer24.Add( self.m_staticText13, 0, wx.ALL, 5 )
        
        self.m_textCtrl_onoffTimeInterval_Stress = wx.TextCtrl( self.m_panel22, wx.ID_ANY, u"300", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer24.Add( self.m_textCtrl_onoffTimeInterval_Stress, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText14 = wx.StaticText( self.m_panel22, wx.ID_ANY, u"BMC ready time:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText14.Wrap( -1 )
        bSizer24.Add( self.m_staticText14, 0, wx.ALL, 5 )
        
        self.m_textCtrlResetBMCInterVal_Stress = wx.TextCtrl( self.m_panel22, wx.ID_ANY, u"180", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer24.Add( self.m_textCtrlResetBMCInterVal_Stress, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel22.SetSizer( bSizer24 )
        self.m_panel22.Layout()
        bSizer24.Fit( self.m_panel22 )
        bSizer22.Add( self.m_panel22, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel23 = wx.Panel( self.m_panel20, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer25 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText15 = wx.StaticText( self.m_panel23, wx.ID_ANY, u"Loops:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText15.Wrap( -1 )
        bSizer25.Add( self.m_staticText15, 0, wx.ALL, 5 )
        
        self.m_textCtrl_Loops_Stress = wx.TextCtrl( self.m_panel23, wx.ID_ANY, u"200", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer25.Add( self.m_textCtrl_Loops_Stress, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText17 = wx.StaticText( self.m_panel23, wx.ID_ANY, u"Star/Stop stress:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )
        bSizer25.Add( self.m_staticText17, 0, wx.ALL, 5 )
        
        self.m_button_StartStress_Stress = wx.Button( self.m_panel23, wx.ID_ANY, u"Start Stress", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer25.Add( self.m_button_StartStress_Stress, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button_Stop_Stress = wx.Button( self.m_panel23, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer25.Add( self.m_button_Stop_Stress, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel23.SetSizer( bSizer25 )
        self.m_panel23.Layout()
        bSizer25.Fit( self.m_panel23 )
        bSizer22.Add( self.m_panel23, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.m_panel20.SetSizer( bSizer22 )
        self.m_panel20.Layout()
        bSizer22.Fit( self.m_panel20 )
        self.m_notebook1.AddPage( self.m_panel20, u"Stress", False )
        
        bSizer20.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        bSizer8.Add( bSizer20, 1, wx.EXPAND, 5 )
        
        
        self.m_panel5.SetSizer( bSizer8 )
        self.m_panel5.Layout()
        bSizer7.Add( self.m_panel5, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TAB_TRAVERSAL )
        self.m_panel6.SetMinSize( wx.Size( 200,-1 ) )
        self.m_panel6.SetMaxSize( wx.Size( 200,-1 ) )
        
        bSizer9 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel8 = wx.Panel( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel8.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
        
        bSizer13 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel9 = wx.Panel( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel9.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
        
        bSizer14 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel11 = wx.Panel( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
        
        bSizer18 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText18 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"IP:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )
        bSizer18.Add( self.m_staticText18, 0, wx.ALL, 5 )
        
        self.m_textCtrl_ip = wx.TextCtrl( self.m_panel11, wx.ID_ANY, u"10.245.17.226", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer18.Add( self.m_textCtrl_ip, 0, wx.ALL, 5 )
        
        self.m_staticText19 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"USERID:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )
        bSizer18.Add( self.m_staticText19, 0, wx.ALL, 5 )
        
        self.m_textCtrl_userid = wx.TextCtrl( self.m_panel11, wx.ID_ANY, u"USERID", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer18.Add( self.m_textCtrl_userid, 0, wx.ALL, 5 )
        
        self.m_staticText20 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"PASSWORD:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText20.Wrap( -1 )
        bSizer18.Add( self.m_staticText20, 0, wx.ALL, 5 )
        
        self.m_textCtrl_password = wx.TextCtrl( self.m_panel11, wx.ID_ANY, u"PASSW0RD", wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
        bSizer18.Add( self.m_textCtrl_password, 0, wx.ALL, 5 )
        
        self.m_staticText91 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Interface:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText91.Wrap( -1 )
        bSizer18.Add( self.m_staticText91, 0, wx.ALL, 5 )
        
        m_comboBox_lanpChoices = []
        self.m_comboBox_lanp = wx.ComboBox( self.m_panel11, wx.ID_ANY, u"Lanp", wx.DefaultPosition, wx.DefaultSize, m_comboBox_lanpChoices, 0 )
        bSizer18.Add( self.m_comboBox_lanp, 0, wx.ALL, 5 )
        
        
        self.m_panel11.SetSizer( bSizer18 )
        self.m_panel11.Layout()
        bSizer18.Fit( self.m_panel11 )
        bSizer14.Add( self.m_panel11, 1, wx.EXPAND |wx.ALL, 5 )
        
        bSizer15 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel10 = wx.Panel( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel10.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
        
        bSizer16 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_button5_DcServerr = wx.Button( self.m_panel10, wx.ID_ANY, u"DC Server", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer16.Add( self.m_button5_DcServerr, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button_ResetBMC = wx.Button( self.m_panel10, wx.ID_ANY, u"Reset BMC", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer16.Add( self.m_button_ResetBMC, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button_ClearLog = wx.Button( self.m_panel10, wx.ID_ANY, u"Clear SEL Log", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer16.Add( self.m_button_ClearLog, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_button_ClearTextResult = wx.Button( self.m_panel10, wx.ID_ANY, u"Clear Text Result", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer16.Add( self.m_button_ClearTextResult, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_buttonGetSELlog = wx.Button( self.m_panel10, wx.ID_ANY, u"Get SEL Log", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer16.Add( self.m_buttonGetSELlog, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel10.SetSizer( bSizer16 )
        self.m_panel10.Layout()
        bSizer16.Fit( self.m_panel10 )
        bSizer15.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        bSizer14.Add( bSizer15, 1, wx.EXPAND, 5 )
        
        
        self.m_panel9.SetSizer( bSizer14 )
        self.m_panel9.Layout()
        bSizer14.Fit( self.m_panel9 )
        bSizer13.Add( self.m_panel9, 1, wx.EXPAND|wx.ALL, 5 )
        
        
        self.m_panel8.SetSizer( bSizer13 )
        self.m_panel8.Layout()
        bSizer13.Fit( self.m_panel8 )
        bSizer9.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.m_panel6.SetSizer( bSizer9 )
        self.m_panel6.Layout()
        bSizer7.Add( self.m_panel6, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer7 )
        self.Layout()
        self.m_statusBar = self.CreateStatusBar( 1, wx.ST_NO_AUTORESIZE, wx.ID_ANY )
        self.m_menubar2 = wx.MenuBar( 0 )
        self.m_menu1 = wx.Menu()
#         self.m_menuItem3 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"New", wx.EmptyString, wx.ITEM_NORMAL )
#         self.m_menu1.AppendItem( self.m_menuItem3 )
        
#         self.m_menuItem4 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
#         self.m_menu1.AppendItem( self.m_menuItem4 )
        
#         self.m_menubar2.Append( self.m_menu1, u"File" ) 
        
        self.m_menu4 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"Set IPMITool Path", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu4.AppendItem( self.m_menuItem1 )
        
        self.m_menubar2.Append( self.m_menu4, u"Setting" ) 
        
        self.m_menu2 = wx.Menu()
        self.m_menuItem5 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.AppendItem( self.m_menuItem5 )
        
        self.m_menuItem6 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Help Info", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.AppendItem( self.m_menuItem6 )
        
        self.m_menubar2.Append( self.m_menu2, u"Help" ) 
        
        self.SetMenuBar( self.m_menubar2 )
        
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_radio_SensorName_Discrete.Bind( wx.EVT_RADIOBUTTON, self.OnSelect_SelectSensorName_DiscreteSensor )
        self.m_radio_SensorID_Discrete.Bind( wx.EVT_RADIOBUTTON, self.OnSelect_SelectSensorID_DiscreteSensor )
        self.m_radio_SensorList_Discrete.Bind( wx.EVT_RADIOBUTTON, self.OnSelect_SelectFromlist_DiscreteSensor )
        self.m_button_RunDiscreteSensorTest.Bind( wx.EVT_BUTTON, self.OnClick_DiscreteSensorTest )
        self.m_radio_SensorName_Threshoold.Bind( wx.EVT_RADIOBUTTON, self.OnSelect_SelectSensorName_Threshold )
#        self.m_Radiobtn_LCRAssert_Threeshold.Bind( wx.EVT_RADIOBUTTON, self.OnSelect_SlectLCRAssert_Threshold )
        self.m_checkBox_InputManually.Bind( wx.EVT_CHECKBOX, self.OnSelect_SelectInputManually_Threshold )
        self.m_radioBtn_SensorID_Threshold.Bind( wx.EVT_RADIOBUTTON, self.OnSelect_SelectSensorID_Threshold )
#         self.m_Radiobtn_Normal_Threshold.Bind( wx.EVT_RADIOBUTTON, self.OnSelect_SelectNormal_Threshold )
        self.m_radioBtn_SensorList_Threshold.Bind( wx.EVT_RADIOBUTTON, self.OnSelect_SelectfromList_Threshold )
#         self.m_Radiobtn_UCRAssert_Threshold.Bind( wx.EVT_RADIOBUTTON, self.OnSelect_SelectUCRAssert_Threshold )
        self.m_button_Test_Threshold.Bind( wx.EVT_BUTTON, self.OnClick_ClickTest_Threshold )
        self.m_button_Run_Threshold.Bind( wx.EVT_BUTTON, self.OnClick_ClickRun_Thresholld )
        self.m_button_Send_TriaggerCMD.Bind( wx.EVT_BUTTON, self.OnClick_ClickSend_TriaggerrCMD )
        self.m_button_StartStress_Stress.Bind( wx.EVT_BUTTON, self.OnClick_StartStress_Stress )
        self.m_button_Stop_Stress.Bind( wx.EVT_BUTTON, self.OnClick_Stop_Stress )
        self.m_button5_DcServerr.Bind( wx.EVT_BUTTON, self.OnClick_DCServer )
        self.m_button_ResetBMC.Bind( wx.EVT_BUTTON, self.OnClick_ResetBMC )
        self.m_button_ClearLog.Bind( wx.EVT_BUTTON, self.OnClick_ClearSELlog )
        self.m_button_ClearTextResult.Bind( wx.EVT_BUTTON, self.OnClick_ClearTextResult )
        self.m_buttonGetSELlog.Bind( wx.EVT_BUTTON, self.OnClick_GetSELlog )
#         self.Bind( wx.EVT_MENU, self.OnClick_MenuNew, id = self.m_menuItem3.GetId() )
#         self.Bind( wx.EVT_MENU, self.OnClick_MenuExit, id = self.m_menuItem4.GetId() )
        self.Bind( wx.EVT_MENU, self.OnClick_MenuIPMItoolPATH, id = self.m_menuItem1.GetId() )
        self.Bind( wx.EVT_MENU, self.OnClick_MenuAbout, id = self.m_menuItem5.GetId() )
        self.Bind( wx.EVT_MENU, self.OnClick_MenuHelp, id = self.m_menuItem6.GetId() )
        self.Bind( wx.EVT_CLOSE, self.OnClose_window )
        self._InitGui()
    
    def _InitGui(self):
        self.state = 'on'
        self.m_radio_SensorName_Discrete.SetValue(True)
        self.m_radio_SensorID_Discrete.SetValue(False)
        self.m_radio_SensorList_Discrete.SetValue(False)
        self.m_text_SensorName_Discrete.Enable(True)
        self.m_text_SensorID_Discrete.Enable(False)
        self.m_combo_SensorList_Discrete.Enable(False)
        offsetdata = ['De-Assert','00h', '01h', '02h', '03h', '04h', '05h', '06h',
                        '07h', '08h', '09h', '0ah', '0bh', '0ch', '0dh', '0eh', '0fh']
        self.m_combo_EventOffsetValue_Discrete.Set(offsetdata)
        self.m_combo_EventOffsetValue_Discrete.Select(0)
        self.m_combo_EventData_Discrete.Set(["0x00 0x00"])
        self.m_combo_EventData_Discrete.Select(0)
        self.m_textCtrl_ip.SetFocus()
        lanpdata = ['lanp', 'lan']
        self.m_comboBox_lanp.Set(lanpdata)
        self.m_comboBox_lanp.Select(0)
        self.m_combo_SensorList_Discrete.Clear()
        self.m_combo_SensorList_Discrete.Append('Sensor List:')
        self.m_combo_SensorList_Discrete.Select(0)
        self.m_text_SensorID_Discrete.Clear()        
        self.m_text_SensorID_Discrete.SetValue('0XFF')
        self.m_text_SensorName_Discrete.Clear()
        self.m_text_SensorName_Discrete.SetValue('XCC Switchover')
        self.m_radio_SensorName_Threshoold.SetValue(True)
        self.m_radioBtn_SensorID_Threshold.SetValue(False)
        self.m_radioBtn_SensorList_Threshold.SetValue(False)
        self.m_textCtrl_Input_Threshold.SetToolTipString(u'LNC: lower non-critical threshold\n'+ 
                                                        u'LC: lower critical threshold\n'+ 
                                                        u'LNR: lower non-recoverable threshold\n'+ 
                                                        u'UNC: upper non-critical threshold\n'+ 
                                                        u'UC: upper critical threshold\n'+ 
                                                        u'UNR: upper non-recoverable threshold')
        

#         self.m_Radiobtn_Normal_Threshold.SetValue(False)
#         self.m_Radiobtn_UCRAssert_Threshold.SetValue(False)
        
        self.m_comboBox_SensorList_Threshold.Clear()
        self.m_comboBox_SensorList_Threshold.Append('Sensor List:')
        self.m_comboBox_SensorList_Threshold.Select(0)                    
#         self.m_checkBox_InputManually.SetValue(False)
        self.m_text_LNC_Threeshold.Enable(False)
        self.m_textCtrl_LC_Threshold.Enable(False)
        self.m_textctrl_LNR_Threshold.Enable(False)
        self.m_textCtr_UNC_Assert_Threshold.Enable(False)
        self.m_textCtrl_UC_Threshold.Enable(False)
        self.m_textCtr_UCR_Threshold.Enable(False)
        self.m_textCtrl_Input_Threshold.Enable(True)
        self.m_textCtrl_SenSorID_Thresshold.Enable(False)
        self.m_comboBox_SensorList_Threshold.Enable(False)
        self.m_button_Stop_Stress.Enable(False)
        CheckIpmiTool()
        self._InfoStatusBar('Start at: %s'%getcurrenttime()) 
        pub.subscribe(self._updatetext, 'UpdateText')



    def __del__( self ):
        pass
    
    
    def _updatetext(self, msg):
        if msg == 'discreteDone':
#             self.m_button_RunDiscreteSensorTest.Enable(True) 
#             self.m_radio_SensorID_Discrete.Enable(True)
#             self.m_radio_SensorList_Discrete.Enable(True)
#             self.m_radio_SensorName_Discrete.Enable(True)
#             self.m_combo_EventData_Discrete.Enable(True)
#             self.m_combo_EventOffsetValue_Discrete.Enable(True)
#             if self.m_radio_SensorName_Discrete.GetValue() == True:
#                 self.m_text_SensorName_Discrete.Enable(True) 
#             if self.m_radio_SensorList_Discrete.GetValue() == True:
#                 self.m_combo_SensorList_Discrete.Enable(True)
#             if self.m_radio_SensorID_Discrete.GetValue() == True:
#                 self.m_text_SensorID_Discrete.Enable(True)    
            self.m_panel6.Enable(True)    
            self.m_panel13.Enable(True)
            self.m_panel14.Enable(True)   
            self.m_panel15.Enable(True)
            self.m_panel20.Enable(True)  
            self._InfoStatusBar('Discrete sensor cmd has executed completely.') 
        elif msg == 'ThresholdDone':
            self.m_panel6.Enable(True)    
            self.m_panel13.Enable(True)
            self.m_panel14.Enable(True)   
            self.m_panel15.Enable(True)
            self.m_panel20.Enable(True)  
            self._InfoStatusBar('Threshold sensor cmd has executed completely.') 
        elif msg == 'Send_IPMI_CMD_Done':
            self.m_panel6.Enable(True)    
            self.m_panel13.Enable(True)
            self.m_panel14.Enable(True)   
            self.m_panel15.Enable(True)
            self.m_panel20.Enable(True)  
            self._InfoStatusBar('IPMI cmd has been sent..')             
        elif msg == '   ':
            pass  
        elif msg == 'SdrElist_receiving':
            self.m_combo_SensorList_Discrete.Enable(False)
            self._InfoStatusBar('Info: Getting sdr elist from server, please wait....')
        elif msg == 'SdrElist_receiving2':
            self.m_comboBox_SensorList_Threshold.Enable(False)
            self._InfoStatusBar('Info: Getting sdr elist from server, please wait....')            
        elif msg == 'SdrElist_done':
            self.m_combo_SensorList_Discrete.Enable(True)
            self._InfoStatusBar('Info: finish Getting sdr elist from server.')  
        elif msg == 'SdrElist_done2':
            self.m_comboBox_SensorList_Threshold.Enable(True) 
            self._InfoStatusBar('Info: finish Getting sdr elist from server.')            
        elif msg == 'SdrElist':
            sdrelist = SDR_ELIST.get()
#             print sdrelist
#             print type(sdrelist)
            sdrelist2 = sdrelist.split('\n')
            #print sdrelist2
            self.sensorname_id_dic = {}
            sensorname_dic = []
            sensorid_dic = []
            rr = re.compile(r'(.................|)')
            kk = re.compile(r'.+h')
            try:
                for line in sdrelist2:            
                    ab = rr.findall(line)
                    ac = kk.findall(line)
                    #print(ac)
                    ae=str(ac)
                    af = ae[-5:-3]
                    ad = '0x' + af
                    #print(ad)
                    #print ab
                    if ac != '' and ab[0] != '':
                        sensorid_dic.append(ac)
                        sensorname_dic.append(ab[0])        
#                     print ac + 'ac'
                    #print ab[0]   + 'ab[0]'                                     
                    self.sensorname_id_dic[ab[0]] = ad                    
            except:
                print 'Add sensorname_id_dic error 558'
                pass
            #print self.sensorname_id_dic
            try:
                self.sensorname_id_dic.pop('')
                #print self.sensorname_id_dic
                #self.sensorname_id_dic.pop('')
            except:
                print 'self.sensorname_id_dic error 256'
                pass
            self.m_combo_SensorList_Discrete.Clear()
            self.m_combo_SensorList_Discrete.Set(sorted(sensorname_dic))
            self.m_combo_SensorList_Discrete.Select(0)    
            self.m_combo_SensorList_Discrete.set(style = wx.CB_READONLY)                  
        elif msg == 'SdrElist2':
            sdrelist = SDR_ELIST.get()
#             print sdrelist
#             print type(sdrelist)
            sdrelist2 = sdrelist.split('\n')
            #print sdrelist2
            self.sensorname_id_dic = {}
            sensorname_dic = []
            sensorid_dic = []
            rr = re.compile(r'(.................|)')
            kk = re.compile(r'.+h')
            try:
                for line in sdrelist2:            
                    ab = rr.findall(line)
                    ac = kk.findall(line)
                    #print(ac)
                    ae=str(ac)
                    af = ae[-5:-3]
                    ad = '0x' + af
                    #print(ad)
                    #print ab
                    if ac != '' and ab[0] != '':
                        sensorid_dic.append(ac)
                        sensorname_dic.append(ab[0])        
#                     print ac + 'ac'
                    #print ab[0]   + 'ab[0]'                                     
                    self.sensorname_id_dic[ab[0]] = ad                    
            except:
                print 'Add sensorname_id_dic error 558'
                pass
            #print self.sensorname_id_dic
            try:
                self.sensorname_id_dic.pop('')
                #print self.sensorname_id_dic
                #self.sensorname_id_dic.pop('')
            except:
                print 'self.sensorname_id_dic error 256'
                pass
            self.m_comboBox_SensorList_Threshold.Clear()
            self.m_comboBox_SensorList_Threshold.Set(sorted(sensorname_dic))
            self.m_comboBox_SensorList_Threshold.Select(0)    
            self.m_comboBox_SensorList_Threshold.set(style = wx.CB_READONLY)               
        elif msg == 'SdrElist_fail':
            self._WarnStatusBar('Waring: Fail to get sdr elist, please try it again.')
        elif msg == 'FailExecuteIPMICMD':
            self._WarnStatusBar('Waring: Fail to execute IPMI CMD�� Please Check your ip userid password ipmicmd...etc')
        elif msg == 'Test_LCR_UCR_Done':
            self.m_button_Run_Threshold.Enable(True)
            self.m_button_Test_Threshold.Enable(True)
        elif msg == 'Fail_Test_LCR_UCR_Done':
            self._WarnStatusBar('Waring: Getting a NONE Threshold sensor.')
        elif msg == 'Threshold_LCR_UCR':

            self.m_text_LNC_Threeshold.SetValue('LNC: 0x' + Threshold_LNC.get().upper())
            self.m_textCtrl_LC_Threshold.SetValue('LC: 0x' + Threshold_LC.get().upper())
            self.m_textctrl_LNR_Threshold.SetValue('LNR: 0x' + Threshold_LNR.get())
            self.m_textCtr_UNC_Assert_Threshold.SetValue('UNC: 0x' + Threshold_UNC.get().upper())
            self.m_textCtrl_UC_Threshold.SetValue('UC: 0x' + Threshold_UC.get().upper())
            self.m_textCtr_UCR_Threshold.SetValue('UNR: 0x' + Threshold_UNR.get().upper())          
#             aaa = Threshold_LCR.get()
#             bbb = Threshold_UCR.get()
#             self.m_textCtr_UNC_Assert_Threshold.SetValue('LCR < 0x%s' %aaa.upper())
#             self.m_textCtr_UCR_Threshold.SetValue('UCR > 0x%s' %bbb.upper())
#             self.m_textCtrl_UC_Threshold.SetValue('0x%s to 0x%s'%(aaa.upper(), bbb.upper()))
            self._InfoStatusBar('Info: Checking LCR UCR value DONE.')
        elif msg == 'ThresholdSensor_run':
            self.m_button_Run_Threshold.Enable(True)
        elif msg == 'Run_stress_Done':
            self.m_panel6.Enable(True) 
            self.m_panel13.Enable(True)
            self.m_panel14.Enable(True)   
            self.m_panel15.Enable(True)
            self.m_checkBox6.Enable(True)
            self.m_checkBox7.Enable(True)
            self.m_checkBox8.Enable(True)
            self.m_checkBox_PowerOnoff_stress.Enable(True)
            self.m_button_StartStress_Stress.Enable(True)
            self.m_button_Stop_Stress.Enable(False)
            self.m_textCtrl_Loops_Stress.Enable(True)
            self.m_textCtrl_onoffTimeInterval_Stress.Enable(True)
            self.m_textCtrlResetBMCInterVal_Stress.Enable(True)      
            self._InfoStatusBar('Info: Stress has been run completely.')            
        else:
            self.m_text_TestResult.AppendText(msg)
    
    
    # Virtual event handlers, overide them in your derived class
    def OnSelect_SelectSensorName_DiscreteSensor( self, event ):
        self.m_radio_SensorName_Discrete.SetValue(True)
        self.m_radio_SensorID_Discrete.SetValue(False)
        self.m_radio_SensorList_Discrete.SetValue(False)
        self.m_text_SensorName_Discrete.Enable(True)
        self.m_text_SensorID_Discrete.Enable(False)
        self.m_combo_SensorList_Discrete.Enable(False)
        self.m_text_SensorName_Discrete.SetFocus()
    
    def OnSelect_SelectSensorID_DiscreteSensor( self, event ):
        self.m_radio_SensorName_Discrete.SetValue(False)
        self.m_radio_SensorID_Discrete.SetValue(True)
        self.m_radio_SensorList_Discrete.SetValue(False)
        self.m_text_SensorName_Discrete.Enable(False)
        self.m_text_SensorID_Discrete.Enable(True)
        self.m_combo_SensorList_Discrete.Enable(False)
        self.m_text_SensorID_Discrete.SetFocus()
    
    def OnSelect_SelectFromlist_DiscreteSensor( self, event ):
        self.m_radio_SensorName_Discrete.SetValue(False)
        self.m_radio_SensorID_Discrete.SetValue(False)
        self.m_radio_SensorList_Discrete.SetValue(True)
        self.m_text_SensorName_Discrete.Enable(False)
        self.m_text_SensorID_Discrete.Enable(False)
        self.m_combo_SensorList_Discrete.Enable(True)
        self._CollectData_ONDiscretePage()                
        #discretemessage = [self.ip1, self.userid1, self.password1, self.lanp1, 'sdr elist']
        discretemessage = [self.ip1, self.userid1, self.password1, self.lanp1, 'sdr elist']         
        OnSelect_SelectFromlist_DiscreteSensor_T(discretemessage)
            
                    

    
    def OnClick_DiscreteSensorTest( self, event ): 
        self._CollectData_ONDiscretePage() 
        if self.m_radio_SensorName_Discrete.GetValue() == True:
            sensornamex = self.m_text_SensorName_Discrete.GetValue()
            if self._CheckSensorNameExites(sensornamex) == 'SensorNamenotExites':
                print 'fffff'
                return 0
            else:
                sensorid = self.sensorname_id_obtion
        elif self.m_radio_SensorID_Discrete.GetValue() == True:
            sensorid = self.m_text_SensorID_Discrete.GetValue()
            if self._CheckSensorIDFormat(sensorid) == 'sensor id format error':
                return 0
        elif self.m_radio_SensorList_Discrete.GetValue() == True:
            try:
                sensorid = self.sensorname_id_dic[self.m_combo_SensorList_Discrete.GetValue()]
            except:
                dlg = wx.MessageDialog(None, 'Get Sensor ID from Sensor list Fail.\nPlease use the other way to test.?', 'Get Sensor ID Fail', wx.OK | wx.ICON_WARNING) 
                dlg.ShowModal()
                return 0
            
        rawdata = {'De-Assert':'0x00 0x00', '00h':'0x00 0x01', '01h':'0x00 0x02', '02h':'0x00 0x04', '03h':'0x00 0x08', 
           '04h':'0x00 0x10', '05h':'0x00 0x20', '06h':'0x00 0x40', '07h':'0x00 0x80', 
           '08h':'0x01 0x00', '09h':'0x02 0x00', '0ah':'0x04 0x00', '0bh':'0x08 0x00',
           '0ch':'0x10 0x00', '0dh':'0x20 0x00', '0eh':'0x40 0x00', '0fh':'0x80 0x00'} 
        try:         
            eventoffset = rawdata[self.m_combo_EventOffsetValue_Discrete.GetValue()] +  ' ' + self.m_combo_EventData_Discrete.GetValue() 
            cmd1 = ['raw 0x3a 0x17 0x0', 'raw 0x3a 0x17 0x4', 'raw 0x3a 0x17 0x5 %s'%(sensorid),
                 'raw 0x3a 0x17 0x1 %s %s'%(sensorid, eventoffset),''] 
        except Exception as e:
            eventoffset = self.m_combo_EventOffsetValue_Discrete.GetValue() +  ' ' + self.m_combo_EventData_Discrete.GetValue() 
            cmd1 = ['raw 0x3a 0x17 0x0', 'raw 0x3a 0x17 0x4', 'raw 0x3a 0x17 0x5 %s'%(sensorid),
                 'raw 0x3a 0x17 0x1 %s %s'%(sensorid, eventoffset),'']             
        finally:
            pass     

        if self.m_combo_EventOffsetValue_Discrete.GetValue() == 'De-Assert' and self.m_combo_EventData_Discrete.GetValue() == 'De-Assert':
            cmd1[4] = 'raw 0x3a 0x17 0x2'
        discretemessage = [self.ip1, self.userid1, self.password1, self.lanp1, cmd1]
#         self.m_button_RunDiscreteSensorTest.Enable(False)  
#         self.m_radio_SensorID_Discrete.Enable(False)
#         self.m_radio_SensorList_Discrete.Enable(False)
#         self.m_radio_SensorName_Discrete.Enable(False)
#         self.m_combo_EventData_Discrete.Enable(False)
#         self.m_combo_EventOffsetValue_Discrete.Enable(False)
#         self.m_combo_SensorList_Discrete.Enable(False)
#         self.m_text_SensorID_Discrete.Enable(False)
#         self.m_text_SensorName_Discrete.Enable(False)
        self._InfoStatusBar('Running discrete sensor test...')   
        self.m_panel6.Enable(False)    
        self.m_panel13.Enable(False)
        self.m_panel14.Enable(False)   
        self.m_panel15.Enable(False)
        self.m_panel20.Enable(False)
        OnClick_DiscreteSensorTest_T(discretemessage)
    def _CheckSensorNameExites(self, sensornamex):
        res2 = os.popen('%s -I %s -H %s -U %s -P %s %s' % (IPMItool_Path, self.lanp1, self.ip1, self.userid1, self.password1, 'raw 0x6 0x1')).read()
        if res2 == '':
            dlg = wx.MessageDialog(None, 'Please check your ip userid password etc ..', 'Fail to connect to Server', wx.OK | wx.ICON_WARNING) 
            dlg.ShowModal()     
            return 'SensorNamenotExites'   
        res = os.popen('%s -I %s -H %s -U %s -P %s %s' % (IPMItool_Path, self.lanp1, self.ip1, self.userid1, self.password1, 'sdr get "%s"'%sensornamex)).read()
        if res == '':
            dlg = wx.MessageDialog(None, 'Please check your sensor Name. Make sure it is correct..', 'Wrong Sensor Name.', wx.OK | wx.ICON_WARNING) 
            dlg.ShowModal()     
            return 'SensorNamenotExites'
        else:
            pub.sendMessage('UpdateText', msg='\n\n###Getting Sensor: "%s" from sdr elist at time: %s###\nPlease wiat...\n'%(sensornamex, getcurrenttime())) 
            pub.sendMessage('UpdateText', msg=res)
            rr = re.compile(r'(Sensor ID.+\))')
            ab = rr.findall(res)
            #print(ab)
            rr2 = re.compile(r'0[Xx].\)|0[Xx]..\)')
            ac = rr2.findall(str(ab)) 
            try:
                self.sensorname_id_obtion = str(ac[0][:-1])
            except:
                dlg = wx.MessageDialog(None, 'Fail to get sensor id from sdr elist.\nPlease use sensor id or sensor list to test.', 'Fail to get sensor id.', wx.OK | wx.ICON_WARNING) 
                dlg.ShowModal()     
                return 'SensorNamenotExites'                
            #print self.sensorname_id_obtion
         
  
    def _CheckSensorIDFormat(self, sensoridx):
        rr2 = re.compile(r'^0[Xx].$|^0[Xx]..$')
        ac = rr2.findall(sensoridx)
        #print ac
        if ac == []:
            dlg = wx.MessageDialog(None, 'Please check your input value format.\nLike format "0x03" "0x9" "0xE2"', 'Wrong Input format.', wx.OK | wx.ICON_WARNING) 
            dlg.ShowModal()   
            return 'sensor id format error'         
        
        
    
        
    
    def OnSelect_SelectSensorName_Threshold( self, event ):
        self.m_radio_SensorName_Threshoold.SetValue(True)
        self.m_radioBtn_SensorID_Threshold.SetValue(False)
        self.m_radioBtn_SensorList_Threshold.SetValue(False)
        self.m_text_SensorName_Threshold.Enable(True)
        self.m_textCtrl_SenSorID_Thresshold.Enable(False)
        self.m_comboBox_SensorList_Threshold.Enable(False)
        self.m_text_SensorName_Threshold.SetFocus()        
#     
#     def OnSelect_SlectLCRAssert_Threshold( self, event ):
#         self.m_Radiobtn_Normal_Threshold.SetValue(False)
#         self.m_Radiobtn_UCRAssert_Threshold.SetValue(False)  
#         self.m_textCtrl_Input_Threshold.Enable(False)     



    
    def OnSelect_SelectInputManually_Threshold( self, event ):
        pass

#         self.m_Radiobtn_Normal_Threshold.Enable(True)
# #         self.m_Radiobtn_UCRAssert_Threshold.Enable(True)
#         if self.m_checkBox_InputManually.GetValue() == True:
#             self.m_textCtrl_Input_Threshold.Enable(True)
# 
#             self.m_Radiobtn_Normal_Threshold.Enable(False)
# #             self.m_Radiobtn_UCRAssert_Threshold.Enable(False)
#             self.m_textCtr_UNC_Assert_Threshold.Enable(False)
#             self.m_textCtr_UCR_Threshold.Enable(False)
#             self.m_textCtrl_UC_Threshold.Enable(False)
#             self.m_textCtrl_Input_Threshold.SetFocus()
#         elif self.m_checkBox_InputManually.GetValue() == False:
#             self.m_textCtrl_Input_Threshold.Enable(False)

    
    def OnSelect_SelectSensorID_Threshold( self, event ):
        self.m_radio_SensorName_Threshoold.SetValue(False)
        self.m_radioBtn_SensorID_Threshold.SetValue(True)
        self.m_radioBtn_SensorList_Threshold.SetValue(False)
        self.m_text_SensorName_Threshold.Enable(False)
        self.m_textCtrl_SenSorID_Thresshold.Enable(True)
        self.m_comboBox_SensorList_Threshold.Enable(False)
        self.m_textCtrl_SenSorID_Thresshold.SetFocus()
    
    def OnSelect_SelectNormal_Threshold( self, event ):

#         self.m_Radiobtn_UCRAssert_Threshold.SetValue(False)       
        self.m_textCtrl_Input_Threshold.Enable(False)
    
    def OnSelect_SelectfromList_Threshold( self, event ):
        self.m_radio_SensorName_Threshoold.SetValue(False)
        self.m_radioBtn_SensorID_Threshold.SetValue(False)
        self.m_radioBtn_SensorList_Threshold.SetValue(True)
        self.m_text_SensorName_Threshold.Enable(False)
        self.m_textCtrl_SenSorID_Thresshold.Enable(False)
        self.m_comboBox_SensorList_Threshold.Enable(True)
        self._CollectData_ONThresholdPage()             
        discretemessage = [self.ip1, self.userid1, self.password1, self.lanp1, 'sdr elist']         
        OnSelect_SelectFromlist_ThresholdSensor_T(discretemessage)
    
    def OnSelect_SelectUCRAssert_Threshold( self, event ):

        self.m_Radiobtn_Normal_Threshold.SetValue(False)       
        self.m_textCtrl_Input_Threshold.Enable(False)
    
    def OnClick_ClickTest_Threshold( self, event ):
        self._CollectData_ONThresholdPage()
        if self.m_radio_SensorName_Threshoold.GetValue() == True:
            sensornamex = self.m_text_SensorName_Threshold.GetValue()
            if self._CheckSensorNameExites(sensornamex) == 'SensorNamenotExites':
                print 'fff4621841ff'
                return 0
            else:
                sensorid = self.sensorname_id_obtion
        elif self.m_radioBtn_SensorID_Threshold.GetValue() == True:
            sensorid = self.m_textCtrl_SenSorID_Thresshold.GetValue()
            if self._CheckSensorIDFormat(sensorid) == 'sensor id format error':
                return 0
        elif self.m_radioBtn_SensorList_Threshold.GetValue() == True:
            try:
                sensorid = self.sensorname_id_dic[self.m_comboBox_SensorList_Threshold.GetValue()]
                #print sensorid
            except:
                dlg = wx.MessageDialog(None, 'Get Sensor ID from Sensor list Fail.\nPlease use the other way to test.?', 'Get Sensor ID Fail', wx.OK | wx.ICON_WARNING) 
                dlg.ShowModal()
                return 0        
            
        if os.popen('%s -H %s -U %s -P %s -I %s %s' %(IPMItool_Path, self.ip1, self.userid1, self.password1, self.lanp1, 'raw 0x4 0x27 %s' %sensorid) ).read() == '':
            dlg = wx.MessageDialog(None, 'Please make sure you had input a threshold sensor.', 'Get a None Threshold sensor', wx.OK | wx.ICON_WARNING) 
            dlg.ShowModal()               
            self._WarnStatusBar('Warning: Get a None Threshold sensor.')
            return 0    
            
            
        discretemessage = [self.ip1, self.userid1, self.password1, self.lanp1, 'raw 0x4 0x27 %s' %sensorid]
        

        
        self.m_button_Test_Threshold.Enable(False)
        self.m_button_Run_Threshold.Enable(False)
        OnClick_ClickTest_Threshold_T(discretemessage)


    

    
    def OnClick_ClickRun_Thresholld( self, event ):
#         self.m_button_Test_Threshold.Enable(False)

        self._CollectData_ONThresholdPage()
        if self.m_radio_SensorName_Threshoold.GetValue() == True:
            sensornamex = self.m_text_SensorName_Threshold.GetValue()
            if self._CheckSensorNameExites(sensornamex) == 'SensorNamenotExites':
                return 0
            else:
                sensorid = self.sensorname_id_obtion
        elif self.m_radioBtn_SensorID_Threshold.GetValue() == True:
            sensorid = self.m_textCtrl_SenSorID_Thresshold.GetValue()
            if self._CheckSensorIDFormat(sensorid) == 'sensor id format error':
                return 0
        elif self.m_radioBtn_SensorList_Threshold.GetValue() == True:
            try:
                sensorid = self.sensorname_id_dic[self.m_comboBox_SensorList_Threshold.GetValue()]
                #print sensorid
            except:
                dlg = wx.MessageDialog(None, 'Get Sensor ID from Sensor list Fail.\nPlease use the other way to test.?', 'Get Sensor ID Fail', wx.OK | wx.ICON_WARNING) 
                dlg.ShowModal()
                return 0       
#         if  self.m_checkBox_InputManually.GetValue() == True:
#             asserttype = self.m_textCtrl_Input_Threshold.GetValue()
        if self._CheckSensorIDFormat(self.m_textCtrl_Input_Threshold.GetValue()) == 'sensor id format error':
            return 0
# 
#         else:
#             if  self.m_Radiobtn_LCRAssert_Threeshold.GetValue() == True:
#                 asserttype = 'lcr'
#             elif  self.m_Radiobtn_Normal_Threshold.GetValue() == True:
#                 asserttype = 'normal'
#             elif self.m_Radiobtn_UCRAssert_Threshold.GetValue() == True:
#                 asserttype = 'ucr'    

        if os.popen('%s -H %s -U %s -P %s -I %s %s' %(IPMItool_Path, self.ip1, self.userid1, self.password1, self.lanp1, 'raw 0x4 0x27 %s' %sensorid) ).read() == '':
            dlg = wx.MessageDialog(None, 'Please make sure you had input a threshold sensor.', 'Get a None Threshold sensor', wx.OK | wx.ICON_WARNING) 
            dlg.ShowModal()               
            self._WarnStatusBar('Warning: Get a None Threshold sensor.')
            return 0    
                  
            
        self.m_panel6.Enable(False)    
        self.m_panel13.Enable(False)
        self.m_panel14.Enable(False)   
        self.m_panel15.Enable(False)
        self.m_panel20.Enable(False)   
              
        discretemessage = [self.ip1, self.userid1, self.password1, self.lanp1, sensorid, self.m_textCtrl_Input_Threshold.GetValue()]                        
        OnClick_ClickRun_Thresholld_T(discretemessage)
            

        

            
#         except:
#             pass
#         finally:
#             self.m_button_Test_Threshold.Enable(True)
#             self.m_button_Run_Threshold.Enable(True)            
#         
        

    
    def OnClick_ClickSend_TriaggerrCMD( self, event ):
        self._CollectData_ONDiscretePage()
        discretemessage = [self.ip1, self.userid1, self.password1, self.lanp1, self.m_textCtrl_RawData_TriaggerrCMD.GetValue()]
        self.m_panel6.Enable(False)    
        self.m_panel13.Enable(False)
        self.m_panel14.Enable(False)   
        self.m_panel15.Enable(False)
        self.m_panel20.Enable(False)
        OnClick_Send_T(discretemessage)

        
        
    
    def OnClick_StartStress_Stress( self, event ):
        self._InfoStatusBar('Info: Stress is ready to run...') 
        self.ip1 = self.m_textCtrl_ip.GetValue()
        self.userid1 = self.m_textCtrl_userid.GetValue()
        self.password1 = self.m_textCtrl_password.GetValue()
        self.lanp1 = self.m_comboBox_lanp.GetValue()        
        powerlist = {'power off/on' : self.m_checkBox_PowerOnoff_stress.GetValue(), 'power cycle' : self.m_checkBox6.GetValue(), 
                     'power reset' : self.m_checkBox7.GetValue(), 'bmc reset' : self.m_checkBox8.GetValue()}
        cmd1 = []
        if powerlist['power off/on'] == True:
            cmd1.append('power off/on')
        if powerlist['power cycle'] == True:
            cmd1.append('power cycle')
        if powerlist['power reset'] == True:
            cmd1.append('power reset')
        if powerlist['bmc reset'] == True:
            cmd1.append('bmc reset')                
        try:     
            powertimeinterval = int(self.m_textCtrl_onoffTimeInterval_Stress.GetValue())
            bmctimeinterval = int(self.m_textCtrlResetBMCInterVal_Stress.GetValue())
            loops = int(self.m_textCtrl_Loops_Stress.GetValue())  
            if powertimeinterval > 30 and bmctimeinterval > 30:
                pass
            else:
                dlg = wx.MessageDialog(None, 'Please enter the time more than 30s!', 'Wrong number', wx.OK | wx.ICON_WARNING)  
                dlg.ShowModal()                
                return 0
        except:            
            dlg = wx.MessageDialog(None, 'Please enter a number, not a stirng!', 'Wrong format', wx.OK | wx.ICON_WARNING)  
            dlg.ShowModal()
            return 0                          
        discretemessage = [self.ip1, self.userid1, self.password1, self.lanp1, cmd1, powertimeinterval, bmctimeinterval, loops]        
        print Start_Stop_Stress
        dlg = wx.MessageDialog(None, 'Are you sure to start stress?', 'Start stress', wx.YES_NO | wx.ICON_INFORMATION)          
        if dlg.ShowModal() == wx.ID_YES:        
            self.m_panel6.Enable(False) 
            self.m_panel13.Enable(False)
            self.m_panel14.Enable(False)   
            self.m_panel15.Enable(False)
            self.m_checkBox6.Enable(False)
            self.m_checkBox7.Enable(False)
            self.m_checkBox8.Enable(False)
            self.m_checkBox_PowerOnoff_stress.Enable(False)
            self.m_button_StartStress_Stress.Enable(False)
            self.m_button_Stop_Stress.Enable(True)
            self.m_textCtrl_Loops_Stress.Enable(False)
            self.m_textCtrl_onoffTimeInterval_Stress.Enable(False)
            self.m_textCtrlResetBMCInterVal_Stress.Enable(False)
            global Start_Stop_Stress
            Start_Stop_Stress = 'start'
        else:
            return 0
        dlg.Destroy()        
        self._InfoStatusBar('Info: Stress is running...') 
        OnClick_StartStress_Stress_T(discretemessage)
     

    def OnClose_window(self, event):
        global Start_Stop_Stress
        if Start_Stop_Stress == 'start':
            dlg = wx.MessageDialog(None, 'Stress is running...\nPlease stop stress first.', 'Trying to close window', wx.OK | wx.ICON_WARNING)       
            dlg.ShowModal()

        else:
            sys.exit()



    
    def OnClick_Stop_Stress( self, event ):
        dlg = wx.MessageDialog(None, 'Are you sure to stop stress?', 'Stop stress', wx.YES_NO | wx.ICON_WARNING)       
        if dlg.ShowModal() == wx.ID_YES:
            self.m_panel6.Enable(True) 
            self.m_panel13.Enable(True)
            self.m_panel14.Enable(True)   
            self.m_panel15.Enable(True)
            self.m_checkBox6.Enable(True)
            self.m_checkBox7.Enable(True)
            self.m_checkBox8.Enable(True)
            self.m_checkBox_PowerOnoff_stress.Enable(True)
            self.m_button_StartStress_Stress.Enable(True)
            self.m_button_Stop_Stress.Enable(False)
            self.m_textCtrl_Loops_Stress.Enable(True)
            self.m_textCtrl_onoffTimeInterval_Stress.Enable(True)
            self.m_textCtrlResetBMCInterVal_Stress.Enable(True)     
            global Start_Stop_Stress 
            Start_Stop_Stress = 'stop'
            self._InfoStatusBar('Info: Stress has been stoped.')      
        dlg.Destroy()

                    
                    
    def OnClick_DCServer( self, event ):
        self._CollectData_ONDiscretePage()     
        discretemessage = [self.ip1, self.userid1, self.password1, self.lanp1, 'power off', 'power on']        
        dlg = wx.MessageDialog(None, 'Are you sure to power off and power on Server?', 'DC Server', wx.YES_NO | wx.ICON_WARNING)       
        if dlg.ShowModal() == wx.ID_YES:
            OnClick_DCServer_T(discretemessage)
        dlg.Destroy()
    
    def OnClick_ResetBMC( self, event ):
        self._CollectData_ONDiscretePage()     
        discretemessage = [self.ip1, self.userid1, self.password1, self.lanp1, 'raw 0x06 0x02']        
        dlg = wx.MessageDialog(None, 'Are you sure to RESET BMC?', 'Reset BMC', wx.YES_NO | wx.ICON_WARNING)       
        if dlg.ShowModal() == wx.ID_YES:
            OnClick_ResetBMC_T(discretemessage)
        dlg.Destroy()
    
    def OnClick_ClearSELlog( self, event ):
        self._CollectData_ONDiscretePage()     
        discretemessage = [self.ip1, self.userid1, self.password1, self.lanp1, 'sel clear']        
        dlg = wx.MessageDialog(None, 'Are you sure to clear SEL log?', 'Clear SEL log', wx.YES_NO | wx.ICON_WARNING)       
        if dlg.ShowModal() == wx.ID_YES:
            OnClick_ClearSELlog_T(discretemessage)
        dlg.Destroy()
    
    def OnClick_ClearTextResult( self, event ):
        self.m_text_TestResult.Clear()
        self._InfoStatusBar('Text result has been cleared.') 

        

    
    def OnClick_GetSELlog( self, event ):
        self._CollectData_ONDiscretePage()     
        discretemessage = [self.ip1, self.userid1, self.password1, self.lanp1, 'sel list']
        OnClick_GetSELlog_T(discretemessage)

    
    def OnClick_MenuNew( self, event ):
        
        pass
    
    def OnClick_MenuExit( self, event ):
        dlg = wx.MessageDialog(None, 'Are you sure exit this tool?', 'Exit tool', wx.YES_NO | wx.ICON_WARNING)  
        if dlg.ShowModal() == wx.ID_YES:                     
            quit()
    
    def OnClick_MenuIPMItoolPATH( self, event ):    
        class MyDialog2 ( wx.Dialog ):           
                def __init__( self, parent ):
                    wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Select ipmitool Path", pos = wx.DefaultPosition, size = wx.Size( 600,60 ), style = wx.DEFAULT_DIALOG_STYLE )                    
                    self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )                    
                    bSizer28 = wx.BoxSizer( wx.HORIZONTAL )                    
                    self.m_filePicker1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*ipmitool.exe*", wx.DefaultPosition, wx.Size( 450,70 ), wx.FLP_DEFAULT_STYLE )
                    bSizer28.Add( self.m_filePicker1, 0, wx.ALL, 5 )                    
                    self.m_button12_save = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
                    bSizer28.Add( self.m_button12_save, 1, wx.ALL, 5 )                                       
                    self.SetSizer( bSizer28 )
                    self.Layout()                    
                    self.Centre( wx.BOTH )                    
                    # Connect Events
                    self.m_button12_save.Bind( wx.EVT_BUTTON, self.OnCLick_SaveIpmiPath )                
                def __del__( self ):
                    pass               
                # Virtual event handlers, overide them in your derived class
                def OnCLick_SaveIpmiPath( self, event ):
                    global IPMItool_Path
                    IPMItool_Path = self.m_filePicker1.GetPath()
                    CheckIpmiTool()
                    print IPMItool_Path   
                    self.Destroy()        
        ipmipath = MyDialog2(None)
        ipmipath.Show(show=True)
        













        

    
    def OnClick_MenuAbout( self, event ):
        dlg = wx.MessageDialog(None, 'This tool is written by python 2.7.14.', 'About', wx.OK | wx.ICON_INFORMATION)       
        dlg.ShowModal()
    
    def OnClick_MenuHelp( self, event ):
        dlg = wx.MessageDialog(None, 'This tool may not work due to the update of ipmitool or the update of BMC FW.\nIf this happens, please connect to me to update this tool.', 'Help', wx.OK | wx.ICON_INFORMATION)       
        dlg.ShowModal()
        
    def _WarnStatusBar(self, your_status):
        self.m_statusBar.SetStatusText(your_status)
        
    def _InfoStatusBar(self, your_status):
        self.m_statusBar.SetStatusText(your_status)
        
    def _CollectData_ONDiscretePage(self):
        try:
            self.ip1 = self.m_textCtrl_ip.GetValue()
            self.userid1 = self.m_textCtrl_userid.GetValue()
            self.password1 = self.m_textCtrl_password.GetValue()
            self.lanp1 = self.m_comboBox_lanp.GetValue()
            self.sensorname1 = self.m_text_SensorName_Discrete.GetValue()
            self.sensorid1 = self.m_text_SensorID_Discrete.GetValue()
            self.sensorlist1 = self.m_combo_SensorList_Discrete.GetValue()
            self.eventoffsetvalue1 = self.m_combo_EventOffsetValue_Discrete.GetValue()
            self.eventdat = self.m_combo_EventData_Discrete.GetValue() 
        except :
            print '_CollectData_ONDiscretePage Fail'
            self._WarnStatusBar('Waring: Collecting discrete sensor data Fail!')
        else : self._InfoStatusBar('Info: Collecting discrete sensor data has complete!')
        pass

    def _CollectData_ONThresholdPage(self):
        try:
            self.ip1 = self.m_textCtrl_ip.GetValue()
            self.userid1 = self.m_textCtrl_userid.GetValue()
            self.password1 = self.m_textCtrl_password.GetValue()
            self.lanp1 = self.m_comboBox_lanp.GetValue()
            self.sensorname2 = self.m_text_SensorName_Threshold.GetValue()
            self.sensorid2 = self.m_textCtrl_SenSorID_Thresshold.GetValue()
            self.sensorlist2 = self.m_comboBox_SensorList_Threshold.GetValue()
            self.lcrassert = self.m_textCtr_UNC_Assert_Threshold.GetValue()
            self.normalassert = self.m_textCtrl_UC_Threshold.GetValue()
            self.ucrassert = self.m_textCtr_UCR_Threshold.GetValue()
            self.inputassert = self.m_textCtrl_Input_Threshold.GetValue()
        except:
            print '_CollectData_ONThresholdPage Fail'
            self._WarnStatusBar('Waring: Collecting discrete sensor data Fail!')
        else : self._InfoStatusBar('Info: Collecting discrete sensor data has complete!')
                  
        
        

def getcurrenttime():
    return time.strftime("%Y-%m-%d-%Hh-%Mmin-%Ss") 

class RunIpmiCmd():
    def __init__(self, ip, userid, password, lanp, cmd):
        self.ip = ip
        self.userid = userid
        self.password = password
        self.lanp = lanp
        self.cmd = cmd
        self.run()    
    def run(self):
        pub.sendMessage('UpdateText', msg='ipmitool -I %s -H %s -U %s -P %s %s:\n' % (self.lanp, self.ip, self.userid, self.password, self.cmd))
        p = os.popen('%s -I %s -H %s -U %s -P %s %s' % (IPMItool_Path, self.lanp, self.ip, self.userid, self.password, self.cmd)).read()
        if p == '':
            pub.sendMessage('UpdateText', msg='--------------------------Warning:  Get an Empty Value--------------------------\n')
            pass
        else:        
            q = ''
            for lines_1 in p:
                q += lines_1
            self.getData = q
            pub.sendMessage('UpdateText', msg=q)
      
      
      
    
# class RunIpmiCmd():
#     def __init__(self, ip, userid, password, lanp, cmd):
#         self.ip = ip
#         self.userid = userid
#         self.password = password
#         self.lanp = lanp
#         self.cmd = cmd
#         self.run()
#     def run(self):
#         pub.sendMessage('UpdateText', msg='ipmitool -I %s -H %s -U %s -P %s %s:\n' % (self.lanp, self.ip, self.userid, self.password, self.cmd))
#         
#         p = subprocess.Popen('ipmitool -I %s -H %s -U %s -P %s %s' % (self.lanp, self.ip, self.userid, self.password, self.cmd), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         time.sleep(5)
# #         #print p.stdout.readline()
# #         while p.poll() is None:
# # #             if p.poll() is None:
# # #                 break
# #             print 'sssssssssss'
# #             time.sleep(1)
#         p_stderr = p.stderr.readlines()
#         p_stdout = p.stdout.readlines()
#         print 'aaa'
#         if p_stderr == '':            
#             print 'bbb'
#             msgg = ''
#             for line in p_stderr :
#                 msgg += line
#             pub.sendMessage('UpdateText', msg=msgg)            
#             dlg = wx.MessageDialog(None, 'Fail to execute IPMI CMD\n Please Check..', 'Fail to execute IPMI CMD', wx.OK | wx.ICON_ERROR)       
#             dlg.ShowModal() 
#             pub.sendMessage('UpdateText', msg='FailExecuteIPMICMD')
#         else:        
#             msgg = ''
#             for line in p_stdout :
#                 msgg += line
#             pub.sendMessage('UpdateText', msg=msgg)
#             print 'ccc'
#         print 'ddd'
class OnClick_ClearSELlog_T(Thread):
    def __init__(self, wds):
        self.wds = wds
        Thread.__init__(self)
        self.start()
    def run(self):
        pub.sendMessage('UpdateText', msg='\n###Start Clear sel log from Server at time: %s###\nPlease wiat...\n'% getcurrenttime())
        RunIpmiCmd(self.wds[0], self.wds[1], self.wds[2], self.wds[3], self.wds[4])
        pub.sendMessage('UpdateText', msg='###finish Clear sel log from Server  at time: %s###\n'% getcurrenttime())
            

    
class OnClick_GetSELlog_T(Thread):
    def __init__(self, wds):
        self.wds = wds
        Thread.__init__(self)
        self.start()
    def run(self):
        pub.sendMessage('UpdateText', msg='\n###Start Getting sel log from Server at time: %s###\nPlease wiat...\n'% getcurrenttime())
        RunIpmiCmd(self.wds[0], self.wds[1], self.wds[2], self.wds[3], self.wds[4])
        pub.sendMessage('UpdateText', msg='###finish Getting sel log from Server  at time: %s###\n'% getcurrenttime())

class OnClick_ResetBMC_T(Thread):
    def __init__(self, wds):
        self.wds = wds
        Thread.__init__(self)
        self.start()
    def run(self):
        pub.sendMessage('UpdateText', msg='\n###Start Reset BMC at time: %s###\n'% getcurrenttime())
        RunIpmiCmd(self.wds[0], self.wds[1], self.wds[2], self.wds[3], self.wds[4])
        pub.sendMessage('UpdateText', msg='###Reset BMC CMD has been sent completely at time: %s###\n'% getcurrenttime())

class OnClick_DCServer_T(Thread):
    def __init__(self, wds):
        self.wds = wds
        Thread.__init__(self)
        self.start()
    def run(self):
        pub.sendMessage('UpdateText', msg='\n###Start DC Server at time: %s###\n'% getcurrenttime())
        pub.sendMessage('UpdateText', msg='#Start Power off Server at time: %s###\n'% getcurrenttime())
        RunIpmiCmd(self.wds[0], self.wds[1], self.wds[2], self.wds[3], self.wds[4])
        time.sleep(15)
        pub.sendMessage('UpdateText', msg='\n#Start Power on Server at time: %s###\n'% getcurrenttime())
        RunIpmiCmd(self.wds[0], self.wds[1], self.wds[2], self.wds[3], self.wds[5])        
        pub.sendMessage('UpdateText', msg='###DC Server CMD has been sent completely at time: %s###\n'% getcurrenttime())    

      
class OnSelect_SelectFromlist_DiscreteSensor_T(Thread):
    def __init__(self, wds):
        self.wds = wds
        Thread.__init__(self)
        self.start()
    def run(self):
        pub.sendMessage('UpdateText', msg='\n###Start Getting sdr elist from Server at time: %s###\nPlease wiat...\n'% getcurrenttime())     
        pub.sendMessage('UpdateText', msg='SdrElist_receiving') 
        try:
            SDR_ELIST.put(RunIpmiCmd(self.wds[0], self.wds[1], self.wds[2], self.wds[3], self.wds[4]).getData) 
            pub.sendMessage('UpdateText', msg='SdrElist')
        except :
            pub.sendMessage('UpdateText', msg='SdrElist_fail')
        pub.sendMessage('UpdateText', msg='###Finish Getting sdr elist from Server at time: %s###'%getcurrenttime())
        pub.sendMessage('UpdateText', msg='SdrElist_done')
        

class OnSelect_SelectFromlist_ThresholdSensor_T(Thread):
    def __init__(self, wds):
        self.wds = wds
        Thread.__init__(self)
        self.start()
    def run(self):
        pub.sendMessage('UpdateText', msg='\n###Start Getting sdr elist from Server at time: %s###\nPlease wiat...\n'% getcurrenttime())     
        pub.sendMessage('UpdateText', msg='SdrElist_receiving2') 
        try:
            SDR_ELIST.put(RunIpmiCmd(self.wds[0], self.wds[1], self.wds[2], self.wds[3], self.wds[4]).getData) 
            pub.sendMessage('UpdateText', msg='SdrElist2')
        except:
            pub.sendMessage('UpdateText', msg='SdrElist_fail')
        pub.sendMessage('UpdateText', msg='###Finish Getting sdr elist from Server at time: %s###'%getcurrenttime())
        pub.sendMessage('UpdateText', msg='SdrElist_done2')

class OnClick_DiscreteSensorTest_T(Thread):
    def __init__(self, wds):
        self.wds = wds
        Thread.__init__(self)
        self.start()
    def run(self):            
        pub.sendMessage('UpdateText', msg='\n###Begin discrete sensor test at %s###\n'% getcurrenttime())
        pub.sendMessage('UpdateText', msg='\n#begin sensor test oem command\n')
        RunIpmiCmd(self.wds[0], self.wds[1], self.wds[2], self.wds[3], self.wds[4][0])
        time.sleep(3)
        pub.sendMessage('UpdateText', msg='\n#get sensor state oem command\n')
        RunIpmiCmd(self.wds[0], self.wds[1], self.wds[2], self.wds[3], self.wds[4][1])
        time.sleep(3)
        pub.sendMessage('UpdateText', msg='\n#stop polling sensor oem command\n')
        RunIpmiCmd(self.wds[0], self.wds[1], self.wds[2], self.wds[3], self.wds[4][2])   
        time.sleep(3)           
        pub.sendMessage('UpdateText', msg='\n#set sensor test to the offset oem command\n')
        RunIpmiCmd(self.wds[0], self.wds[1], self.wds[2], self.wds[3], self.wds[4][3])     
        time.sleep(6)
        if self.wds[4][4] != '':
            pub.sendMessage('UpdateText', msg='\n#End Sensor test oem command\n')
            RunIpmiCmd(self.wds[0], self.wds[1], self.wds[2], self.wds[3], self.wds[4][4])    
            time.sleep(1) 
        pub.sendMessage('UpdateText', msg='\n###finish discrete sensor test cmd at %s###\n'% getcurrenttime())  
        time.sleep(1)
        pub.sendMessage('UpdateText', msg='discreteDone')          
       
class OnClick_ClickTest_Threshold_T(Thread):
    def __init__(self, wds):
        self.wds = wds
        Thread.__init__(self)
        self.start()
    def run(self):            
        pub.sendMessage('UpdateText', msg='\n###Begin to check the Threshold sensor LCR UCR Value at %s###\n'% getcurrenttime())
        #print 'ipmitool -H %s -U %s -P %s -I %s %s' % (self.wds[0], self.wds[1], self.wds[2], self.wds[3], self.wds[4])
        p = os.popen('%s -H %s -U %s -P %s -I %s %s' % (IPMItool_Path, self.wds[0], self.wds[1], self.wds[2], self.wds[3], self.wds[4])).read()
        if p == '':
            dlg = wx.MessageDialog(None, 'Please make sure your sensor is Threshold sensor.', 'Not Threshold sensor', wx.OK | wx.ICON_WARNING)       
            dlg.ShowModal()
            pub.sendMessage('UpdateText', msg='Fail_Test_LCR_UCR_Done')
            pub.sendMessage('UpdateText', msg='Test_LCR_UCR_Done')
            return 'NotThresholdSensor'
        else:
            #print p
            aaa = str(p)
            aaa = aaa.strip().lstrip().rstrip()
            
            Threshold_LNC.put(aaa[3:5])
            Threshold_LC.put(aaa[6:8])
            Threshold_LNR.put(aaa[9:11])
            Threshold_UNC.put(aaa[12:14])
            Threshold_UC.put(aaa[15:17])
            Threshold_UNR.put(aaa[18:])
            
            pub.sendMessage('UpdateText', msg='ipmitool -H %s -U %s -P %s -I %s %s\n' % (self.wds[0], self.wds[1], self.wds[2], self.wds[3], self.wds[4])) 
            pub.sendMessage('UpdateText', msg=aaa) 
            pub.sendMessage('UpdateText', msg='Threshold_LCR_UCR') 
        pub.sendMessage('UpdateText', msg='Test_LCR_UCR_Done')
        pub.sendMessage('UpdateText', msg='\n###Finish to check the Threshold sensor LCR UCR Value at %s###\n'% getcurrenttime()) 
        
    

class OnClick_ClickRun_Thresholld_T(Thread):
    def __init__(self, wds):
        self.wds = wds
        Thread.__init__(self)
        self.start()
    def run(self):      
        sensorid = self.wds[4]
        #print sensorid
        p = os.popen('%s -H %s -U %s -P %s -I %s %s' % (IPMItool_Path, self.wds[0], self.wds[1], self.wds[2], self.wds[3], 'raw 0x4 0x27 %s'%sensorid)).read()
        if p == '':
            pub.sendMessage('UpdateText', msg='ThresholdSensor_run')
            dlg = wx.MessageDialog(None, 'Please make sure your sensor is Threshold sensor.', 'Not Threshold sensor', wx.OK | wx.ICON_WARNING)       
            dlg.ShowModal()
            
        else:        
            aaa = str(p)
            aaa = aaa.strip().lstrip().rstrip()

            
            
            Threshold_LNC.put(aaa[3:5])
            Threshold_LC.put(aaa[6:8])
            Threshold_LNR.put(aaa[9:11])
            Threshold_UNC.put(aaa[12:14])
            Threshold_UC.put(aaa[15:17])
            Threshold_UNR.put(aaa[18:])
            
#discretemessage = [self.ip1, self.userid1, self.password1, self.lanp1, sensorid, self.m_textCtrl_Input_Threshold.GetValue()]            
            
            

            pub.sendMessage('UpdateText', msg='###Checking Threshold sensor LCR UCR value:\n')
            pub.sendMessage('UpdateText', msg='ipmitool -H %s -U %s -P %s -I %s raw 0x4 0x27 %s\n' % (self.wds[0], self.wds[1], self.wds[2], self.wds[3], self.wds[4])) 
            pub.sendMessage('UpdateText', msg=aaa) 
            pub.sendMessage('UpdateText', msg='Threshold_LCR_UCR') 
            lcr_ucr_offset = self.wds[5]
        cmd1= ['raw 0x3a 0x17 0x0', 'raw 0x3a 0x17 0x4', 'raw 0x3a 0x17 0x5 %s' %sensorid, 'raw 0x3a 0x17 0x1 %s %s' %(sensorid, lcr_ucr_offset)]
        pub.sendMessage('UpdateText', msg='\n\n###Begin Threshold sensor test at %s###\n'% getcurrenttime())
        pub.sendMessage('UpdateText', msg='\n#begin sensor test oem command\n')
        RunIpmiCmd(self.wds[0], self.wds[1], self.wds[2], self.wds[3], cmd1[0])
        time.sleep(3)
        pub.sendMessage('UpdateText', msg='\n#get sensor state oem command\n')
        RunIpmiCmd(self.wds[0], self.wds[1], self.wds[2], self.wds[3], cmd1[1])
        time.sleep(3)
        pub.sendMessage('UpdateText', msg='\n#stop polling sensor oem command\n')
        RunIpmiCmd(self.wds[0], self.wds[1], self.wds[2], self.wds[3], cmd1[2])   
        time.sleep(3)           
        pub.sendMessage('UpdateText', msg='\n#set the current reading value of the sensor out of the threshold\n')
        RunIpmiCmd(self.wds[0], self.wds[1], self.wds[2], self.wds[3], cmd1[3])     
        time.sleep(3)
        pub.sendMessage('UpdateText', msg='\n###Finish setting the current reading value of the sensor out of the threshold at %s###\n'% getcurrenttime())  
        pub.sendMessage('UpdateText', msg='\nSensorid: %s\nSet sensor reading value: %s'%(sensorid.upper(), lcr_ucr_offset.upper())) 
        time.sleep(1)
        pub.sendMessage('UpdateText', msg='ThresholdDone')                          
        pub.sendMessage('UpdateText', msg='ThresholdSensor_run')
      
class OnClick_Send_T(Thread):
    def __init__(self, wds):
        self.wds = wds
        Thread.__init__(self)
        self.start()
    def run(self):      
        pub.sendMessage('UpdateText', msg='\n###Begin to send IPMI CMD to Server at time: %s###\n'% (getcurrenttime())) 
        RunIpmiCmd(self.wds[0], self.wds[1], self.wds[2], self.wds[3], self.wds[4])
        pub.sendMessage('UpdateText', msg='Send_IPMI_CMD_Done')
        pub.sendMessage('UpdateText', msg='###Finish to send IPMI CMD to Server at time: %s###\n'% (getcurrenttime()) )

class OnClick_StartStress_Stress_T(Thread):
    def __init__(self, wds):
        self.wds = wds
        Thread.__init__(self)
        self.start()
    def run(self):      
        pub.sendMessage('UpdateText', msg='\n###Begin to Run stress at time: %s###\n'% (getcurrenttime())) 
        #RunIpmiCmd(self.wds[0], self.wds[1], self.wds[2], self.wds[3], self.wds[4])
        powertimeinterval = self.wds[5]
        bmctimeinterval = self.wds[6]
        loops = self.wds[7]       
        loop = 0
        loop1 = 1
        if loops == 0:
            pass
        else:
            loop1 = loops
        while Start_Stop_Stress == 'start' and loop1 != 0:
            loop += 1
            if loops == 0:
                pass
            else:
                loop1 -= 1                            
            for poweraction in self.wds[4]:
                if poweraction == 'power off/on':              
                    pub.sendMessage('UpdateText', msg='\nThe %s time for running power off/on at time: %s\n'%(loop, getcurrenttime()))
                    RunIpmiCmd(self.wds[0], self.wds[1], self.wds[2], self.wds[3], 'power off')
                    for i in range(30):
                        time.sleep(1)
                        if Start_Stop_Stress == 'stop': 
                            return 0
                    RunIpmiCmd(self.wds[0], self.wds[1], self.wds[2], self.wds[3], 'power on')
                    for i in range(powertimeinterval):
                        time.sleep(1)
                        if Start_Stop_Stress == 'stop': 
                            pub.sendMessage('UpdateText', msg='\n###Stop stress manually at time %s###' %getcurrenttime())
                            return 0
                if poweraction == 'power cycle':
                    pub.sendMessage('UpdateText', msg='\nThe %s time for running power cycle at time: %s\n'%(loop, getcurrenttime()))
                    RunIpmiCmd(self.wds[0], self.wds[1], self.wds[2], self.wds[3], 'power cycle')
                    for i in range(powertimeinterval):
                        time.sleep(1)
                        if Start_Stop_Stress == 'stop': 
                            pub.sendMessage('UpdateText', msg='###Stop stress manually at time %s###' %getcurrenttime())
                            return 0
                if poweraction == 'power reset':
                    pub.sendMessage('UpdateText', msg='\nThe %s time for running power reset at time: %s\n'%(loop, getcurrenttime()))
                    RunIpmiCmd(self.wds[0], self.wds[1], self.wds[2], self.wds[3], 'power reset')
                    for i in range(powertimeinterval):
                        time.sleep(1)
                        if Start_Stop_Stress == 'stop': 
                            pub.sendMessage('UpdateText', msg='###Stop stress manually at time %s###' %getcurrenttime())
                            return 0                
                if poweraction == 'bmc reset':
                    pub.sendMessage('UpdateText', msg='\nThe %s time for running BMC reset at time: %s\n'%(loop, getcurrenttime()))
                    RunIpmiCmd(self.wds[0], self.wds[1], self.wds[2], self.wds[3], 'raw 0x6 0x2')
                    for i in range(bmctimeinterval):
                        time.sleep(1)
                        if Start_Stop_Stress == 'stop': 
                            pub.sendMessage('UpdateText', msg='###Stop stress manually at time %s###' %getcurrenttime())
                            return 0                        
        pub.sendMessage('UpdateText', msg='Run_stress_Done')     
        global Start_Stop_Stress 
        Start_Stop_Stress = 'stop'           
        pub.sendMessage('UpdateText', msg='###Finish to Run stress at time: %s###\n'% (getcurrenttime()) )    
        #discretemessage = [self.ip1, self.userid1, self.password1, self.lanp1, cmd1, powertimeinterval, bmctimeinterval, loops]
        
         
        
class CheckIpmiTool(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.start()
    def run(self):                                 
        q = os.popen('%s -V'% IPMItool_Path).read()
        if q != '':
            pub.sendMessage('UpdateText', msg='\n'+q+'\nIpmitool is ready to use!\n')
            pub.sendMessage('UpdateText', msg='\n###########################################################\n\n')
            
        else:
            pub.sendMessage('UpdateText', msg='\nFailed to get ipmitool. \n1. You can set the ipmitool path at "Menu-> Setting-> IPMItool path" or add it to OS PATH.\n2. You can put the tool in the same folder with ipmitool.')
        

if __name__ == '__main__':
    app = wx.App()
    myfram= MyFrame1(None)
    myfram.Show(show=True)
    app.MainLoop()
