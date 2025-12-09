from pydantic import BaseModel

class Interface(BaseModel):
    name: str
    link_status: str
    protocol_status: str
    mtu: int
    duplex: str
    ip: str
    description: str
    
    
