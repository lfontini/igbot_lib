from typing import Literal, Optional

from pydantic import BaseModel


class CiscoLogEvent(BaseModel):
    number: str
    month: str
    day: str
    time: str
    timezone: str
    facility: str
    severity: str
    mnemonic: str
    message: list[str]
