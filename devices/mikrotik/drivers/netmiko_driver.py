from devices.mikrotik.drivers.base_mikrotik import BaseMikrotik
from netmiko import ConnectHandler
from devices.mikrotik.models.ip_address import IpAddress
from devices.mikrotik.parsers.textfsm_normalizer import normalize_record

class MikrotikNetmiko(BaseMikrotik):
    def connect(self):
        self.client = ConnectHandler(
            device_type="mikrotik_routeros",
            ip=self.ip,
            username=self.username,
            password=self.password,
            port=self.port,
            conn_timeout=15,
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

    def get_interfaces_strutured(self):
        self.connect()
        return self.client.send_command("/interface print detail" , use_textfsm=True)

    def get_ips(self):
        self.connect()
        return self.client.send_command("/ip address print")

    def get_ips_structured(self):
        self.connect()
        raw = self.client.send_command("/ip address print", use_textfsm=True)
        result = []
        for item in raw:
            clean = normalize_record(item)
            result.append(IpAddress(**clean))

        return result

    def get_arp(self):
        self.connect()
        return self.client.send_command("/ip arp print")

    def get_mac(self):
        self.connect()
        return self.client.send_command("/ip mac-address print")

    def get_firewall(self):
        self.connect()
        return self.client.send_command("/ip firewall filter print")

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