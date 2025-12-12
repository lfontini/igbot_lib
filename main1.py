from devices.enums.datacom_driver import DatacomDriver
from devices.enums.cisco_driver import CiscoDriver
from devices.enums.vendor import Vendor
from devices.factory import DeviceFactory
from infra.configs.settings import settings

cs = DeviceFactory.create(
    vendor=Vendor.CISCO,
    driver=CiscoDriver.NETMIKO,
    ip="172.20.125.13",
    username=settings.USERNAME_LDAP,
    password=settings.PASSWORD_LDAP,
)


#cs.connect()
# print(mt.run("/ip firewall filter print"))
# print(mt.get_system())
# interfaces = cs.get_interfaces_strutured()
# for interface in interfaces:
#     print(interface.name)


datacom = DeviceFactory.create(
    vendor=Vendor.DATACOM,
    driver=DatacomDriver.NETMIKO,
    ip="172.20.4.100",
    username=settings.USERNAME_LDAP,
    password=settings.PASSWORD_LDAP,
)

datacom.connect()

print(datacom.get_interface_config("gigabit-ethernet-1/1/4"))
#172.20.111.12
#172.20.125.15 DM4170 - 24GX+12XS
#172.20.39.11  DM4100 - 24FX+4XS
#172.23.66.178 DM4370 - 24FX+4XS
