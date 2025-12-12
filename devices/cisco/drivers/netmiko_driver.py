from devices.cisco.model.interfaces import Interface
from netmiko import ConnectHandler
from devices.cisco.parsers.adapters import (
    InterfaceParserAdapter,
    IpParserAdapter,
    ArpParserAdapter,
    FirewallParserAdapter,
    LogsParserAdapter,
    SystemParserAdapter,
)


from .base_cisco import BaseCisco


class CiscoNetmiko(BaseCisco):
    def __init__(
        self,
        ip: str,
        username: str,
        password: str,
    ):
        self.ip = ip
        self.username = username
        self.password = password
        self.port = 22
        self.client = None

    def connect(self):
        self.client = ConnectHandler(
            device_type="cisco_ios",
            ip=self.ip,
            username=self.username,
            password=self.password,
            port=self.port,
            secret=self.password,
        )
        self.client.enable()

    def run(self, command: str, **kwargs) -> str:
        return self.client.send_command(command, **kwargs)

    def get_interfaces(self) -> str:
        """
        return raw output of show interfaces
        """
        return self.run("show interfaces")

    def get_interfaces_strutured(self) -> list[Interface]:
        """
        return structured output of show interfaces
        """
        raw = self.run("show interfaces", use_textfsm=True)
        return InterfaceParserAdapter().parse(raw)

    def get_ips(self) -> str:
        """
        return raw output of show ip interface brief
        """
        return self.run("show ip interface brief")

    def get_ips_structured(self):
        """
        return structured output of show ip interface
        """
        raw = self.run("show ip interface", use_textfsm=True)
        return IpParserAdapter().parse(raw)

    def get_arp(self) -> str:
        """
        return raw output of show ip arp
        """
        return self.run("show ip arp")

    def get_arp_structured(self):
        """
        return structured output of show ip arp
        """
        raw = self.run("show ip arp", use_textfsm=True)
        return ArpParserAdapter().parse(raw)

    def get_firewall(self) -> str:
        """
        return raw output of show ip access-lists
        """
        return self.run("show ip access-lists")

    def get_firewall_structured(self):
        """
        return structured output of show ip access-lists
        """
        raw = self.run("show ip access-lists", use_textfsm=True)
        return FirewallParserAdapter().parse(raw)

    def get_logs(self) -> str:
        """
        return raw output of show logging
        """
        return self.run("show logging")

    def get_logs_structured(self):
        """
        return structured output of show logging
        """
        raw = self.run("show logging", use_textfsm=True)
        return LogsParserAdapter().parse(raw)

    def get_system(self) -> str:
        """
        return raw output of show version
        """
        return self.run("show version")

    def get_system_structured(self):
        """
        return structured output of show version
        """
        raw = self.run("show version", use_textfsm=True)
        return SystemParserAdapter().parse(raw)

    def get_config(self) -> str:
        """
        return raw output of show running-config
        """
        return self.run("show running-config")

    def close(self):
        """
        close connection
        """
        if self.client:
            self.client.disconnect()
