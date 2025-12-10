from netmiko import ConnectHandler

from .base_datacom import BaseDatacom


class DatacomNetmiko(BaseDatacom):
    """
    Driver for datacom using netmiko
    """

    def connect(self):
        self.client = ConnectHandler(
            device_type="autodetect",
            ip=self.ip,
            username=self.username,
            password=self.password,
            port=self.port,
            secret=self.password,
        )

    def close(self):
        """
        close the connection
        """
        self.client.disconnect()

    def run(self, command: str) -> str:
        """
        execute free command
        """
        return self.client.send_command(command)
