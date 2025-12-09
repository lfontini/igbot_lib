from pydantic import BaseModel


class IpArp(BaseModel):
    ip: str
    interface: str
    mac: str
    age: str
