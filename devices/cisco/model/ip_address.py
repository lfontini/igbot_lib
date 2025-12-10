from typing import List, Optional

from pydantic import BaseModel, Field, computed_field


class IpAddress(BaseModel):
    ip: str
    interface: str
    prefix: str

    @computed_field
    @property
    def cidr(self) -> str:
        return f"{self.ip}/{self.prefix}"
