
from devices.factory import DeviceFactory
from devices.enums.vendor import Vendor
from devices.enums.cisco_driver import CiscoDriver
from infra.configs.settings import settings   


cs = DeviceFactory.create(
    vendor=Vendor.CISCO,
    driver=CiscoDriver.PARAMIKO ,
    ip="172.20.125.13",
    username=settings.USERNAME_LDAP,
    password=settings.PASSWORD_LDAP,
)


cs.connect()
#print(mt.run("/ip firewall filter print"))
#print(mt.get_system())
system = cs.get_system_structured()
print(system)


