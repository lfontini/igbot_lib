from devices.base import Device


class BaseCisco(Device):
    """
    Driver for cisco using paramiko
    """

    pass


def connect(self):
    """
    connect to the device
    """
    pass


def run(self, command):
    """
    run a command
    """
    pass


def get_interfaces(self):
    """
    get all interfaces
    """
    pass


def get_ips(self):
    """
    get all ips
    """
    pass


def get_arp(self):
    """
    get all arp
    """
    pass


def get_mac(self):
    """
    get all mac address-table
    """
    pass


def get_firewall(self):
    """
    get all firewall
    """
    pass


def get_users(self):
    """
    get all users
    """
    pass


def get_logs(self):
    """
    get all logs
    """
    pass


def get_system(self):
    """
    get all system information
    """
    pass


def get_config(self):
    """
    get all config
    """
    pass


def close(self):
    """
    close the connection
    """
    pass
