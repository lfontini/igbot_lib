from pydantic import BaseModel


class Interface(BaseModel):
    id: int
    status: str
    name: str
    type: str
    mtu: int
