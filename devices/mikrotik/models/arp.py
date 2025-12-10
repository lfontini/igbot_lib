from pydantic import BaseModel, computed_field


class Arp(BaseModel):
    num: int
    ip: str
    mac_address: str
    interface: str

    @computed_field(return_type=str)
    def mac(self) -> str:
        return f"{self.mac_address}"
