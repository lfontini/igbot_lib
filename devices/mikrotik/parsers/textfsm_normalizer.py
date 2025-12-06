def normalize_record(record: dict) -> dict:
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
