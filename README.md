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
