from pydantic import BaseModel
from typing import Optional

class Vlan(BaseModel):
    id: int
    name: Optional[str] = None
    type: str
    interfaces: list[str]
    status_interfaces: list[str]
    port_state_interfaces: list[str]
