from pydantic import BaseModel
class UserBase(BaseModel):
    username: str
    email: str

class UserIn(UserBase):
    password: str
    re_password: str

class UserOut(UserBase):
    id: int
    class Config:
        orm_mode =True