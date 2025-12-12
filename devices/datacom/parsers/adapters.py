# adapters.py



from devices.datacom.parsers.mac_address_service import MacAddressTableService
from devices.datacom.parsers.vlan_service import VlanService4100
from devices.datacom.parsers.vlan_service import VlanService4170
from devices.datacom.parsers.vlan_service import VlanService4370 , VlanService4050
from devices.datacom.parsers.uptime_service import UptimeService
from devices.datacom.parsers.interface_service import InterfaceService_DM4370, InterfaceService_DM4170, InterfaceService_DM4050, InterfaceService_DM4100

#=================== INTERFACE ====================

class BaseInterfaceAdapter:
    command: str = "show interface"

    @classmethod
    def parse(cls, raw: str) -> list[dict]:
        raise NotImplementedError



class DM4100Adapter(BaseInterfaceAdapter):
    command = "show interfaces status"

    @classmethod
    def parse(cls, raw: str) -> list[dict]:
        return InterfaceService_DM4100.parse(raw)


class DM4050Adapter(BaseInterfaceAdapter):
    command = "show running-config switchport interface"

    @classmethod
    def command_by_name(cls, name: str) -> str:
        return f"{cls.command} {name}"

    @classmethod
    def parse(cls, raw: str) -> list[dict]:
        return InterfaceService_DM4050.parse(raw)


class DM4170Adapter(BaseInterfaceAdapter):
    @classmethod
    def parse(cls, raw: str) -> list[dict]:
        return InterfaceService_DM4170.parse(raw)


class DM4370Adapter(BaseInterfaceAdapter):
    @classmethod
    def parse(cls, raw: str) -> list[dict]:
        return InterfaceService_DM4370.parse(raw)


# Mapa de versão → adapter
INTERFACE_ADAPTERS = {
    "DM4100": DM4100Adapter,
    "DM4050": DM4050Adapter,
    "DM4170": DM4170Adapter,
    "DM4370": DM4370Adapter,
}


#=================== UPTIME ====================

class BaseUptimeAdapter:
    command: str = "show system"

    @classmethod
    def parse(cls, raw: str) -> str:
        raise NotImplementedError

class DM4370UptimeAdapter(BaseUptimeAdapter):
    command = "show system"

    @classmethod
    def parse(cls, raw: str) -> str:
        return UptimeService.parse(raw)


UPTIME_ADAPTERS = {
    "DM4370": DM4370UptimeAdapter,
}


#=================== VLAN ====================

class BaseVlanAdapter:
    command: str = "show vlans"

    @classmethod
    def parse(cls, raw: str) -> list[dict]:
        raise NotImplementedError

class DM4370VlanAdapter(BaseVlanAdapter):
    command = "show vlan membership detail"

    @classmethod
    def parse(cls, raw: str) -> list[dict]:
        return VlanService4370.parse(raw)

class DM4050VlanAdapter(BaseVlanAdapter):
    full_command = "show vlan membership detail"
    single_command = "show vlan brief"

    @classmethod
    def command_by_id(cls, vlan_id: int) -> str:
        return f"{cls.single_command} {vlan_id}"

    @classmethod
    def parse(cls, raw: str) -> list[dict]:
        return VlanService4050.parse(raw)

class DM4170VlanAdapter(BaseVlanAdapter):
    command = "show vlan membership detail"

    @classmethod
    def parse(cls, raw: str) -> list[dict]:
        return VlanService4170.parse(raw)

class DM4100VlanAdapter(BaseVlanAdapter):
    command = "show vlan"

    @classmethod
    def parse(cls, raw: str) -> list[dict]:
        return VlanService4100.parse(raw)

VLAN_ADAPTERS = {
    "DM4370": DM4370VlanAdapter,
    "DM4050": DM4050VlanAdapter,
    "DM4170": DM4170VlanAdapter,
    "DM4100": DM4100VlanAdapter,
}





#=================== MAC ADDRESS TABLE ====================

class BaseMacAddressTableAdapter:
    base_command: str = "show mac-address-table"

    @classmethod
    def command_by_vlan(cls, vlan: int) -> str:
        """
        Command to filter MAC address table by VLAN
        """
        return f"{cls.base_command} vlan {vlan}"

    @classmethod
    def command_by_interface(cls, interface: str) -> str:
        """
        Command to filter MAC address table by interface
        """
        return f"{cls.base_command} interface {interface}"

    @classmethod
    def command_all(cls) -> str:
        """
        Default command for all MAC addresses.
        """
        return cls.base_command

    @classmethod
    def parse(cls, raw: str) -> list[dict]:
        raise NotImplementedError


class DM4100MacAddressTableAdapter(BaseMacAddressTableAdapter):
    base_command = "show mac-address-table"

    @classmethod
    def parse(cls, raw: str) -> list[dict]:
        return MacAddressTableService.parse(raw)

MAC_ADDRESS_TABLE_ADAPTERS = {
    "DM4100": DM4100MacAddressTableAdapter,
}



#=================== CLEAR MAC ADDRESS TABLE ====================

class BaseClearMacTableAdapter:
    command: str = "clear mac-address-table"

    @classmethod
    def build_command(cls, interface: str | None = None, vlan: int | None = None) -> str:
        if interface:
            return f"{cls.command} interface {interface}"
        if vlan:
            return f"{cls.command} vlan {vlan}"
        return cls.command

    @classmethod
    def parse(cls, raw: str) -> dict:
        return {"status": raw.strip()}

class DM4100ClearMacTableAdapter(BaseClearMacTableAdapter):
    command = "clear mac-address-table"


class DM4170ClearMacTableAdapter(BaseClearMacTableAdapter):
    command = "clear mac-address-table"


class DM4370ClearMacTableAdapter(BaseClearMacTableAdapter):
    command = "clear mac-address-table"


class DM4050ClearMacTableAdapter(BaseClearMacTableAdapter):
    command = "clear mac-address-table"


CLEAR_MAC_TABLE_ADAPTERS = {
    "DM4100": DM4100ClearMacTableAdapter,
    "DM4170": DM4170ClearMacTableAdapter,
    "DM4370": DM4370ClearMacTableAdapter,
    "DM4050": DM4050ClearMacTableAdapter,
}
