from pydantic import BaseModel
class UserBase(BaseModel):
    name: str


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    id: int
    class Config:
        orm_mode =True