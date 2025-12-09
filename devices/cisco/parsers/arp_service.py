from devices.cisco.model.ip_arp import IpArp

class ArpService:
    @staticmethod
    def parse(raw_arp: list) -> list[IpArp]:
        arps = []

        for entry in raw_arp:
            if entry.get("ip_address"):
                arps.append(
                    IpArp(
                        ip=entry["ip_address"],
                        interface=entry["interface"],
                        mac=entry["mac_address"],
                        age=entry["age"]
                    )
                )

        return arps
