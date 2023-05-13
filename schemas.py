from typing import Optional
from pydantic import BaseModel,constr

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
   # id: int

    class Config:
        orm_mode = True



#currency supported schema

class currency_supported_base(BaseModel):
    currency_name : str
    currency_symbol: constr(max_length=10)
    status : bool
    USD_equivalent : int
    
    class Config:
        orm_mode = True
    

class add_currency(currency_supported_base):
    pass    

class update_currency(currency_supported_base):
    pass

class currency_supported(currency_supported_base):
  #  currency_id : int 
    
    class config:
        orm_mode = True