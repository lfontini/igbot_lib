from napalm.base.models import MACAdressTable
from devices.datacom.models.mac_address import MacAddressTable
from textfsm import TextFSM
class MacAddressTableService:
    @staticmethod
    def parse(raw: str) -> list[MacAddressTable]:
        with open("devices/datacom/parsers/templates/mac_address_dm_4100.textfsm", encoding="utf-8") as template:
            fsm = TextFSM(template)
            result = fsm.ParseText(raw)

        mac_address_table = []
        for row in result:
            entry = dict(zip(fsm.header, row))
            mac_address = entry.get("MAC")
            vlan = entry.get("VLAN")
            interface = entry.get("INTERFACE")
            type = entry.get("TYPE")
            mac_address_table.append(MACAdressTable(
                mac_address=mac_address,
                vlan=vlan,
                interface=interface,
                type=type,
            ))
        return mac_address_table
