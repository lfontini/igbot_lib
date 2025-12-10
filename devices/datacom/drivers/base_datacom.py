from abc import ABC, abstractmethod

from devices.base import Device


class BaseDatacom(Device, ABC):
    @abstractmethod
    def connect(self):
        """
        connect to the device
        """
        pass

    @abstractmethod
    def close(self):
        """
        close the connection
        """
        pass
