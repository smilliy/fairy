# -*- coding: utf-8 -*-

from wxGUI import MyFrame2
from wx.lib.pubsub import pub
import wx
import paramiko
import threading
from wxGUI import MyDialog2


CUSTOM = []


class auth_click(MyDialog2):
    def __init__(self, parent=None):
        MyDialog2.__init__(self, parent=parent)
        for i in CUSTOM:
            if i == 'am':
                self.m_checkBox1_am.SetValue(True)
            if i == 'rca':
                self.m_checkBox2_rca.SetValue(True)
            if i == 'rcvma':
                self.m_checkBox3_rcvma.SetValue(True)
            if i == 'pr':
                self.m_checkBox4_pr.SetValue(True)
            if i == 'cel':
                self.m_checkBox5_cel.SetValue(True)
            if i == 'bc':
                self.m_checkBox6_bc.SetValue(True)
            if i == 'nsc':
                self.m_checkBox7_ns.SetValue(True)
            if i == 'ac':
                self.m_checkBox8_ac.SetValue(True)

    def close_custom_window(self, event):
        global CUSTOM
        CUSTOM = []
        if self.m_checkBox1_am.GetValue():
            CUSTOM.append('am')
        if self.m_checkBox2_rca.GetValue():
            CUSTOM.append('rca')
        if self.m_checkBox3_rcvma.GetValue():
            CUSTOM.append('rcvma')
        if self.m_checkBox4_pr.GetValue():
            CUSTOM.append('pr')
        if self.m_checkBox5_cel.GetValue():
            CUSTOM.append('cel')
        if self.m_checkBox6_bc.GetValue():
            CUSTOM.append('bc')
        if self.m_checkBox7_ns.GetValue():
            CUSTOM.append('nsc')
        if self.m_checkBox8_ac.GetValue():
            CUSTOM.append('ac')
        pub.sendMessage('pub_update', msg='custom')
        print CUSTOM
        self.Destroy()


class MyFram(MyFrame2):
    def __init__(self):
        MyFrame2.__init__(self, None)
        pub.subscribe(self.pub_update, 'pub_update')
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        for button in [self.m_snmpbutton, self.m_applay, self.m_applayTemplate, self.m_gettemplate]:
            button.Enable(False)
        self.m_authorlevel_custom = ''
        self.initgui()

    def initgui(self):
        self.m_authorlevel_custom = ''
        self.m_authorlevel.SetToolTip(u"""   
-a  - authority level (super, ro, custom:am|rca|rcvma|pr|cel|bc|nsc|ac)
      am    - User account management access
      rca   - Remote console access
      rcvma - Remote console and remote disk (virtual media) access
      pr    - Remote server power/restart access
      cel   - Ability to clear event logs
      bc    - Adapter Configuration (basic)
      nsc   - Adapter Configuration (network and security)
      ac    - Adapter Configuration (advanced)
      Note: the above custom permission flags can be used in any combination
""")
        for gui in [self.m_authorlevel, self.m_xccuserid, self.m_xccpassword, self.m_xccip, self.m_xccport,
                    self.m_accesstype, self.m_userid]:
            gui.SetMinSize(wx.Size(100, 25))
            gui.SetMaxSize(wx.Size(100, 25))
        for key in ['super', 'readonly', 'custom']:
            self.m_authorlevel.Append(key)
        self.m_authorlevel.Select(0)
        for key in ['none', 'HMAC-SHA']:
            self.m_authprotocol.Append(key)
        for key in ['none', 'CBC-DES', 'AES']:
            self.m_privprotocol.Append(key)
        for key in ['PASSW0RD', 'Passw0rd', 'Passw0rd!']:
            self.m_xccpassword.Append(key)
        for key in ['USERID', 'Userid', 'userid']:
            self.m_xccuserid.Append(key)
        for key in ['Get']:
            self.m_accesstype.Append(key)
        for key in ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:
            self.m_userid.Append(key)

    def pub_update(self, msg):
        if msg == 'custom':
            self.m_authorlevel_custom = 'custom:'
            for i in CUSTOM:
                self.m_authorlevel_custom += i + '|'
            self.m_authorlevel_custom = self.m_authorlevel_custom[:-1]
            self.m_authorlevel.SetValue(self.m_authorlevel_custom)
            self.m_outputtext.AppendText(self.m_authorlevel_custom)
            self.m_outputtext.AppendText('\n')

    def log_in_out_click(self, event):
        try:
            if self.m_xccloginout.GetLabel() == 'Log out':
                self.ssh.close()
                self.m_xccloginout.SetLabel('Log in')
                for button in [self.m_snmpbutton, self.m_applay, self.m_applayTemplate, self.m_gettemplate]:
                    button.Enable(False)
                return
            threading.Thread(target=self.loginxcc).start()
        except Exception as e:
            self.messagewindow(e)
            self.m_xccloginout.SetLabel('Log in')
        else:
            for button in [self.m_snmpbutton, self.m_applay, self.m_applayTemplate, self.m_gettemplate]:
                button.Enable(True)
        finally:
            if self.m_xccloginout.GetLabel() == 'Log in':
                self.m_outputtext.AppendText('Log out successfully.\n')

    def snmp_enable_click(self, event):
        try:
            self.execute_ssh_CMD('snmp -t on -a3 on -l adduser_location -cn adduser_contactname')
            self.execute_ssh_CMD('snmpalerts -crt all -wrn all -sys all -crten enabled -wrnen enabled -sysen enabled')
            self.execute_ssh_CMD('Done!')
        except Exception as e:
            self.messagewindow(e)

    def auth_level_click(self, event):
        print self.m_authorlevel.GetSelection()
        if self.m_authorlevel.GetSelection() == 2:
            my_frame2 = auth_click(self)
            my_frame2.Show(show=True)

    def applay_single_user_click(self, event):
        try:
            print self.m_authorlevel.GetValue()
            if self.m_authorlevel.GetValue() == 'super':
                self.m_authorlevel_custom = 'super'
            elif self.m_authorlevel.GetValue() == 'readonly':
                self.m_authorlevel_custom = 'ro'
            elif self.m_authorlevel.GetValue() == self.m_authorlevel_custom:
                pass
            else:
                self.m_authorlevel_custom = self.m_authorlevel.GetValue()
                self.messagewindow('Using your input value for [Authority level] -a %s' % self.m_authorlevel_custom)
            cmd = 'users'
            if self.m_userid.GetValue() != '':
                cmd += ' -' + self.m_userid.GetValue()
            if self.m_username.GetValue() != '':
                cmd += ' -n ' + self.m_username.GetValue()
            if self.m_userpassword.GetValue() != '':
                cmd += ' -p ' + self.m_userpassword.GetValue()
            if self.m_authorlevel_custom != '':
                cmd += ' -a ' + self.m_authorlevel_custom
            if self.m_authprotocol.GetValue() != '':
                cmd += ' -sauth ' + self.m_authprotocol.GetValue()
            if self.m_privprotocol.GetValue() != '':
                cmd += ' -spriv ' + self.m_privprotocol.GetValue()
            if self.m_privpassword.GetValue() != '':
                cmd += ' -spw ' + self.m_privpassword.GetValue()
            if self.m_accesstype.GetValue() != '':
                cmd += ' -sacc ' + self.m_accesstype.GetValue()
            if self.m_tripIP1.GetValue() != '':
                cmd += ' -strap ' + self.m_tripIP1.GetValue()
            self.execute_ssh_CMD(cmd)
            self.execute_ssh_CMD('Done!')
        except Exception as e:
            self.messagewindow(e)

    def applay_template_click(self, event):
        try:
            self.m_applayTemplate.Enable(False)
            m = threading.Thread(target=self.executetempleuser)
            m.start()
        except Exception as e:
            self.messagewindow(e)
        finally:
            self.m_applayTemplate.Enable(True)

    def executetempleuser(self):
        snmpip = self.m_trapIP2.GetValue()
        cmds = [
            'users -2 -n test1 -p Passw0rd1! -a ro -sauth HMAC-SHA -spriv CBC-DES -spw Passw0rd1! -sacc Get -strap %s ' % snmpip,
            'users -3 -n test2 -p Passw0rd1! -a custom:am -sauth HMAC-SHA -spriv CBC-DES -spw Passw0rd1! -sacc Get -strap %s ' % snmpip,
            'users -4 -n test3 -p Passw0rd1! -a custom:rca -sauth HMAC-SHA -spriv CBC-DES -spw Passw0rd1! -sacc Get -strap %s ' % snmpip,
            'users -5 -n test4 -p Passw0rd1! -a custom:rcvma -sauth HMAC-SHA -spriv CBC-DES -spw Passw0rd1! -sacc Get -strap %s ' % snmpip,
            'users -6 -n test5 -p Passw0rd1! -a custom:pr -sauth HMAC-SHA -spriv CBC-DES -spw Passw0rd1! -sacc Get -strap %s ' % snmpip,
            'users -7 -n test6 -p Passw0rd1! -a custom:cel -sauth HMAC-SHA -spriv CBC-DES -spw Passw0rd1! -sacc Get -strap %s ' % snmpip,
            'users -8 -n test7 -p Passw0rd1! -a custom:bc -sauth HMAC-SHA -spriv CBC-DES -spw Passw0rd1! -sacc Get -strap %s ' % snmpip,
            'users -9 -n test8 -p Passw0rd1! -a custom:nsc -sauth HMAC-SHA -spriv CBC-DES -spw Passw0rd1! -sacc Get -strap %s ' % snmpip,
            'users -10 -n test9 -p Passw0rd1! -a custom:ac -sauth HMAC-SHA -spriv CBC-DES -spw Passw0rd1! -sacc Get -strap %s ' % snmpip,
            'users -11 -n test10 -p Passw0rd1! -a super -sauth HMAC-SHA -spriv AES -spw Passw0rd1! -sacc Get -strap %s ' % snmpip,
            'users -12 -n A -p Passw0rd1! -a ro -sauth HMAC-SHA -spriv CBC-DES -spw Passw0rd1! -sacc Get -strap %s ' % snmpip,
            'Done!']
        try:
            for cmd in cmds:
                self.execute_ssh_CMD(cmd=cmd)
        except Exception as e:
            self.messagewindow(e)

    def get_template_click(self, event):
        cmd = """
##################################################################################################################################################################################################################
User list by default:

User     Password       Authority Level      Access type    Address for traps       Authentication protocol      Privacy protocol      Privacy password

test1    Passw0rd1!   Read-only                 Get          Refer to your input       HMAC-SHA                    CBC-DES                Passw0rd1!
test2    Passw0rd1!   User Account Management   Get          Refer to your input       HMAC-SHA                    CBC-DES                Passw0rd1!
test3    Passw0rd1!   Remote Console Access     Get          Refer to your input       HMAC-SHA                    CBC-DES                Passw0rd1!
test4    Passw0rd1!   Remote Console and Remote Disk Access    Get          Refer to your input       HMAC-SHA                    CBC-DES                Passw0rd1!
test5    Passw0rd1!   Remote Server Power/Restart              Get          Refer to your input       HMAC-SHA                    CBC-DES                Passw0rd1!
test6    Passw0rd1!   Ability to Clear Event Logs              Get          Refer to your input       HMAC-SHA                    CBC-DES                Passw0rd1!
test7    Passw0rd1!   Adapter Configuration - Basic            Get          Refer to your input       HMAC-SHA                    CBC-DES                Passw0rd1!
test8    Passw0rd1!   Adapter Configuration - Networking and Security     Get    Refer to your input       HMAC-SHA               CBC-DES                Passw0rd1!
test9    Passw0rd1!   Adapter Configuration - Advanced (Firmware Update, Restart BMC, Restore Configuration)    Get   Refer to your input       HMAC-SHA                    CBC-DES                Passw0rd1!
test10   Passw0rd1!   Super                     Get          Refer to your input       HMAC-SHA                    CBC-DES                Passw0rd1!
A        Passw0rd1!   Read-only                 Get          Refer to your input       HMAC-SHA                    CBC-DES                Passw0rd1!
##################################################################################################################################################################################################################

"""
        self.m_outputtext.AppendText(cmd)


    def execute_ssh_CMD(self, cmd):
        if cmd == 'Done!':
            self.m_outputtext.AppendText('########## CMDs have been executed! ##########\n')
            return[]
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        self.m_outputtext.AppendText('system>%s\n' % cmd)
        self.m_outputtext.AppendText(stdout.read().replace('system>', ''))
        self.m_outputtext.AppendText('\n')

    def loginxcc(self):
        try:
            self.m_xccloginout.SetLabel('Connecting...')
            self.ssh.connect(self.m_xccip.GetValue(), int(self.m_xccport.GetValue()), self.m_xccuserid.GetValue(),
                             self.m_xccpassword.GetValue())
            self.m_xccloginout.SetLabel('Log out')
            self.m_outputtext.AppendText('Log in successfully.\n')
        except Exception as e:
            for button in [self.m_snmpbutton, self.m_applay, self.m_applayTemplate, self.m_gettemplate]:
                button.Enable(False)
            self.messagewindow(e)
            self.m_xccloginout.SetLabel('Log in')

    def messagewindow(self, msg):
        dlg = wx.MessageDialog(None, 'Waring: %s' % str(msg), 'Please check your settings.',
                               wx.OK | wx.ICON_WARNING)
        dlg.ShowModal()

if __name__ == '__main__':
    app = wx.App()
    my_frame = MyFram()
    my_frame.Show(show=True)
    app.MainLoop()