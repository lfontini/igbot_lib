from devices.base import Device, abstractmethod


class BaseMikrotik(Device):
    @abstractmethod
    def run(self, command):
        """
        execute free command
        """
        pass

    @abstractmethod
    def close(self):
        """
        close the connection
        """
        pass

    @abstractmethod
    def get_interfaces(self):
        """
        get all interfaces as a string
        """
        pass

    @abstractmethod
    def get_interfaces_strutured(self):
        """
        get all interfaces and return a list of Interface objects
        """
        pass

    @abstractmethod
    def get_ips(self):
        """
        get all ips as a string
        """
        pass

    @abstractmethod
    def get_ips_strutured(self):
        """
        get all ips and return a list of IpAddress objects
        """
        pass

    @abstractmethod
    def get_arp(self):
        """
        get all arp as a string
        """
        pass

    @abstractmethod
    def get_arp_strutured(self):
        """
        get all arp and return a list of IpAddress objects
        """
        pass

    @abstractmethod
    def get_mac(self):
        """
        get all mac address-table as a string
        """
        pass

    @abstractmethod
    def get_mac_strutured(self):
        """
        get all mac address-table and return a list of MacAddress objects
        """
        pass

    @abstractmethod
    def firewall(self):
        """
        get all firewall as a string
        """
        pass

    @abstractmethod
    def get_firewall_strutured(self):
        """
        get all firewall and return a list of Firewall objects
        """
        pass

    @abstractmethod
    def get_users(self):
        """
        get all users as a string
        """
        pass

    @abstractmethod
    def get_users_strutured(self):
        """
        get all users and return a list of User objects
        """
        pass

    @abstractmethod
    def get_logs(self):
        """
        get all logs as a string
        """
        pass

    @abstractmethod
    def get_logs_strutured(self):
        """
        get all logs and return a list of Log objects
        """
        pass

    @abstractmethod
    def get_system_strutured(self):
        """
        get all system information and return a list of System objects
        """
        pass

    @abstractmethod
    def get_system(self):
        """
        get all system information as a string
        """
        pass

    @abstractmethod
    def get_config(self):
        """
        get all config as a string
        """
        pass

    @abstractmethod
    def get_config_strutured(self):
        """
        get all config and return a list of Config objects
        """
        pass
