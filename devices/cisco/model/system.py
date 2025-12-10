from pydantic import BaseModel


class System(BaseModel):
    hostname: str
    uptime: str
