from devices.cisco.model.interfaces import Interface


class InterfaceService:
    @staticmethod
    def parse(raw_interfaces: list) -> list[Interface]:
        interfaces = []

        for entry in raw_interfaces:
            interfaces.append(
                Interface(
                    name=entry.get("interface", ""),
                    link_status=entry.get("link_status", ""),
                    protocol_status=entry.get("protocol_status", ""),
                    mtu=entry.get("mtu", ""),
                    duplex=entry.get("duplex", ""),
                    speed=entry.get("speed", ""),
                    ip=entry.get("ip_address", ""),
                    description=entry.get("description", ""),
                )
            )

        return interfaces
