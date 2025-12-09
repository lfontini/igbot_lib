from netmiko import ConnectHandler
from .base_datacom import BaseDatacom

class DatacomNetmiko(BaseDatacom):
    def connect(self):
        return ConnectHandler(
            device_type="datacom",
            ip=self.ip,
            username=self.username,
           password=self.password,
            port=self.port
        )
    
    def close(self):
        self.client.disconnect()
