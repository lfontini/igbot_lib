from devices.factory import DeviceFactory
from devices.enums.vendor import Vendor
from devices.enums.mikrotik_driver import MikrotikDriver
from infra.configs.settings import settings   

mt = DeviceFactory.create(
    vendor=Vendor.MIKROTIK,
    driver=MikrotikDriver.NETMIKO,
    ip="172.20.39.4",
    username=settings.MIKROTIK_USERNAME_POP,
    password=settings.MIKROTIK_PASSWORD_POP,
)


mt.connect()
#print(mt.run("/system/resource/print"))
print(mt.get_system())



mt.close()








