from pydantic import BaseModel


class User(BaseModel):
    user_id: int
    name: str
    company: str
    address: str
    city: str

    class Config:
        orm_mode = True


class UserIn(BaseModel):
    name: str
    company: str
    address: str
    city: str

    class Config:
        orm_mode = True
