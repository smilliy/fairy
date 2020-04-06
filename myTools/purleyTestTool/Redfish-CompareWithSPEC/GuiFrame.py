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
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Redfish Assistant -- Compare Body with SPEC.", pos=wx.DefaultPosition,
                          size=wx.Size(563, 278), style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DLIGHT))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel3 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel3.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DLIGHT))

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1 = wx.StaticText(self.m_panel3, wx.ID_ANY, u"URI:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        bSizer2.Add(self.m_staticText1, 0, wx.ALL, 5)

        m_comboBox3_URIChoices = []
        self.m_comboBox3_URI = wx.ComboBox(self.m_panel3, wx.ID_ANY, u"/redfish/v1/", wx.DefaultPosition,
                                           wx.DefaultSize, m_comboBox3_URIChoices, 0)
        bSizer2.Add(self.m_comboBox3_URI, 1, wx.ALL, 5)

        m_comboBox1_MethodChoices = [u"Get", u"Post", u"Patch", u"Delete"]
        self.m_comboBox1_Method = wx.ComboBox(self.m_panel3, wx.ID_ANY, u"Get", wx.DefaultPosition, wx.DefaultSize,
                                              m_comboBox1_MethodChoices, wx.CB_READONLY)
        self.m_comboBox1_Method.SetSelection(0)
        bSizer2.Add(self.m_comboBox1_Method, 0, wx.ALL, 5)

        self.m_button6_Spec = wx.Button(self.m_panel3, wx.ID_ANY, u"Spec", wx.DefaultPosition, wx.DefaultSize,
                                        wx.BU_EXACTFIT)
        bSizer2.Add(self.m_button6_Spec, 0, wx.ALL, 5)

        self.m_button3_send = wx.Button(self.m_panel3, wx.ID_ANY, u"Send", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button3_send.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DLIGHT))

        bSizer2.Add(self.m_button3_send, 0, wx.ALL, 5)

        self.m_panel3.SetSizer(bSizer2)
        self.m_panel3.Layout()
        bSizer2.Fit(self.m_panel3)
        bSizer1.Add(self.m_panel3, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticline1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer1.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        self.m_notebook2 = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_BOTTOM)
        self.m_notebook2.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DLIGHT))

        self.m_panel8_Login = wx.Panel(self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_panel9 = wx.Panel(self.m_panel8_Login, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText2 = wx.StaticText(self.m_panel9, wx.ID_ANY, u"IP:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        bSizer6.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.m_textCtrl3_IP = wx.TextCtrl(self.m_panel9, wx.ID_ANY, u"https://10.245.", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        bSizer6.Add(self.m_textCtrl3_IP, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText3 = wx.StaticText(self.m_panel9, wx.ID_ANY, u"Authorization:", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        bSizer6.Add(self.m_staticText3, 0, wx.ALL, 5)

        m_comboBox2_AuthorizationChoices = [u"Basic Auth",]
        self.m_comboBox2_Authorization = wx.ComboBox(self.m_panel9, wx.ID_ANY, u"Basic Auth", wx.DefaultPosition,
                                                     wx.DefaultSize, m_comboBox2_AuthorizationChoices, wx.CB_READONLY)
        self.m_comboBox2_Authorization.SetSelection(0)
        bSizer6.Add(self.m_comboBox2_Authorization, 0, wx.ALL | wx.EXPAND, 5)

        self.m_panel9.SetSizer(bSizer6)
        self.m_panel9.Layout()
        bSizer6.Fit(self.m_panel9)
        bSizer5.Add(self.m_panel9, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel10 = wx.Panel(self.m_panel8_Login, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText4 = wx.StaticText(self.m_panel10, wx.ID_ANY, u"UserId:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        bSizer7.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.m_textCtrl5_Userid = wx.TextCtrl(self.m_panel10, wx.ID_ANY, u"USERID", wx.DefaultPosition, wx.DefaultSize,
                                              0)
        bSizer7.Add(self.m_textCtrl5_Userid, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText5 = wx.StaticText(self.m_panel10, wx.ID_ANY, u"Password:", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText5.Wrap(-1)
        bSizer7.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.m_textCtrl6_Passw0rd = wx.TextCtrl(self.m_panel10, wx.ID_ANY, u"PASSW0RD", wx.DefaultPosition,
                                                wx.DefaultSize, wx.TE_PASSWORD)
        bSizer7.Add(self.m_textCtrl6_Passw0rd, 0, wx.ALL | wx.EXPAND, 5)

        self.m_panel10.SetSizer(bSizer7)
        self.m_panel10.Layout()
        bSizer7.Fit(self.m_panel10)
        bSizer5.Add(self.m_panel10, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel8_Login.SetSizer(bSizer5)
        self.m_panel8_Login.Layout()
        bSizer5.Fit(self.m_panel8_Login)
        self.m_notebook2.AddPage(self.m_panel8_Login, u"Login", True)
        self.m_panel5_Body = wx.Panel(self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl2_body = wx.TextCtrl(self.m_panel5_Body, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, wx.TE_MULTILINE)
        self.m_textCtrl2_body.SetValue('{}')
        bSizer3.Add(self.m_textCtrl2_body, 1, wx.ALL | wx.EXPAND, 5)

        self.m_panel5_Body.SetSizer(bSizer3)
        self.m_panel5_Body.Layout()
        bSizer3.Fit(self.m_panel5_Body)
        self.m_notebook2.AddPage(self.m_panel5_Body, u"Body", False)
        self.m_panel6_Headers = wx.Panel(self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                         wx.TAB_TRAVERSAL)
        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl7_headers = wx.TextCtrl(self.m_panel6_Headers, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                               wx.DefaultSize, wx.TE_MULTILINE)
        self.m_textCtrl7_headers.SetValue('Redfish Assistant will fill it automatically when you use Patch Method.\nYou have nothing to do here.')
        bSizer4.Add(self.m_textCtrl7_headers, 1, wx.ALL | wx.EXPAND, 5)

        self.m_panel6_Headers.SetSizer(bSizer4)
        self.m_panel6_Headers.Layout()
        bSizer4.Fit(self.m_panel6_Headers)
        self.m_notebook2.AddPage(self.m_panel6_Headers, u"Headers", False)
        self.m_panel7_Setting = wx.Panel(self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                         wx.TAB_TRAVERSAL)
        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_panel13 = wx.Panel(self.m_panel7_Setting, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                  wx.TAB_TRAVERSAL)
        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.m_checkBox1_AlwaysOnTop = wx.CheckBox(self.m_panel13, wx.ID_ANY, u"Always On Top", wx.DefaultPosition,
                                                   wx.DefaultSize, 0)
        self.m_checkBox1_AlwaysOnTop.SetValue(True)
        bSizer9.Add(self.m_checkBox1_AlwaysOnTop, 0, wx.ALL, 5)

        self.m_panel13.SetSizer(bSizer9)
        self.m_panel13.Layout()
        bSizer9.Fit(self.m_panel13)
        bSizer8.Add(self.m_panel13, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel14 = wx.Panel(self.m_panel7_Setting, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                  wx.TAB_TRAVERSAL)
        bSizer8.Add(self.m_panel14, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel15 = wx.Panel(self.m_panel7_Setting, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                  wx.TAB_TRAVERSAL)
        bSizer8.Add(self.m_panel15, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel16 = wx.Panel(self.m_panel7_Setting, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                  wx.TAB_TRAVERSAL)
        bSizer8.Add(self.m_panel16, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel7_Setting.SetSizer(bSizer8)
        self.m_panel7_Setting.Layout()
        bSizer8.Fit(self.m_panel7_Setting)
        self.m_notebook2.AddPage(self.m_panel7_Setting, u"Setting", False)
        self.m_panel17_About = wx.Panel(self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TAB_TRAVERSAL)
        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText12 = wx.StaticText(self.m_panel17_About, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText12.Wrap(-1)
        bSizer10.Add(self.m_staticText12, 0, wx.ALL, 5)

        self.m_staticText11 = wx.StaticText(self.m_panel17_About, wx.ID_ANY, u"Welcome to use this tool.",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        self.m_staticText11.SetFont(wx.Font(15, 75, 90, 92, True, "隶书"))
        self.m_staticText11.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        self.m_staticText11.SetBackgroundColour(wx.Colour(28, 187, 64))

        bSizer10.Add(self.m_staticText11, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText8 = wx.StaticText(self.m_panel17_About, wx.ID_ANY, u"Written on 2018/02/02 with Python 2.7.14",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)
        self.m_staticText8.SetFont(wx.Font(14, 75, 93, 90, True, "隶书"))

        bSizer10.Add(self.m_staticText8, 0, wx.ALL, 5)

        self.m_staticText9 = wx.StaticText(self.m_panel17_About, wx.ID_ANY, u"Any Concern Please contact with me.",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)
        self.m_staticText9.SetFont(wx.Font(9, 74, 90, 92, True, "微软雅黑"))
        self.m_staticText9.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer10.Add(self.m_staticText9, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.m_panel17_About.SetSizer(bSizer10)
        self.m_panel17_About.Layout()
        bSizer10.Fit(self.m_panel17_About)
        self.m_notebook2.AddPage(self.m_panel17_About, u"About", False)

        bSizer1.Add(self.m_notebook2, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_comboBox3_URI.Bind(wx.EVT_COMBOBOX, self.URI_OnCombobox)
        self.m_comboBox3_URI.Bind(wx.EVT_TEXT, self.URI_OnText)
        self.m_comboBox3_URI.Bind(wx.EVT_TEXT_ENTER, self.URI_OnTextEnter)
        self.m_button6_Spec.Bind(wx.EVT_BUTTON, self.Spec_OnButtonClick)
        self.m_button3_send.Bind(wx.EVT_BUTTON, self.Send_OnButtonClick)
        self.m_checkBox1_AlwaysOnTop.Bind(wx.EVT_CHECKBOX, self.AlwaysOnTop_OnCheckBox)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def URI_OnCombobox(self, event):
        event.Skip()

    def URI_OnText(self, event):
        event.Skip()

    def URI_OnTextEnter(self, event):
        event.Skip()

    def Spec_OnButtonClick(self, event):
        event.Skip()

    def Send_OnButtonClick(self, event):
        event.Skip()

    def AlwaysOnTop_OnCheckBox(self, event):
        event.Skip()

if __name__ == '__main__':
    app = wx.App()
    myfram = MyFrame1(None)
    myfram.Show(show=True)
    app.MainLoop()

