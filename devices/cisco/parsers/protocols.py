# devices/cisco/parsers/protocols.py
from typing import Any, List, Protocol

from devices.cisco.model.firewall import Firewall
from devices.cisco.model.interfaces import Interface
from devices.cisco.model.ip_address import IpAddress
from devices.cisco.model.logs import CiscoLogEvent
from devices.cisco.model.system import System


class InterfaceParserProtocol(Protocol):
    def parse(self, raw: Any) -> List[Interface]: ...


class IpParserProtocol(Protocol):
    def parse(self, raw: Any) -> List[IpAddress]: ...


class ArpParserProtocol(Protocol):
    def parse(self, raw: Any) -> List[IpAddress]: ...


class FirewallParserProtocol(Protocol):
    def parse(self, raw: Any) -> List[Firewall]: ...


class LogsParserProtocol(Protocol):
    def parse(self, raw: Any) -> List[CiscoLogEvent]: ...


class SystemParserProtocol(Protocol):
    def parse(self, raw: Any) -> List[System]: ...
