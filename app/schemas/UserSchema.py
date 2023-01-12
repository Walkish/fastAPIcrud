from pydantic import BaseModel


class Users(BaseModel):
    user_id: int
    name: str
    company: str
    address: str
    city: str

    class Config:
        orm_mode = True
