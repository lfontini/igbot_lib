from enum import Enum , auto

class CiscoDriver(Enum):
    NETMIKO = auto()
    PARAMIKO = auto()
    NAPALM = auto()
