
from devices.factory import DeviceFactory
from devices.enums.vendor import Vendor
from devices.enums.cisco_driver import CiscoDriver
from infra.configs.settings import settings   


cs = DeviceFactory.create(
    vendor=Vendor.CISCO,
    driver=CiscoDriver.NETMIKO ,
    ip="172.20.125.13",
    username=settings.USERNAME_LDAP,
    password=settings.PASSWORD_LDAP,
)


cs.connect()
#print(mt.run("/ip firewall filter print"))
#print(mt.get_system())
interfaces = cs.get_interfaces_strutured()
for interface in interfaces:
     print(interface)

ips = cs.get_ips_structured()
for ip in ips:
    print(ip)









