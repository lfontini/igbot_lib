from paramiko import AutoAddPolicy, SSHClient

from devices.cisco.model.firewall import Firewall
from devices.cisco.model.interfaces import Interface
from devices.cisco.model.ip_address import IpAddress
from devices.cisco.model.ip_arp import IpArp
from devices.cisco.model.logs import CiscoLogEvent
from devices.cisco.model.system import System
from devices.cisco.parsers.arp_service import ArpService
from devices.cisco.parsers.firewall_parser import FirewallParser
from devices.cisco.parsers.interface_service import InterfaceService
from devices.cisco.parsers.logs import LogParser
from devices.cisco.parsers.system import SystemParser, SystemParserTextFSM

from .base_cisco import BaseCisco


class CiscoParamiko(BaseCisco):
    """
    Driver for cisco using paramiko

    """

    def connect(self):
        ssh_client = SSHClient()
        ssh_client.set_missing_host_key_policy(AutoAddPolicy())
        ssh_client.connect(self.ip, self.port, self.username, self.password)
        self.client = ssh_client

    def run(self, command: str, **kwargs) -> str:
        """
        execute free command
        """
        stdin, stdout, stderr = self.client.exec_command(command, **kwargs)
        return stdout.read().decode("utf-8")

    def get_interfaces(self) -> str:
        """
        get all interfaces as a string
        """
        return self.run("show interfaces")

    def get_interfaces_strutured(self) -> list[Interface]:
        """
        get all interfaces and return a list of Interface objects

        """
        raw_interfaces = self.run("show interfaces")
        return InterfaceService.parse(raw_interfaces)

    def get_ips_structured(self) -> list[IpArp]:
        raw_ips = self.run("show ip interface")
        return ArpService.parse(raw_ips)

    def get_firewall_structured(self) -> list[Firewall]:
        raw = self.run("show ip access-lists")
        return FirewallParser.parse(raw)

    def get_users(self) -> str:
        """
        return all local users
        """
        return self.run("show users")

    def get_system(self) -> str:
        """
        get all system information as a string
        """
        return self.run("show version")

    def get_interfaces_strutured(self) -> list[Interface]:
        """
        get all interfaces and return a list of Interface objects
        """
        raw_interfaces = self.run("show interfaces")
        return InterfaceService.parse(raw_interfaces)

    def get_ips_structured(self) -> list[IpAddress]:
        """
        get all ips and return a list of IpAddress objects
        """
        raw_ips = self.run("show ip interface")
        return ArpService.parse(raw_ips)

    def get_arp(self) -> str:
        """
        get all arp as a string
        """
        return self.run("show ip arp")

    def get_arp_structured(self) -> list[IpArp]:
        """
        get all arp and return a list of IpAddress objects
        """
        raw = self.run("show ip arp")
        return ArpService.parse(raw)

    def get_mac(self) -> str:
        """
        get all mac address-table as a string
        """
        return self.run("show mac address-table")

    def get_logs(self) -> str:
        """
        get all logs as a string
        """
        return self.run("show logging")

    def get_logs_structured(self) -> list[CiscoLogEvent]:
        """
        get all logs and return a list of Log objects
        """
        raw = self.run("show logging")
        return LogParser.parse(raw)

    def get_system_structured(self) -> list[System]:
        """
        get all system information and return a list of System objects
        """
        raw = self.run("show version")
        return SystemParserTextFSM.parse(raw)

    def get_config(self) -> str:
        """
        get all config as a string
        """
        return self.run("show running-config")

    def close(self):
        """
        close the connection
        """
        self.client.close()
