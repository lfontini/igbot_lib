from devices.cisco.model.logs import CiscoLogEvent


class LogParser:
    @staticmethod
    def parse(raw_logs: list[dict]) -> list[CiscoLogEvent]:
        logs = []

        for entry in raw_logs:
            logs.append(
                CiscoLogEvent(
                    number=entry.get("number", ""),
                    month=entry.get("month", ""),
                    day=entry.get("day", ""),
                    time=entry.get("time", ""),
                    timezone=entry.get("timezone", ""),
                    facility=entry.get("facility", ""),
                    severity=entry.get("severity", ""),
                    mnemonic=entry.get("mnemonic", ""),
                    message=entry.get("message", ""),
                )
            )

        return logs
