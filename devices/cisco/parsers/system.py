from devices.cisco.model.system import System
from pathlib import Path
import textfsm

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

class SystemParserTextFSM:
    @staticmethod
    def parse(raw_system: str) -> list:
        template_path = (
            Path(__file__)
            .resolve()
            .parent / "templates" / "cisco_ios_show_version.textfsm"
        )

        with open(template_path) as f:
            fsm = textfsm.TextFSM(f)
            parsed = fsm.ParseText(raw_system)
            records = [dict(zip(fsm.header, row)) for row in parsed]
            return records
