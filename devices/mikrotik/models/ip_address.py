from typing import List, Optional

from pydantic import BaseModel, Field, computed_field


class IpAddress(BaseModel):
    num: int
    ip: str
    subnet: int
    network: str
    interface: str

    @computed_field(return_type=str)
    def cidr(self):
        return f"{self.ip}/{self.subnet}"
