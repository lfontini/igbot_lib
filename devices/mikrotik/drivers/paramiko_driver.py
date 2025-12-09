from devices.mikrotik.models.arp import Arp
from paramiko import SSHClient, AutoAddPolicy
from .base_mikrotik import BaseMikrotik
from devices.mikrotik.parsers.textfsm_normalizer import parse_arp_mikrotik

class MikrotikParamiko(BaseMikrotik):
    def connect(self):
        ssh_client = SSHClient()
        ssh_client.set_missing_host_key_policy(AutoAddPolicy())
        ssh_client.connect(self.ip, self.port, self.username, self.password)
        self.client = ssh_client

    def run(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        return stdout.read().decode(), stderr.read().decode()

    def _exec(self, cmd):
        stdin, stdout, stderr = self.client.exec_command(cmd)
        out = stdout.read().decode()
        err = stderr.read().decode()
        return out, err

    def get_interfaces(self):
        return self._exec("/interface print")

    def get_ips(self):
        return self._exec("/ip address print")

    def get_arp(self):
        return self._exec("/ip arp print")

    def get_arp_structured(self):
        raw , error = self._exec("/ip arp print")
        if error:
            return error
        else:
            arp = parse_arp_mikrotik(raw)
            result = []
            for item in arp:
                result.append(Arp(num=item["INDEX"], ip=item["ADDRESS"], mac_address=item["MAC_ADDRESS"], interface=item["INTERFACE"]))
            return result

    def get_mac(self):
        return self._exec("/ip mac-address print")

    def get_firewall(self):
        return self._exec("/ip firewall print")

    def get_users(self):
        return self._exec("/user print")

    def get_logs(self):
        return self._exec("/log print")

    def get_system(self):
        return self._exec("/system resource print")

    def get_config(self):
        return self._exec("/export")

    def close(self):
        self.client.close()
