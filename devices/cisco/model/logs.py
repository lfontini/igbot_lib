from pydantic import BaseModel


from pydantic import BaseModel
from typing import Optional, Literal


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

