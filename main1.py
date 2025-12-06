from devices.factory import DeviceFactory
from devices.enums.vendor import Vendor
from devices.enums.mikrotik_driver import MikrotikDriver
from infra.configs.settings import settings   

mt = DeviceFactory.create(
    vendor=Vendor.MIKROTIK,
    driver=MikrotikDriver.NETMIKO,
    ip="172.23.95.10",
    username=settings.MIKROTIK_USERNAME_CPE,
    password=settings.MIKROTIK_PASSWORD_CPE,
)


mt.connect()
#print(mt.run("/ip firewall filter print"))
#print(mt.get_system())
ips = mt.get_ips_structured()
for ip in ips:
    print(ip.num)
    print(ip.ip)
    print(ip.subnet)
    print(ip.network)
    print(ip.interface)
    print(ip.flags)
    print(ip.comment)
    print(ip.cidr)
    print("\n")

mt.close()








