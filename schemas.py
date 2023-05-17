from typing import Optional
from pydantic import BaseModel,constr
from datetime import datetime

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
    currency_id : int 
    
    class config:
        orm_mode = True




class WithdrawalBase(BaseModel):
    transaction_code: str
    amount: float
    charged: float
    to_receive: float
    date_time: datetime
    method: str
    status: int
    remarks: str


class WithdrawalCreate(WithdrawalBase):
    member_id: int


class WithdrawalUpdate(WithdrawalBase):
    pass


class Withdrawal(WithdrawalBase):
    withdrawal_id: int
    member_id: int

    class Config:
        orm_mode = True


class DepositBase(BaseModel):
    transaction_code: str
    member_id: int
    deposit_amount: float
    currency_id: int
    date_time: datetime
    gateway_id: int
    status: int
    remarks: str

    class Config:
        orm_mode = True


class DepositCreate(DepositBase):
    pass


class DepositUpdate(DepositBase):
    pass


class Deposit(DepositBase):
    id: int

    class Config:
        orm_mode = True


#Gateway  schema

class gateway_base(BaseModel):
    gateway_name : str
    gateway_status: bool
    gateway_type : str
  
    
    class Config:
        orm_mode = True
    

class add_gateway(gateway_base):
    pass    

class update_gateway(gateway_base):
    pass

class gateway(gateway_base):
    gateway_id : int 
    
    class config:
        orm_mode = True


class TransactionLogBase(BaseModel):
    member_id: int
    transaction_type: int
    amount: float
    status: int


class TransactionLogCreate(TransactionLogBase):
    pass


class TransactionLogUpdate(TransactionLogBase):
    pass


class TransactionLog(TransactionLogBase):
    transaction_log_id: int

    class Config:
        orm_mode = True
