def normalize(record: dict) -> dict:
    normalized = {}

    for k, v in record.items():
        if v in ("", None):
            continue

        key = k.strip().lower().replace("-", "_")

        if key in ("num", "subnet"):
            try:
                v = int(v)
            except ValueError:
                pass

        if key == "flags":
            v = list(v)

        normalized[key] = v

    return normalized


def parse_arp_mikrotik(raw: str) -> list[dict]:
    with open("devices/mikrotik/parsers/mikrotik_routeros_ip_arp_print.textfsm") as f:
        import textfsm

        fsm = textfsm.TextFSM(f)
        parsed = fsm.ParseText(raw)
        records = [dict(zip(fsm.header, row)) for row in parsed]
        return records
