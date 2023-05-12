from typing import Optional
from pydantic import BaseModel

# User schema 
class UserBase(BaseModel):
    username: str
    password: str
    complete_name: str 
    email_address: str 


    class Config:
        orm_mode = True


class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

# Member Schema
class MemberBase(BaseModel):
    First_name: str
    Middle_name: Optional[str] = None
    Last_name: str
    Email: str
    Country: str
    Contact_Number: str
    username: str
    password: str
    account_status: int
    processed_by_id: int


class MemberCreate(MemberBase):
    pass


class MemberUpdate(MemberBase):
    pass


class Member(MemberBase):
    id: int

    class Config:
        orm_mode = True
