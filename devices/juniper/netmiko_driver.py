from netmiko import ConnectHandler
from .base_juniper import BaseJuniper

class JuniperNetmiko(BaseJuniper):
    def connect(self):
        return ConnectHandler(
            device_type="juniper",
            ip=self.ip,
            username=self.username,
            password=self.password,
            port=self.port
        )
    
    def close(self):
        self.client.disconnect()
