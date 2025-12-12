from pydantic import BaseModel

class MacAddressTable(BaseModel):
    interface: str
    mac_address: str
    vlan: int
    type: str
