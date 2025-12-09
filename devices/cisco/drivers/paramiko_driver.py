from .base_cisco import BaseCisco

class CiscoParamiko(BaseCisco):
    """
    Driver for cisco using paramiko

    """
    def connect(self):
        ssh_client = SSHClient()
        ssh_client.set_missing_host_key_policy(AutoAddPolicy())
        ssh_client.connect(self.ip, self.port, self.username, self.password)
        return ssh_client
    
    def close(self):
        self.client.close()