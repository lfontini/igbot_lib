from devices.cisco.model.system import System
from devices.cisco.model.logs import CiscoLogEvent
from devices.cisco.parsers.system import SystemParser
from devices.cisco.parsers.logs import LogParser
from devices.cisco.model.firewall import Firewall
from devices.cisco.parsers.firewall_parser import FirewallParser
from devices.cisco.parsers.arp_service import ArpService
from devices.cisco.model.ip_address import IpAddress
from devices.cisco.model.interfaces import Interface
from devices.cisco.parsers.ip_service import IpService
from devices.cisco.parsers.interface_service import InterfaceService
from netmiko import ConnectHandler
from .base_cisco import BaseCisco

class CiscoNetmiko(BaseCisco):
    def connect(self):
        self.client = ConnectHandler(
        device_type="cisco_ios",
        ip=self.ip,
        username=self.username,
        password=self.password,
        port=self.port,
        secret=self.password)   
        self.client.enable()
    
    def run(self, command: str, **kwargs) -> str:
        """
        execute free command 
        """
        return self.client.send_command(command, **kwargs)
    
    def get_interfaces(self) -> str:
        """
        get all interfaces as a string 
        """
        return self.run("show interfaces")

    def get_interfaces_strutured(self) -> list[Interface]:
        """
        get all interfaces and return a list of Interface objects

        """
        raw_interfaces = self.run("show interfaces", use_textfsm=True)
        return InterfaceService.parse(raw_interfaces)

    def get_ips(self) -> str:
        return self.run("show ip interface brief")

    def get_ips_structured(self) -> list[IpAddress]:
        raw_ips = self.run("show ip interface", use_textfsm=True)
        return ArpService.parse(raw_ips)

    def get_arp(self) -> str:
        return self.run("show ip arp")

    def get_arp_structured(self) -> list[IpAddress]:
        raw = self.run("show ip arp", use_textfsm=True)
        return ArpService.parse(raw)

    def get_mac(self) -> str:
        return self.run("show mac address-table")

    def get_firewall(self) -> str:
        return self.run("show ip access-lists")

    def get_firewall_structured(self) -> list[Firewall]:
        raw = self.run("show ip access-lists", use_textfsm=True)
        return FirewallParser.parse(raw)

    def get_users(self) -> str:
        '''
        return all local users
        '''
        return self.run("show users")

    def get_logs(self) -> str:
        """
        get all logs as a string
        """
        return self.run("show logging")

    def get_logs_structured(self) -> list[CiscoLogEvent]:
        """
        get all logs and return a list of Log objects
        """
        raw = self.run("show logging", use_textfsm=True)
        return LogParser.parse(raw)

    def get_system(self) -> str:
        """
        get all system information as a string
        """
        return self.run("show version")

    def get_system_structured(self) -> list[System]:
        """
        get all system information and return a list of System objects
        """
        raw = self.run("show version", use_textfsm=True)
        return SystemParser.parse(raw)
    
    def get_config(self) -> str:
        """
        get all config as a string
        """
        return self.run("show running-config")
    
    def close(self) -> None:
        self.client.disconnect()
