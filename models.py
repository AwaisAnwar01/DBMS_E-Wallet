from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String,ForeignKey,Boolean,Float,DateTime
from database import Base


# User Model
class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), index=True, nullable=False)
    password = Column(String(50))
    complete_name = Column(String(50),nullable=False)
    email_address = Column(String(120), index=True,unique=True, nullable=False)


class Member(Base):
    __tablename__ = "Members"

    Member_id = Column(Integer,primary_key= True,index = True)
    First_name = Column(String(20))
    Middle_name = Column(String(20))  #optional Attribute
    Last_name = Column(String(20))
    Email = Column(String(150), index=True,unique=True, nullable=False)
    Country = Column(String(120))
    Contact_Number = Column(String(20),unique=True, nullable=False)
    username = Column(String(50), unique=True, index=True)
    password = Column(String(50))
    account_status = Column(Integer)
    processed_by_id = Column(Integer, ForeignKey("Users.id"))
    processed_by = relationship("User", backref="processed_by")



#Currency_Support Model

class Currency_supported(Base):
    __tablename__= "Currency_Supported"

    currency_name= Column(String(25))
    currency_id=Column(Integer , primary_key= True , index = True)
    currency_symbol=Column(String(10))
    status= Column( Boolean , default= False)
    USD_equivalent=Column(Integer)



#Deposit Model
class Deposit(Base):
    __tablename__ = "deposits"

    id = Column(Integer, primary_key=True, index=True)
    transaction_code = Column(String(20), unique=True)
    member_id = Column(Integer, ForeignKey("members.id"))
    deposit_amount = Column(Float)
    currency_id = Column(Integer, ForeignKey("currency_supported.id"))
    date_time = Column(DateTime, default=datetime.utcnow())
    payment_gateway_id = Column(Integer, ForeignKey("gateways.id"))
    status = Column(Integer, default=0)
    remarks = Column(String(255))

    member = relationship("Member", back_populates="deposits")
    currency_supported = relationship("CurrencySupported", back_populates="deposits")
    gateway = relationship("Gateway", back_populates="deposits")
