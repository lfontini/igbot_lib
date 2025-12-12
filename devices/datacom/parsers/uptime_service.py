from devices.datacom.models.uptime import Uptime
from textfsm import TextFSM

class UptimeService:
    @staticmethod
    def parse(raw: str) -> Uptime:
        with open("devices/datacom/parsers/templates/uptime_dm_4370.textfsm") as template:
            fsm = TextFSM(template)
            result = fsm.ParseText(raw)

        headers = fsm.header  # nomes dos campos
        for row in result:
            entry = dict(zip(headers, row))
            return Uptime(uptime=entry.get("UPTIME", ""))
