# -*- coding: utf-8 -*-
import paramiko
import configparser


class SSHtoBMC:
    """
    1. 通过ssh协议，连接BMC
    2. 通过CLI命令，控制BMC
    """
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("../config.ini", encoding='utf-8')
        self.hostname = config.get("BMC", "ip")
        self.username = config.get("BMC", "userid")
        self.password = config.get("BMC", "password")
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect(hostname=self.hostname, username=self.username, password=self.password)

    def exec_cmd(self, command="vpd fw"):
        stdin, stdout, stderr = self.ssh_client.exec_command(command)
        print(stderr.read().decode())
        print(stdout.read().decode().replace("system>", ""))

    def close_ssh_connection(self):
        self.ssh_client.close()


if __name__ == "__main__":
    ssh_client_test = SSHtoBMC()
    ssh_client_test.exec_cmd("vpd bmc")
    ssh_client_test.close_ssh_connection()
