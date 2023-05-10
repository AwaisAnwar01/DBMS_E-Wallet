
from sqlalchemy import Column, Integer, String
from database import Base


# User Model
class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), index=True, nullable=False)
    password = Column(String(50))
    complete_name = Column(String(50),nullable=False)
    email_address = Column(String(120), index=True,unique=True, nullable=False)

