from pydantic import BaseModel


class Interface(BaseModel):
    """
    Interface object
    """
    name: str
    link_status: str
    admin_status: str
    duplex: str
    speed: str
    description: str
