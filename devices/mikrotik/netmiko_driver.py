from netmiko import ConnectHandler
from .base_mikrotik import BaseMikrotik

class MikrotikNetmiko(BaseMikrotik):
    def connect(self):
        self.client = ConnectHandler(
            device_type="mikrotik_routeros",
            ip=self.ip,
            username=self.username,
            password=self.password,
            port=self.port
        )
    
    def run(self, command):
        """
        execute free command 
        """ 
        self.connect()
        return self.client.send_command(command)


    def get_interfaces(self):
        self.connect()
        return self.client.send_command("/interface print")

    def get_ips(self):
        self.connect()
        return self.client.send_command("/ip address print")

    def get_arp(self):
        self.connect()
        return self.client.send_command("/ip arp print")

    def get_mac(self):
        self.connect()
        return self.client.send_command("/ip mac-address print")

    def get_firewall(self):
        self.connect()
        return self.client.send_command("/ip firewall print")

    def get_users(self):
        self.connect()
        return self.client.send_command("/user print")

    def get_logs(self):
        self.connect()
        return self.client.send_command("/log print")   


    def get_system(self):
        self.connect()
        return self.client.send_command("/system resource print")
    
    def get_config(self):
        self.connect()
        return self.client.send_command("/export")

    def close(self):
        self.client.disconnect()