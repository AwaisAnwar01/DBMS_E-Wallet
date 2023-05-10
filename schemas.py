from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    password: str
    complete_name: str 
    email_address:  str 


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
