from devices.cisco.drivers.netmiko_driver import CiscoNetmiko
from devices.cisco.drivers.paramiko_driver import CiscoParamiko
from devices.datacom.drivers.netmiko_driver import DatacomNetmiko
from devices.enums.cisco_driver import CiscoDriver
from devices.enums.datacom_driver import DatacomDriver
from devices.enums.juniper_driver import JuniperDriver
from devices.enums.mikrotik_driver import MikrotikDriver
from devices.enums.vendor import Vendor
from devices.juniper.drivers.netmiko_driver import JuniperNetmiko
from devices.mikrotik.drivers.napalm_driver import MikrotikNapalm
from devices.mikrotik.drivers.netmiko_driver import MikrotikNetmiko
from devices.mikrotik.drivers.paramiko_driver import MikrotikParamiko


class DeviceFactory:
    """
    Device factory to create device instances.
    """

    _registry = {
        Vendor.MIKROTIK: {
            MikrotikDriver.NETMIKO: MikrotikNetmiko,
            MikrotikDriver.PARAMIKO: MikrotikParamiko,
            MikrotikDriver.NAPALM: MikrotikNapalm,
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
