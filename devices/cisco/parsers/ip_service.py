from devices.cisco.model.ip_address import IpAddress


class IpService:
    @staticmethod
    def parse(raw_ips: list) -> list[IpAddress]:
        ips = []

        for entry in raw_ips:
            if entry.get("ip_address"):
                ips.append(
                    IpAddress(
                        ip=entry["ip_address"][0],
                        interface=entry["interface"],
                        prefix=entry["prefix_length"][0],
                    )
                )

        return ips
