from configs.settings import settings
from devices.factory import DeviceFactory
from enums.device_type import DeviceType


device = DeviceFactory.create(
    DeviceType.MIKROTIK,
    ip="172.20.39.4",
    username=settings.MIKROTIK_USERNAME_POP,
    password=settings.MIKROTIK_PASSWORD_POP,
    port=settings.DEFAULT_PORT
)

conn = device.connect()
print(conn.send_command("/system identity print"))
