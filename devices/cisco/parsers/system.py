from devices.cisco.model.system import System


class SystemParser:
    @staticmethod
    def parse(raw_system: list) -> list[System]:
        systems = []

        for entry in raw_system:
            systems.append(
                System(
                    hostname=entry.get("hostname", ""),
                    uptime=entry.get("uptime", ""),
                )
            )

        return systems
