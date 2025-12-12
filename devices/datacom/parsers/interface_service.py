from devices.datacom.models.interfaces import Interface
from textfsm import TextFSM

class InterfaceService_DM4100:
    @staticmethod
    def parse(raw_interfaces: str) -> list[Interface]:
        interfaces = []

        with open("devices/datacom/parsers/templates/interfaces_dm_4100.textfsm") as template:
            fsm = TextFSM(template)
            result = fsm.ParseText(raw_interfaces)

        headers = fsm.header  # nomes dos campos
        for row in result:
            entry = dict(zip(headers, row))
            interfaces.append(
                Interface(
                    name=entry.get("INTERFACE", ""),
                    link_status=entry.get("LINK_STATUS", ""),
                    admin_status=entry.get("ADMIN_STATUS", ""),
                    duplex=entry.get("SPEED_DUPLEX", ""),
                    speed=entry.get("OPER_SPEED_DUPLEX", ""),
                    description=entry.get("NAME", ""),
                )
            )

        return interfaces


class InterfaceService_DM4050:
    @staticmethod
    def parse(raw_interfaces: str) -> list[Interface]:
        interfaces = []

        with open("devices/datacom/parsers/templates/interfaces_dm_4050.textfsm") as template:
            fsm = TextFSM(template)
            result = fsm.ParseText(raw_interfaces)

        headers = fsm.header  # nomes dos campos

        for row in result:
            entry = dict(zip(headers, row))
            print(entry)
            speed = entry.get("SPEED", "") if entry.get("SPEED", "") != "" else entry.get("OPER_SPEED_DUPLEX", "")
            interfaces.append(
                Interface(
                    name=entry.get("INTERFACE", ""),
                    link_status=entry.get("LINK_STATUS", ""),
                    admin_status=entry.get("ADMIN_STATUS", ""),
                    duplex=entry.get("DUPLEX", ""),
                    speed=speed,
                    description=entry.get("DESCRIPTION", ""),
                )
            )

        return interfaces


class InterfaceService_DM4170:
    @staticmethod
    def parse(raw_interfaces: str) -> list[Interface]:
        interfaces = []

        with open("devices/datacom/parsers/templates/interfaces_dm_4170.textfsm") as template:
            fsm = TextFSM(template)
            result = fsm.ParseText(raw_interfaces)

        headers = fsm.header  # nomes dos campos
        for row in result:
            entry = dict(zip(headers, row))
            interfaces.append(
                Interface(
                    name=entry.get("INTERFACE", ""),
                    link_status=entry.get("LINK_STATUS", ""),
                    admin_status=entry.get("ADMIN_STATUS", ""),
                    duplex=entry.get("DUPLEX", ""),
                    speed=entry.get("SPEED", ""),
                    description=entry.get("DESCRIPTION", ""),
                )
            )

        return interfaces


class InterfaceService_DM4370:
    @staticmethod
    def parse(raw_interfaces: str) -> list[Interface]:
        interfaces = []

        with open("devices/datacom/parsers/templates/interfaces_dm_4370.textfsm") as template:
            fsm = TextFSM(template)
            result = fsm.ParseText(raw_interfaces)

        headers = fsm.header  # nomes dos campos
        for row in result:
            entry = dict(zip(headers, row))
            interfaces.append(
                Interface(
                    name=entry.get("INTERFACE", ""),
                    link_status=entry.get("LINK_STATUS", ""),
                    admin_status=entry.get("ADMIN_STATUS", ""),
                    duplex=entry.get("DUPLEX", ""),
                    speed=entry.get("SPEED", ""),
                    description=entry.get("DESCRIPTION", ""),
                )
            )

        return interfaces
