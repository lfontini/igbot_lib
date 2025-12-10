## IGBOTlib documentation



## Project structure

```
devices
    ├───accedian
    ├───cisco
    ├───datacom
    ├───juniper
        ├───drivers
        │   ├───netmiko_driver.py        - Netmiko driver only to access the device
        │   └───paramiko_driver.py       - Paramiko driver only to access the device
        ├───models
        │   ├───arp.py                   - ARP model to store the ARP table as objects
        │   ├───interface.py             - Interface model to store the interfaces as objects
        │   ├───ip_address.py            - IP Address model to store the IP addresses as objects
        │   └───user.py                  - User model to store the users as objects
        └───parsers
            ├───textfsm_normalizer.py    - TextFSM normalizer to normalize the output of the device
            └───arp_parser.py           - ARP parser to parse the ARP table
    └───mikrotik
        ├───drivers
        │   ├───netmiko_driver.py       - Netmiko driver only to access the device
        │   └───paramiko_driver.py      - Paramiko driver only to access the device
        ├───models
        │   ├───arp.py                  - ARP model to store the ARP table as objects
        │   ├───interface.py            - Interface model to store the interfaces as objects
        │   ├───ip_address.py           - IP Address model to store the IP addresses as objects
        │   └───user.py                 - User model to store the users as objects
        └───parsers
            ├───textfsm_normalizer.py   - TextFSM normalizer to normalize the output of the device
            └───arp_parser.py           - ARP parser to parse the ARP table
infra
    ├───configs
    └───logs



```


flowchart LR

    %% =======================================
    %%   MÓDULOS E PASTAS
    %% =======================================
    subgraph MAIN_APP["Aplicação"]
        MAIN["main.py"]
        FACTORY["factory.py<br/>DeviceFactory"]
    end

    subgraph DEVICE_CORE["Core de Dispositivos"]
        BASE_DEVICE["base.py<br/>Device (abstract)"]
    end

    subgraph CISCO["Cisco"]

        subgraph CISCO_DRIVERS["Drivers"]
            NETMIKO_DRIVER["netmiko_driver.py<br/>CiscoNetmiko"]
            PARAMIKO_DRIVER["paramiko_driver.py<br/>CiscoParamiko"]
        end

        BASE_CISCO["base_cisco.py<br/>BaseCisco"]

        subgraph PARSING["Parsing Layer"]
            PROTOCOLS["protocols.py<br/>Protocols"]
            ADAPTERS["adapters.py<br/>Adapters"]
            INTERFACE_SERVICE["interface_service.py"]
            IP_SERVICE["ip_service.py"]
            ARP_SERVICE["arp_service.py"]
            FIREWALL_PARSER["firewall_parser.py"]
            LOGS_PARSER["logs.py"]
            SYSTEM_PARSER["system.py"]
        end

        subgraph MODELS["Modelos (Pydantic)"]
            M_INTERFACE["interfaces.py"]
            M_IP["ip_address.py"]
            M_FIREWALL["firewall.py"]
            M_LOGS["logs.py"]
            M_SYSTEM["system.py"]
        end
    end

    %% =======================================
    %%   RELAÇÕES
    %% =======================================

    MAIN --> FACTORY
    FACTORY --> NETMIKO_DRIVER
    FACTORY --> PARAMIKO_DRIVER

    NETMIKO_DRIVER --> BASE_CISCO
    PARAMIKO_DRIVER --> BASE_CISCO
    BASE_CISCO --> BASE_DEVICE

    %% Driver depende de Protocols
    NETMIKO_DRIVER --> PROTOCOLS

    %% Protocols são implementados pelos adapters
    PROTOCOLS --> ADAPTERS

    %% Adapters chamam services/parsers
    ADAPTERS --> INTERFACE_SERVICE
    ADAPTERS --> IP_SERVICE
    ADAPTERS --> ARP_SERVICE
    ADAPTERS --> FIREWALL_PARSER
    ADAPTERS --> LOGS_PARSER
    ADAPTERS --> SYSTEM_PARSER

    %% Services retornam models
    INTERFACE_SERVICE --> M_INTERFACE
    IP_SERVICE --> M_IP
    ARP_SERVICE --> M_IP
    FIREWALL_PARSER --> M_FIREWALL
    LOGS_PARSER --> M_LOGS
    SYSTEM_PARSER --> M_SYSTEM


How to use?

```
from devices.enums.cisco_driver import CiscoDriver
from devices.enums.vendor import Vendor
from devices.factory import DeviceFactory
from infra.configs.settings import settings

cs = DeviceFactory.create(
    vendor=Vendor.CISCO,
    driver=CiscoDriver.PARAMIKO,
    ip="172.20.125.13",
    username=settings.USERNAME_LDAP,
    password=settings.PASSWORD_LDAP,
)
cs.connect()
print(mt.run("/ip firewall filter print"))
print(mt.get_system())
system = cs.get_system_structured()
print(system)
mt.close()
```


Mikrotik example:

```
from devices.enums.mikrotik_driver import MikrotikDriver
from devices.enums.vendor import Vendor
from devices.factory import DeviceFactory
from infra.configs.settings import settings

mt = DeviceFactory.create(
    vendor=Vendor.MIKROTIK,          -- Vendor enum
    driver=MikrotikDriver.PARAMIKO,  -- Driver enum you can change for paramiko or netmiko
    ip="172.20.125.13",
    username=settings.USERNAME_LDAP,
    password=settings.PASSWORD_LDAP,
)
mt.connect()
print(mt.run("/ip firewall filter print"))
print(mt.get_system())
system = mt.get_system_structured()
print(system)
mt.close()
```
