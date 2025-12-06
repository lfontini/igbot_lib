from paramiko import SSHClient
from .base_mikrotik import BaseMikrotik
from paramiko import AutoAddPolicy

class MikrotikParamiko(BaseMikrotik):
    def connect(self):
        ssh_client = SSHClient()
        ssh_client.set_missing_host_key_policy(AutoAddPolicy())
        ssh_client.connect(self.ip, self.port, self.username, self.password)
        self.client = ssh_client
    
    def run(self, command):
        return self.client.exec_command(command)

    def get_interfaces(self):
        self.connect()
        return self.client.exec_command("/interface print")

    def get_ips(self):
        self.connect()
        return self.client.exec_command("/ip address print")

    def get_arp(self):
        self.connect()
        return self.client.exec_command("/ip arp print")

    def get_mac(self):
        self.connect()
        return self.client.exec_command("/ip mac-address print")

    def get_firewall(self):
        self.connect()
        return self.client.exec_command("/ip firewall print")

    def get_users(self):
        self.connect()
        return self.client.exec_command("/user print")

    def get_logs(self):
        self.connect()
        return self.client.exec_command("/log print")   
    
    def get_system(self):
        self.connect()
        return self.client.exec_command("/system resource print")
    
    def get_config(self):
        self.connect()
        return self.client.exec_command("/export")

    def get_config_strutured(self):
        self.connect()
        return self.client.exec_command("/export")

    def get_interfaces_strutured(self):
        self.connect()
        return self.client.exec_command("/interface print")

    def get_ips_strutured(self):
        self.connect()
        return self.client.exec_command("/ip address print")

    def get_arp_strutured(self):
        self.connect()
        return self.client.exec_command("/ip arp print")

    def get_mac_strutured(self):
        self.connect()
        return self.client.exec_command("/ip mac-address print")

    def get_firewall_strutured(self):
        self.connect()
        return self.client.exec_command("/ip firewall print")

    def get_users_strutured(self):
        self.connect()
        return self.client.exec_command("/user print")

    def get_logs_strutured(self):
        self.connect()
        return self.client.exec_command("/log print")   
    
    def get_system_strutured(self):
        self.connect()
        return self.client.exec_command("/system resource print")

    def get_firewall_strutured(self):
        self.connect()
        return self.client.exec_command("/ip firewall print")

    def get_users_strutured(self):
        self.connect()
        return self.client.exec_command("/user print")

    def get_logs_strutured(self):
        self.connect()
        return self.client.exec_command("/log print")   
    
    def get_system_strutured(self):
        self.connect()
        return self.client.exec_command("/system resource print")
    
    def get_config_strutured(self):
        self.connect()
        return self.client.exec_command("/export")

    def close(self):
        self.client.close()
        