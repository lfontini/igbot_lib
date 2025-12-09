from pydantic import BaseModel, Field, computed_field
from typing import List, Optional

class IpAddress(BaseModel):
    num: int
    ip: str
    subnet: int
    network: str
    interface: str

    @computed_field
    @property
    def cidr(self) -> str:
        return f"{self.ip}/{self.subnet}"
