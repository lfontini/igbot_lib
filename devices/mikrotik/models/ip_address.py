from pydantic import BaseModel, Field, computed_field
from typing import List, Optional

class IpAddress(BaseModel):
    num: int
    ip: str
    subnet: int
    network: str
    interface: str
    flags: List[str] = Field(default_factory=list)
    comment: Optional[str] = None

    @computed_field
    @property
    def cidr(self) -> str:
        return f"{self.ip}/{self.subnet}"
