# -*- coding: utf-8 -*-

import wx
import os
from GuiFrame import MyFrame1
from wx.lib.pubsub import pub
from threading import Thread
from BasicAuth import basic_auth
import time
import openpyxl


def get_current_time():
    return time.strftime("%Y-%m-%d-%Hh-%Mmin-%Ss")


class MyGui(MyFrame1):
    def __init__(self):
        self.uri_body = {}
        self.uri_body2 = {}
        MyFrame1.__init__(self, None)
        self.gui_init()

    def gui_init(self):
        self.m_textCtrl3_IP.SetFocus()
        pub.subscribe(self._update, 'update')
        if not os.path.exists('Spec'):
            os.mkdir('Spec')
        if not os.path.exists('Result'):
            os.mkdir('Result')
        if not os.path.exists(r'%s/Spec/%s' % (os.path.abspath('.'), 'uri_body.json')):
            f = open(r'%s/Spec/%s' % (os.path.abspath('.'), 'uri_body.json'), 'w')
            self.uri_body['/redfish/v1/'] = '{}'
            f.seek(0, 0)
            f.write(str(self.uri_body))
            f.close()
        f2 = open(r'%s/Spec/%s' % (os.path.abspath('.'), 'uri_body.json'), 'r')
        self.uri_body2 = eval(f2.read())
        f2.close()
        uri = []
        for uri1 in self.uri_body2:
            uri.append(uri1)
        for uri2 in sorted(uri):
            self.m_comboBox3_URI.Append(uri2)

    def _update(self):
        pass

    def URI_OnCombobox(self, event):
        self.m_textCtrl2_body.SetValue(self.uri_body2[self.m_comboBox3_URI.GetValue()])
        event.Skip()

    def URI_OnText(self, event):

        event.Skip()

    def URI_OnTextEnter(self, event):
        event.Skip()

    def AlwaysOnTop_OnCheckBox(self, event):
        if self.m_checkBox1_AlwaysOnTop.GetValue():
            self.SetWindowStyle(style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP | wx.TAB_TRAVERSAL)
        else:
            self.SetWindowStyle(style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

    def Spec_OnButtonClick(self, event):
        spec_file = 'Spec--' + str(self.m_comboBox3_URI.GetValue()).replace(r':', '_').replace(r'/', '_').replace(r'.', '_') + r'.xlsx'
        SpecOnButtonClickT(spec_file)
        event.Skip()

    def Send_OnButtonClick(self, event):
        ip = self.m_textCtrl3_IP.GetValue()
        uri = self.m_comboBox3_URI.GetValue()
        userid = self.m_textCtrl5_Userid.GetValue()
        password = self.m_textCtrl6_Passw0rd.GetValue()
        auth = self.m_comboBox2_Authorization.GetValue()
        method = self.m_comboBox1_Method.GetValue()
        headers = self.m_textCtrl7_headers.GetValue()
        body = self.m_textCtrl2_body.GetValue()
        spec_file = 'Spec--' + str(self.m_comboBox3_URI.GetValue()).replace(r':', '_').replace(r'/', '_').replace(r'.', '_') + r'.xlsx'
        result_file = 'Result--' + str(self.m_textCtrl3_IP.GetValue() + '--' + self.m_comboBox3_URI.GetValue()).replace(r':', '_').replace(r'/', '_').replace(r'.', '_') + '--' + get_current_time() + r'.xlsx'

        f = open(r'%s/Spec/%s' % (os.path.abspath('.'), 'uri_body.json'), 'r')
        self.uri_body = eval(f.read())
        self.uri_body[str(uri)] = str(body)
        f.close()
        f3 = open(r'%s/Spec/%s' % (os.path.abspath('.'), 'uri_body.json'), 'w')
        f3.write(str(self.uri_body))
        f3.close()

        f2 = open(r'%s/Spec/%s' % (os.path.abspath('.'), 'uri_body.json'), 'r')
        self.uri_body2 = eval(f2.read())
        f2.close()
        _uri = []
        self.m_comboBox3_URI.Clear()
        for _uri1 in self.uri_body2:
            _uri.append(_uri1)
        for _uri2 in sorted(_uri):
            self.m_comboBox3_URI.Append(_uri2)
        self.m_comboBox3_URI.SetValue(uri)

        try:
            if auth == 'Basic Auth':
                basic_auth(ip, uri, userid, password, method, headers, body, spec_file, result_file)
        except IOError:
            dlg = wx.MessageDialog(None, 'Please make your Spec Excel exist.\nAnd you should have closed the result Excel.\nMake sure the ip userid...are correct.', 'Detect Excel worng status', wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
            return 0
        else:
            OpenResultExcel(r'%s/Result/%s' % (os.path.abspath('.'),  result_file))
            pass

        event.Skip()


class SpecOnButtonClickT(Thread):
    def __init__(self, spec_file):
        self.spec_file = spec_file
        Thread.__init__(self)
        self.start()

    def run(self):
        if os.path.exists(r'%s/Spec/%s' % (os.path.abspath('.'), self.spec_file)):
            os.system(r'%s/Spec/%s' % (os.path.abspath('.'), self.spec_file))
        else:
            wb = openpyxl.Workbook()
            ws1 = wb.active
            ws1.title = 'Spec'
            wb.save(r'%s/Spec/%s' % (os.path.abspath('.'), self.spec_file))
            os.system(r'%s/Spec/%s' % (os.path.abspath('.'), self.spec_file))


class OpenResultExcel(Thread):
    def __init__(self, result_file):
        self.result_file = result_file
        Thread.__init__(self)
        self.start()

    def run(self):
        os.system(self.result_file)


if __name__ == '__main__':
    app = wx.App()
    my_frame = MyGui()
    my_frame.Show(show=True)
    app.MainLoop()
