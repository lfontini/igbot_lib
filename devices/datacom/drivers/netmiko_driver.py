from devices.datacom.parsers.adapters import CLEAR_MAC_TABLE_ADAPTERS
from devices.datacom.models.mac_address import MacAddressTable
from devices.datacom.parsers.adapters import MAC_ADDRESS_TABLE_ADAPTERS
from devices.datacom.models.vlans import Vlan
from devices.datacom.parsers.adapters import VLAN_ADAPTERS
from devices.datacom.parsers.adapters import UPTIME_ADAPTERS
from devices.datacom.models.interfaces import Interface
from devices.datacom.parsers.adapters import INTERFACE_ADAPTERS
from netmiko import ConnectHandler
from .base_datacom import BaseDatacom


class DatacomNetmiko(BaseDatacom):
    """
    Driver for Datacom using Netmiko.
    Cleaned up for maintainability and safety.
    """

    VERSION_KEYWORDS = ["DM2301", "DM4050", "DM4100", "DM4170", "DM4370"]
    FALLBACK_COMMANDS = [
        "show version",
        "show platform",
        "show system",
    ]

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
        if self.client:
            self.client.disconnect()

    def run(self, command: str, **kwargs) -> str:
        """
        Executes a command on device.
        """
        return self.client.send_command(command, **kwargs)

    def _try_commands(self, commands: list[str]) -> str:
        """
        Runs each command until one returns valid output
        (i.e., not syntax error).
        """
        for cmd in commands:
            output = self.run(
                cmd,
                strip_prompt=False,
                strip_command=False,
                expect_string="#",
            )
            if (
                "Invalid input detected" not in output
                and "syntax error" not in output
            ):
                return output

        return ""  # If all commands fail

    def get_version(self) -> str:
        """
        Returns the Datacom model version based on show commands output.
        """

        output = self._try_commands(self.FALLBACK_COMMANDS)

        if not output:
            return "UNKNOWN"

        for keyword in self.VERSION_KEYWORDS:
            if keyword in output:
                return keyword

        return "UNSUPPORTED_MODEL"


    def get_uptime(self) -> str:
        """
        Returns the Datacom uptime based on show commands output.
        """
        version = self.get_version()
        adapter_cls = UPTIME_ADAPTERS.get(version)

        if not adapter_cls:
            raise ValueError(f"Unknown Datacom model: {version}")

        raw = self.run(adapter_cls.command)
        return adapter_cls.parse(raw)


    def get_interfaces(self) -> list[Interface]:
        """
        Returns the Datacom interfaces based on show commands output.
        """
        version = self.get_version()
        adapter_cls = INTERFACE_ADAPTERS.get(version)

        if not adapter_cls:
            raise ValueError(f"Unknown Datacom model: {version}")

        raw = self.run(adapter_cls.command)
        return adapter_cls.parse(raw)

    def get_interface_config(self, interface: str) -> str:
        """
        Returns the Datacom interface config based on show running-config switchport interface commands output.
        """
        version = self.get_version()
        adapter_cls = INTERFACE_ADAPTERS.get(version)

        if not adapter_cls:
            raise ValueError(f"Unknown Datacom model: {version}")

        raw = self.run(adapter_cls.command_by_name(interface))

        return raw


    def get_interface_statistics(self, interface: str) -> str:
        """
        Returns the Datacom interface statistics based on show commands output.
        """
        version = self.get_version()

        return NotImplemented

    def get_interface_errors(self, interface: str) -> str:
        """
        Returns the Datacom interface errors based on show commands output.
        """
        version = self.get_version()

        return NotImplemented


    def get_vlans(self) -> list[Vlan]:
        """
        Returns the Datacom vlans based on show commands output.
        """
        version = self.get_version()
        print("version", version)
        adapter_cls = VLAN_ADAPTERS.get(version)

        if not adapter_cls:
            raise ValueError(f"Unknown Datacom model: {version}")

        raw = self.run(adapter_cls.command)
        return adapter_cls.parse(raw)


    def get_vlan_by_id(self, id: int) -> Vlan:
        """
        Returns the Datacom vlan based on show commands output.
        """
        version = self.get_version()
        adapter_cls = VLAN_ADAPTERS.get(version)

        if not adapter_cls:
            raise ValueError(f"Unknown Datacom model: {version}")

        command = adapter_cls.command_by_id(id)
        raw = self.run(command)
        return adapter_cls.parse(raw)

    def get_global_mac_address_table(self) -> list[MacAddressTable]:
        """
        Returns the Datacom mac address table based on show commands output.
        """
        version = self.get_version()
        adapter_cls = MAC_ADDRESS_TABLE_ADAPTERS.get(version)

        if not adapter_cls:
            raise ValueError(f"Unknown Datacom model: {version}")

        command = adapter_cls.command_all()
        raw = self.run(command)
        return adapter_cls.parse(raw)

    def get_mac_address_table_by_interface(self, interface: str) -> list[MacAddressTable]:
        version = self.get_version()
        adapter_cls = MAC_ADDRESS_TABLE_ADAPTERS.get(version)

        if not adapter_cls:
            raise ValueError(f"Unknown Datacom model: {version}")

        command = adapter_cls.command_by_interface(interface)
        raw = self.run(command)
        return adapter_cls.parse(raw)

    def get_mac_address_table_by_vlan(self, vlan: int) -> list[MacAddressTable]:
        version = self.get_version()
        adapter_cls = MAC_ADDRESS_TABLE_ADAPTERS.get(version)

        if not adapter_cls:
            raise ValueError(f"Unknown Datacom model: {version}")

        command = adapter_cls.command_by_vlan(vlan)
        raw = self.run(command)
        return adapter_cls.parse(raw)

    def clear_mac_address_table_by_vlan(self, vlan: int) -> dict:
        """
        Clears MAC Address Table filtered by VLAN.
        """
        version = self.get_version()
        adapter_cls = CLEAR_MAC_TABLE_ADAPTERS.get(version)

        if not adapter_cls:
            raise ValueError(f"Unknown Datacom model: {version}")

        command = adapter_cls.build_command(vlan=vlan)
        raw = self.run(command)
        return adapter_cls.parse(raw)


    def clear_mac_address_table_by_interface(self, interface: str) -> dict:
        """
        Clears MAC Address Table filtered by interface.
        """
        version = self.get_version()
        adapter_cls = CLEAR_MAC_TABLE_ADAPTERS.get(version)

        if not adapter_cls:
            raise ValueError(f"Unknown Datacom model: {version}")

        command = adapter_cls.build_command(interface=interface)
        raw = self.run(command)
        return adapter_cls.parse(raw)

    def clear_mac_address_table(self) -> dict:
        """
        Clears MAC Address Table.
        """
        version = self.get_version()
        adapter_cls = CLEAR_MAC_TABLE_ADAPTERS.get(version)

        if not adapter_cls:
            raise ValueError(f"Unknown Datacom model: {version}")

        command = adapter_cls.build_command()
        raw = self.run(command)
        return adapter_cls.parse(raw)
