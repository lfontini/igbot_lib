# devices/cisco/parsers/adapters.py
# Adapters simples para manter compatibilidade com os parsers já existentes
from typing import Any, List

from devices.cisco.model.firewall import Firewall
from devices.cisco.model.interfaces import Interface
from devices.cisco.model.ip_address import IpAddress
from devices.cisco.model.ip_arp import IpArp
from devices.cisco.model.logs import CiscoLogEvent
from devices.cisco.model.system import System
from devices.cisco.parsers.arp_service import ArpService
from devices.cisco.parsers.firewall_parser import FirewallParser

# Importa os parsers concretos que você já tem e delega a eles.
from devices.cisco.parsers.interface_service import InterfaceService
from devices.cisco.parsers.ip_service import IpService
from devices.cisco.parsers.logs import LogParser
from devices.cisco.parsers.protocols import (
    ArpParserProtocol,
    FirewallParserProtocol,
    InterfaceParserProtocol,
    IpParserProtocol,
    LogsParserProtocol,
    SystemParserProtocol,
)
from devices.cisco.parsers.system import SystemParser


class InterfaceParserAdapter(InterfaceParserProtocol):
    def parse(self, raw: Any) -> List[Interface]:
        return InterfaceService.parse(raw)


class IpParserAdapter(IpParserProtocol):
    def parse(self, raw: Any) -> List[IpAddress]:
        return IpService.parse(raw)


class ArpParserAdapter(ArpParserProtocol):
    def parse(self, raw: Any) -> List[IpArp]:
        return ArpService.parse(raw)


class FirewallParserAdapter(FirewallParserProtocol):
    def parse(self, raw: Any) -> List[Firewall]:
        return FirewallParser.parse(raw)


class LogsParserAdapter(LogsParserProtocol):
    def parse(self, raw: Any) -> List[CiscoLogEvent]:
        return LogParser.parse(raw)


class SystemParserAdapter(SystemParserProtocol):
    def parse(self, raw: Any) -> List[System]:
        return SystemParser.parse(raw)
