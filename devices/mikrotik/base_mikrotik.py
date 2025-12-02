from devices.base import Device ,abstractmethod

class BaseMikrotik(Device):
    @abstractmethod
    def run(self, command):
        pass
    
    @abstractmethod
    def close(self):
        pass
    
    @abstractmethod
    def get_interfaces(self):
        pass
    
    @abstractmethod
    def get_ips(self):
        pass
    
    @abstractmethod
    def get_arp(self):
        pass
    
    @abstractmethod
    def get_mac(self):
        pass
    
    @abstractmethod
    def firewall(self):
        pass
    
    @abstractmethod
    def get_users(self):
        pass
    
    @abstractmethod
    def get_logs(self):
        pass

    def get_system(self):
        pass

    def get_config(self):
        pass
