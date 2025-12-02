from devices.enums.vendor import Vendor
from devices.enums.mikrotik_driver import MikrotikDriver
from devices.enums.cisco_driver import CiscoDriver
from devices.enums.juniper_driver import JuniperDriver
from devices.enums.datacom_driver import DatacomDriver

from devices.mikrotik.netmiko_driver import MikrotikNetmiko
from devices.mikrotik.paramiko_driver import MikrotikParamiko


from devices.cisco.netmiko_driver import CiscoNetmiko
from devices.cisco.paramiko_driver import CiscoParamiko

from devices.juniper.netmiko_driver import JuniperNetmiko

from devices.datacom.netmiko_driver import DatacomNetmiko



class DeviceFactory:

    _registry = {
        Vendor.MIKROTIK: {
            MikrotikDriver.NETMIKO: MikrotikNetmiko,
            MikrotikDriver.PARAMIKO: MikrotikParamiko,
        },
        Vendor.CISCO: {
            CiscoDriver.NETMIKO: CiscoNetmiko,
            CiscoDriver.PARAMIKO: CiscoParamiko,
        },
        Vendor.JUNIPER: {
            JuniperDriver.NETMIKO: JuniperNetmiko,
        },
        Vendor.DATACOM: {
            DatacomDriver.NETMIKO: DatacomNetmiko,
        },
    }

    @classmethod
    def create(cls, vendor, driver, ip, username, password):
        try:
            klass = cls._registry[vendor][driver]
        except KeyError:
            raise ValueError(f"Driver not supported for {vendor}")

        return klass(ip, username, password)
