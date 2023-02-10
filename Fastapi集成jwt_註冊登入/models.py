from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()


class User(BaseModel):
    __tablename__ = "jwt_users"  # 指定数据库中表的名字
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255))
    password = Column(String(255))
    email =Column(String(255))
    def __str__(self):
        return f"id:{self.id} name:{self.username} password:{self.password} email:{self.email}"