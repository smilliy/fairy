# -*- coding: utf-8 -*-

import os
import configparser


class ExeCMD:
    """
    执行传递的命令
    """
    def __init__(self, command=[]):
        config = configparser.ConfigParser()
        config.read("../config.ini", encoding='utf-8')
        self.hostname = config.get("BMC", "ip")
        self.username = config.get("BMC", "userid")
        self.password = config.get("BMC", "password")
        self.ipmitool = config.get("ipmitool", "path")
        self.command = command

    def run_cmd(self):
        command = ""
        for cmd in self.command:
            command += "&"+cmd
        command = command.lstrip("&")
        os.popen(r'start cmd /k "{command}"'.format(command=command))


if __name__ == "__main__":
    a = ExeCMD(command=["java", "dir", "python"])
    a.run_cmd()

