from enum import Enum, auto

class MikrotikDriver(Enum):
    NETMIKO = auto()
    PARAMIKO = auto()
    API = auto()
