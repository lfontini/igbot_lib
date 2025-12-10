from netmiko import ConnectHandler

from devices.mikrotik.drivers.base_mikrotik import BaseMikrotik
from devices.mikrotik.models.arp import Arp
from devices.mikrotik.models.interfaces import Interface
from devices.mikrotik.models.ip_address import IpAddress
from devices.mikrotik.parsers.textfsm_normalizer import normalize


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
        return self.client.send_command(command)

    def get_interfaces(self):
        return self.client.send_command("/interface print")

    def get_interfaces_strutured(self):
        raw = self.client.send_command("/interface print detail", use_textfsm=True)
        result = []
        for item in raw:
            clean = normalize(item)
            result.append(
                Interface(
                    id=clean["id"],
                    name=clean["name"],
                    status=clean.get("status", "Unknown"),
                    type=clean["type"],
                    mtu=clean["mtu"],
                )
            )

        return result

    def get_ips(self):
        return self.client.send_command("/ip address print")

    def get_ips_structured(self):
        raw = self.client.send_command("/ip address print", use_textfsm=True)
        result = []
        for item in raw:
            clean = normalize(item)
            result.append(
                IpAddress(
                    num=clean["num"],
                    ip=clean["ip"],
                    subnet=clean["subnet"],
                    network=clean["network"],
                    interface=clean["interface"],
                )
            )

        return result

    def get_arp(self):
        return self.client.send_command("/ip arp print")

    def get_arp_structured(self):
        raw = self.client.send_command("/ip arp print", use_textfsm=True)
        result = []
        for item in raw:
            clean = normalize(item)
            result.append(
                Arp(
                    num=clean["num"],
                    ip=clean["ip_address"],
                    mac_address=clean["mac_address"],
                    interface=clean["interface"],
                )
            )
        return result

    def get_firewall(self):
        return self.client.send_command("/ip firewall filter print")

    def get_users(self):
        return self.client.send_command("/user print")

    def get_logs(self):
        return self.client.send_command("/log print")

    def get_system(self):
        return self.client.send_command("/system resource print")

    def get_config(self):
        return self.client.send_command("/export")

    def close(self):
        self.client.disconnect()
