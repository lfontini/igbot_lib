from netmiko import ConnectHandler
from .base_cisco import BaseCisco

class CiscoNetmiko(BaseCisco):
    def connect(self):
        return ConnectHandler(
            device_type="cisco_ios",
            ip=self.ip,
            username=self.username,
            password=self.password,
            port=self.port
        )
    
    def run(self, command):
        self.connect()
        return self.client.send_command(command)
    
    def get_interfaces(self):
        self.connect()
        return self.client.send_command("show ip interface brief")

    def get_ips(self):
        self.connect()
        return self.client.send_command("show ip interface brief")

    def get_arp(self):
        self.connect()
        return self.client.send_command("show ip arp")

    def get_mac(self):
        self.connect()
        return self.client.send_command("show mac address-table")

    def get_firewall(self):
        return NotImplemented

    def get_users(self):
        self.connect()
        return self.client.send_command("show users")

    def get_logs(self):
        self.connect()
        return self.client.send_command("show logs")
    
    def get_system(self):
        self.connect()
        return self.client.send_command("show version")
    
    def get_config(self):
        self.connect()
        return self.client.send_command("show running-config")
    
    def close(self):
        self.client.disconnect()
