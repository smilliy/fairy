# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Add User Tool", pos=wx.DefaultPosition,
                          size=wx.Size(900, 600), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        #self.SetSizeHintsSz(wx.Size(900, 600), wx.Size(900, 600))
        self.SetSizeHints(wx.Size(900, 600), wx.Size(900, 600))
        self.SetBackgroundColour(wx.Colour(127, 127, 127))

        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_panel14 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(700, 600), wx.TAB_TRAVERSAL)
        self.m_panel14.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVEBORDER))
        self.m_panel14.SetMinSize(wx.Size(700, 600))
        self.m_panel14.SetMaxSize(wx.Size(700, 600))

        bSizer14 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel3 = wx.Panel(self.m_panel14, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 150), wx.TAB_TRAVERSAL)
        self.m_panel3.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))
        self.m_panel3.SetMinSize(wx.Size(-1, 150))
        self.m_panel3.SetMaxSize(wx.Size(-1, 150))

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Output:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        self.m_staticText1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer3.Add(self.m_staticText1, 0, wx.ALL, 5)

        self.m_outputtext = wx.TextCtrl(self.m_panel3, wx.ID_ANY,
                                        u"########################\n     Welcome to use this tool. \n########################\n",
                                        wx.DefaultPosition, wx.Size(700, 280), wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY)
        self.m_outputtext.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        self.m_outputtext.SetMinSize(wx.Size(700, 280))
        self.m_outputtext.SetMaxSize(wx.Size(700, 280))

        bSizer3.Add(self.m_outputtext, 1, wx.ALL | wx.EXPAND, 5)

        self.m_panel3.SetSizer(bSizer3)
        self.m_panel3.Layout()
        bSizer14.Add(self.m_panel3, 1, wx.EXPAND | wx.ALL, 5)

        self.m_staticText30 = wx.StaticText(self.m_panel14, wx.ID_ANY, u"Add User Individually:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText30.Wrap(-1)
        self.m_staticText30.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer14.Add(self.m_staticText30, 0, wx.ALL, 5)

        self.m_panel4 = wx.Panel(self.m_panel14, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel5 = wx.Panel(self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel5.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_panel8 = wx.Panel(self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText9 = wx.StaticText(self.m_panel8, wx.ID_ANY, u"UserID:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)
        bSizer10.Add(self.m_staticText9, 0, wx.ALL, 5)

        m_useridChoices = []
        self.m_userid = wx.ComboBox(self.m_panel8, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, m_useridChoices,
                                    0)
        bSizer10.Add(self.m_userid, 0, wx.ALL, 5)

        self.m_staticText251 = wx.StaticText(self.m_panel8, wx.ID_ANY, u"SNMP V3:", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.m_staticText251.Wrap(-1)
        bSizer10.Add(self.m_staticText251, 0, wx.ALL, 5)

        self.m_staticText10 = wx.StaticText(self.m_panel8, wx.ID_ANY, u"Authentication protocol：", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)
        bSizer10.Add(self.m_staticText10, 0, wx.ALL, 5)

        m_authprotocolChoices = []
        self.m_authprotocol = wx.ComboBox(self.m_panel8, wx.ID_ANY, u"HMAC-SHA", wx.DefaultPosition, wx.DefaultSize,
                                          m_authprotocolChoices, 0)
        bSizer10.Add(self.m_authprotocol, 0, wx.ALL, 5)

        self.m_staticText11 = wx.StaticText(self.m_panel8, wx.ID_ANY, u"Address for traps:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        bSizer10.Add(self.m_staticText11, 0, wx.ALL, 5)

        self.m_tripIP1 = wx.TextCtrl(self.m_panel8, wx.ID_ANY, u"10.245.19.39", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer10.Add(self.m_tripIP1, 0, wx.ALL, 5)

        self.m_panel8.SetSizer(bSizer10)
        self.m_panel8.Layout()
        bSizer10.Fit(self.m_panel8)
        bSizer7.Add(self.m_panel8, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel81 = wx.Panel(self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer101 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText91 = wx.StaticText(self.m_panel81, wx.ID_ANY, u"Username：", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText91.Wrap(-1)
        bSizer101.Add(self.m_staticText91, 0, wx.ALL, 5)

        self.m_username = wx.TextCtrl(self.m_panel81, wx.ID_ANY, u"test1", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer101.Add(self.m_username, 0, wx.ALL, 5)

        self.m_staticText81 = wx.StaticText(self.m_panel81, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText81.Wrap(-1)
        bSizer101.Add(self.m_staticText81, 0, wx.ALL, 5)

        self.m_staticText101 = wx.StaticText(self.m_panel81, wx.ID_ANY, u"Privacy protocol：", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText101.Wrap(-1)
        bSizer101.Add(self.m_staticText101, 0, wx.ALL, 5)

        m_privprotocolChoices = []
        self.m_privprotocol = wx.ComboBox(self.m_panel81, wx.ID_ANY, u"CBC-DES", wx.DefaultPosition, wx.DefaultSize,
                                          m_privprotocolChoices, 0)
        bSizer101.Add(self.m_privprotocol, 0, wx.ALL, 5)

        self.m_staticText281 = wx.StaticText(self.m_panel81, wx.ID_ANY, u"Add Single User:", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText281.Wrap(-1)
        bSizer101.Add(self.m_staticText281, 0, wx.ALL, 5)

        self.m_applay = wx.Button(self.m_panel81, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer101.Add(self.m_applay, 0, wx.ALL, 5)

        self.m_panel81.SetSizer(bSizer101)
        self.m_panel81.Layout()
        bSizer101.Fit(self.m_panel81)
        bSizer7.Add(self.m_panel81, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel82 = wx.Panel(self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer102 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText92 = wx.StaticText(self.m_panel82, wx.ID_ANY, u"Password：", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText92.Wrap(-1)
        bSizer102.Add(self.m_staticText92, 0, wx.ALL, 5)

        self.m_userpassword = wx.TextCtrl(self.m_panel82, wx.ID_ANY, u"Passw0rd1!", wx.DefaultPosition, wx.DefaultSize,
                                          0)
        bSizer102.Add(self.m_userpassword, 0, wx.ALL, 5)

        self.m_staticText262 = wx.StaticText(self.m_panel82, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText262.Wrap(-1)
        bSizer102.Add(self.m_staticText262, 0, wx.ALL, 5)

        self.m_staticText102 = wx.StaticText(self.m_panel82, wx.ID_ANY, u"Privacy password:", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText102.Wrap(-1)
        bSizer102.Add(self.m_staticText102, 0, wx.ALL, 5)

        self.m_privpassword = wx.TextCtrl(self.m_panel82, wx.ID_ANY, u"Passw0rd1!", wx.DefaultPosition, wx.DefaultSize,
                                          0)
        bSizer102.Add(self.m_privpassword, 0, wx.ALL, 5)

        self.m_staticText112 = wx.StaticText(self.m_panel82, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText112.Wrap(-1)
        bSizer102.Add(self.m_staticText112, 0, wx.ALL, 5)

        self.m_panel82.SetSizer(bSizer102)
        self.m_panel82.Layout()
        bSizer102.Fit(self.m_panel82)
        bSizer7.Add(self.m_panel82, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel83 = wx.Panel(self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer103 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText83 = wx.StaticText(self.m_panel83, wx.ID_ANY, u"Authority level：", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText83.Wrap(-1)
        bSizer103.Add(self.m_staticText83, 0, wx.ALL, 5)

        m_authorlevelChoices = []
        self.m_authorlevel = wx.ComboBox(self.m_panel83, wx.ID_ANY, u"ro", wx.DefaultPosition, wx.DefaultSize,
                                         m_authorlevelChoices, 0)
        bSizer103.Add(self.m_authorlevel, 0, wx.ALL, 5)

        self.m_staticText271 = wx.StaticText(self.m_panel83, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText271.Wrap(-1)
        bSizer103.Add(self.m_staticText271, 0, wx.ALL, 5)

        self.m_staticText24 = wx.StaticText(self.m_panel83, wx.ID_ANY, u"Access type:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText24.Wrap(-1)
        bSizer103.Add(self.m_staticText24, 0, wx.ALL, 5)

        m_accesstypeChoices = []
        self.m_accesstype = wx.ComboBox(self.m_panel83, wx.ID_ANY, u"Get", wx.DefaultPosition, wx.DefaultSize,
                                        m_accesstypeChoices, 0)
        bSizer103.Add(self.m_accesstype, 0, wx.ALL, 5)

        self.m_panel83.SetSizer(bSizer103)
        self.m_panel83.Layout()
        bSizer103.Fit(self.m_panel83)
        bSizer7.Add(self.m_panel83, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel5.SetSizer(bSizer7)
        self.m_panel5.Layout()
        bSizer7.Fit(self.m_panel5)
        bSizer4.Add(self.m_panel5, 1, wx.EXPAND | wx.ALL, 5)

        self.m_templatesetting = wx.StaticText(self.m_panel4, wx.ID_ANY,
                                               u"User Template for test case \"LXCC_CLI-users\". Trap address needed: ",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_templatesetting.Wrap(-1)
        self.m_templatesetting.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer4.Add(self.m_templatesetting, 0, wx.ALL, 5)

        self.m_panel16 = wx.Panel(self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel16.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_panel17 = wx.Panel(self.m_panel16, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer18 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText301 = wx.StaticText(self.m_panel17, wx.ID_ANY, u"Template Settings:", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText301.Wrap(-1)
        bSizer18.Add(self.m_staticText301, 0, wx.ALL, 5)

        self.m_gettemplate = wx.Button(self.m_panel17, wx.ID_ANY, u"Get Template", wx.DefaultPosition, wx.DefaultSize,
                                       0)
        bSizer18.Add(self.m_gettemplate, 0, wx.ALL, 5)

        self.m_panel17.SetSizer(bSizer18)
        self.m_panel17.Layout()
        bSizer18.Fit(self.m_panel17)
        bSizer13.Add(self.m_panel17, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel141 = wx.Panel(self.m_panel16, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer15 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText34 = wx.StaticText(self.m_panel141, wx.ID_ANY, u"Address for traps:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText34.Wrap(-1)
        bSizer15.Add(self.m_staticText34, 0, wx.ALL, 5)

        self.m_trapIP2 = wx.TextCtrl(self.m_panel141, wx.ID_ANY, u"10.245.19.39", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer15.Add(self.m_trapIP2, 0, wx.ALL, 5)

        self.m_panel141.SetSizer(bSizer15)
        self.m_panel141.Layout()
        bSizer15.Fit(self.m_panel141)
        bSizer13.Add(self.m_panel141, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel151 = wx.Panel(self.m_panel16, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer16 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText36 = wx.StaticText(self.m_panel151, wx.ID_ANY, u"Add Template Users:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText36.Wrap(-1)
        bSizer16.Add(self.m_staticText36, 0, wx.ALL, 5)

        self.m_applayTemplate = wx.Button(self.m_panel151, wx.ID_ANY, u"Apply Template", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        bSizer16.Add(self.m_applayTemplate, 0, wx.ALL, 5)

        self.m_panel151.SetSizer(bSizer16)
        self.m_panel151.Layout()
        bSizer16.Fit(self.m_panel151)
        bSizer13.Add(self.m_panel151, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel161 = wx.Panel(self.m_panel16, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer17 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText38 = wx.StaticText(self.m_panel161, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText38.Wrap(-1)
        bSizer17.Add(self.m_staticText38, 0, wx.ALL, 5)

        self.m_panel161.SetSizer(bSizer17)
        self.m_panel161.Layout()
        bSizer17.Fit(self.m_panel161)
        bSizer13.Add(self.m_panel161, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel16.SetSizer(bSizer13)
        self.m_panel16.Layout()
        bSizer13.Fit(self.m_panel16)
        bSizer4.Add(self.m_panel16, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel4.SetSizer(bSizer4)
        self.m_panel4.Layout()
        bSizer4.Fit(self.m_panel4)
        bSizer14.Add(self.m_panel4, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel14.SetSizer(bSizer14)
        self.m_panel14.Layout()
        bSizer11.Add(self.m_panel14, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel15 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(200, 600), wx.TAB_TRAVERSAL)
        self.m_panel15.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))
        self.m_panel15.SetMinSize(wx.Size(200, 600))
        self.m_panel15.SetMaxSize(wx.Size(200, 600))

        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText23 = wx.StaticText(self.m_panel15, wx.ID_ANY, u"IP:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText23.Wrap(-1)
        bSizer12.Add(self.m_staticText23, 0, wx.ALL, 5)

        self.m_xccip = wx.TextCtrl(self.m_panel15, wx.ID_ANY, u"10.245.16.256", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.m_xccip, 0, wx.ALL, 5)

        self.m_staticText25 = wx.StaticText(self.m_panel15, wx.ID_ANY, u"UserName:", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText25.Wrap(-1)
        bSizer12.Add(self.m_staticText25, 0, wx.ALL, 5)

        m_xccuseridChoices = []
        self.m_xccuserid = wx.ComboBox(self.m_panel15, wx.ID_ANY, u"USERID", wx.DefaultPosition, wx.DefaultSize,
                                       m_xccuseridChoices, 0)
        bSizer12.Add(self.m_xccuserid, 0, wx.ALL, 5)

        self.m_staticText26 = wx.StaticText(self.m_panel15, wx.ID_ANY, u"Password:", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.m_staticText26.Wrap(-1)
        bSizer12.Add(self.m_staticText26, 0, wx.ALL, 5)

        m_xccpasswordChoices = []
        self.m_xccpassword = wx.ComboBox(self.m_panel15, wx.ID_ANY, u"PASSW0RD", wx.DefaultPosition, wx.DefaultSize,
                                         m_xccpasswordChoices, 0)
        bSizer12.Add(self.m_xccpassword, 0, wx.ALL, 5)

        self.m_staticText27 = wx.StaticText(self.m_panel15, wx.ID_ANY, u"Port:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText27.Wrap(-1)
        bSizer12.Add(self.m_staticText27, 0, wx.ALL, 5)

        self.m_xccport = wx.TextCtrl(self.m_panel15, wx.ID_ANY, u"22", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.m_xccport, 0, wx.ALL, 5)

        self.m_staticText29 = wx.StaticText(self.m_panel15, wx.ID_ANY, u"Enable SNMP:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText29.Wrap(-1)
        bSizer12.Add(self.m_staticText29, 0, wx.ALL, 5)

        self.m_snmpbutton = wx.Button(self.m_panel15, wx.ID_ANY, u"Enable", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.m_snmpbutton, 0, wx.ALL, 5)

        self.m_staticText28 = wx.StaticText(self.m_panel15, wx.ID_ANY, u"Log in/out:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText28.Wrap(-1)
        bSizer12.Add(self.m_staticText28, 0, wx.ALL, 5)

        self.m_xccloginout = wx.Button(self.m_panel15, wx.ID_ANY, u"Log in", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.m_xccloginout, 0, wx.ALL, 5)

        self.m_staticText40 = wx.StaticText(self.m_panel15, wx.ID_ANY,
                                            u"\n\n\n\nWritten by Python \n         --PA BMC Team", wx.DefaultPosition,
                                            wx.DefaultSize, wx.ALIGN_CENTRE)
        self.m_staticText40.Wrap(-1)
        self.m_staticText40.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_CAPTIONTEXT))

        bSizer12.Add(self.m_staticText40, 1, wx.ALL | wx.EXPAND, 5)

        self.m_panel15.SetSizer(bSizer12)
        self.m_panel15.Layout()
        bSizer11.Add(self.m_panel15, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer11)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_applay.Bind(wx.EVT_BUTTON, self.applay_single_user_click)
        self.m_gettemplate.Bind(wx.EVT_BUTTON, self.get_template_click)
        self.m_applayTemplate.Bind(wx.EVT_BUTTON, self.applay_template_click)
        self.m_snmpbutton.Bind(wx.EVT_BUTTON, self.snmp_enable_click)
        self.m_xccloginout.Bind(wx.EVT_BUTTON, self.log_in_out_click)
        self.m_authorlevel.Bind(wx.EVT_COMBOBOX, self.auth_level_click)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def auth_level_click(self, event):
        event.Skip()

    def applay_single_user_click(self, event):
        event.Skip()

    def get_template_click(self, event):
        event.Skip()

    def applay_template_click(self, event):
        event.Skip()

    def snmp_enable_click(self, event):
        event.Skip()

    def log_in_out_click(self, event):
        event.Skip()


class MyDialog2(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"-custom settings", pos=wx.DefaultPosition,
                           size=wx.Size(500, 300), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.Size(500, 300), wx.Size(500, 300))

        bSizer16 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText30 = wx.StaticText(self, wx.ID_ANY,
                                            u"-a       - authority level (super, ro, custom:am|rca|rcvma|pr|cel|bc|nsc|ac)",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText30.Wrap(-1)
        self.m_staticText30.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer16.Add(self.m_staticText30, 0, wx.ALL, 5)

        self.m_checkBox1_am = wx.CheckBox(self, wx.ID_ANY, u"am    - User account management access",
                                          wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer16.Add(self.m_checkBox1_am, 0, wx.ALL, 5)

        self.m_checkBox2_rca = wx.CheckBox(self, wx.ID_ANY, u"rca   - Remote console access", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        bSizer16.Add(self.m_checkBox2_rca, 0, wx.ALL, 5)

        self.m_checkBox3_rcvma = wx.CheckBox(self, wx.ID_ANY,
                                             u"rcvma - Remote console and remote disk (virtual media) access",
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer16.Add(self.m_checkBox3_rcvma, 0, wx.ALL, 5)

        self.m_checkBox4_pr = wx.CheckBox(self, wx.ID_ANY, u"pr    - Remote server power/restart access",
                                          wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer16.Add(self.m_checkBox4_pr, 0, wx.ALL, 5)

        self.m_checkBox5_cel = wx.CheckBox(self, wx.ID_ANY, u"cel   - Ability to clear event logs", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        bSizer16.Add(self.m_checkBox5_cel, 0, wx.ALL, 5)

        self.m_checkBox6_bc = wx.CheckBox(self, wx.ID_ANY, u"bc    - Adapter Configuration (basic)", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        bSizer16.Add(self.m_checkBox6_bc, 0, wx.ALL, 5)

        self.m_checkBox7_ns = wx.CheckBox(self, wx.ID_ANY, u"nsc   - Adapter Configuration (network and security)",
                                          wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer16.Add(self.m_checkBox7_ns, 0, wx.ALL, 5)

        self.m_checkBox8_ac = wx.CheckBox(self, wx.ID_ANY, u"ac    - Adapter Configuration (advanced)",
                                          wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer16.Add(self.m_checkBox8_ac, 0, wx.ALL, 5)

        self.m_staticText31 = wx.StaticText(self, wx.ID_ANY,
                                            u"Note: the above custom permission flags can be used in any combination",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText31.Wrap(-1)
        self.m_staticText31.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer16.Add(self.m_staticText31, 0, wx.ALL, 5)

        self.SetSizer(bSizer16)
        self.Layout()

        self.Centre(wx.BOTH)

        self.Bind(wx.EVT_CLOSE, self.close_custom_window)

    def __del__(self):
        pass

    def close_custom_window(self, event):
        event.Skip()

if __name__ == '__main__':
    app = wx.App()
    my_frame = MyFrame2(None)
    my_frame.Show(show=True)
    my_frame2 = MyDialog2(None)
    my_frame2.Show(show=True)
    app.MainLoop()
