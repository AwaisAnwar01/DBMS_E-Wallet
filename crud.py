from sqlalchemy.orm import Session
from models import Member
from schemas import MemberCreate, MemberUpdate
from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session
import sys
sys.path.append(r'/Users/awais/Documents/DBMS_Project/crud.py') 
import schemas,models
from pymysql.err import IntegrityError





#crud operations for user 
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Username or email already exists")
    return db_user


def read_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def read_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    update_data = user.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_user, key, value)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return db_user


#crud operations for members

def create_member(db: Session, member: schemas.MemberCreate):
    db_member = models.Member(**member.dict())
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member



def get_member(db: Session, member_id: int):
    return db.query(Member).filter(Member.Member_id == member_id).first()


def get_members(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Member).offset(skip).limit(limit).all()


def update_member(db: Session, member_id: int, member_update: MemberUpdate):
    member = db.query(Member).filter(Member.Member_id == member_id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    update_data = member_update.dict(exclude_unset=True)
    db.query(Member).filter(Member.Member_id == member_id).update(update_data)
    db.commit()
    db.refresh(member)
    return member



def delete_member(db: Session, member_id: int):
    member = db.query(models.Member).filter(models.Member.Member_id == member_id).first()
    if member:
        db.delete(member)
        db.commit()
        return member
    

    #CRUD operation for currency supported

def add_currency(db: Session, currency_supported: schemas.add_currency):
    #import pdb ; pdb.set_trace()
    currency_in_db = models.Currency_supported(**currency_supported.dict())
    db.add(currency_in_db)
    db.commit()
    db.refresh(currency_in_db)
    return currency_in_db






def get_currency(db: Session, currency_id: int):
    return db.query(models.Currency_supported).filter(models.Currency_supported.currency_id ==currency_id ).first()



def get_currencies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Currency_supported).offset(skip).limit(limit).all()


def update_currency(db: Session, currency_id: int, currency_update: schemas.update_currency):
    currency = db.query(models.Currency_supported).filter(models.Currency_supported.currency_id == currency_id).first()
    if not currency:
        raise HTTPException(status_code=404, detail="Currency not found")
    update_data = currency_update.dict(exclude_unset=True)
    db.query(models.Currency_supported).filter(models.Currency_supported.currency_id == currency_id).update(update_data)
    db.commit()
    db.refresh(currency)
    return currency


def delete_currency(db: Session, currency_id : int):
    currency = db.query(models.Currency_supported).filter(models.Currency_supported.currency_id == currency_id).first()
    if currency:
        db.delete(currency)
        db.commit()
        return currency



def delete_member(db: Session, member_id: int):
    member = db.query(models.Member).filter(models.Member.Member_id == member_id).first()
    if member:
        db.delete(member)
        db.commit()
        return member
    

#crud operations for Deposit


def create_deposit(db: Session, deposit:schemas.DepositCreate):
    db_deposit = models.Deposit(**deposit.dict())
    db.add(db_deposit)
    db.commit()
    db.refresh(db_deposit)
    return db_deposit


def get_deposit(db: Session, deposit_id: int):
    return db.query(models.Deposit).filter(models.Deposit.id == deposit_id).first()


def get_deposits(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Deposit).offset(skip).limit(limit).all()


def update_deposit(db: Session, deposit_id: int, deposit_update: schemas.DepositUpdate):
    deposit = db.query(models.Deposit).filter(models.Deposit.id == deposit_id).first()
    if not deposit:
        raise HTTPException(status_code=404, detail="Deposit not found")
    update_data = deposit_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(deposit, key, value)
    db.commit()
    db.refresh(deposit)
    return deposit



def delete_deposit(db: Session, deposit_id: int):
    db_deposit = db.query(models.Deposit).filter(models.Deposit.id == deposit_id).first()
    if db_deposit:
        db.delete(db_deposit)
        db.commit()
        return db_deposit

#CRUD operation for Gateway

def add_gateway(db: Session, gateway: schemas.add_gateway):
    #import pdb ; pdb.set_trace()
    gateway_in_db = models.gateway(**gateway.dict())
    db.add(gateway_in_db)
    db.commit()
    db.refresh(gateway_in_db)
    return gateway_in_db



def get_gateway(db: Session, gateway_id: int):
    return db.query(models.gateway).filter(models.gateway.gateway_id ==gateway_id ).first()



def get_gateways(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.gateway).offset(skip).limit(limit).all()


def update_gateway(db: Session, gateway_id: int, gateway_update: schemas.update_gateway):
    gateway = db.query(models.gateway).filter(models.gateway.gateway_id == gateway_id).first()
    if not gateway:
        raise HTTPException(status_code=404, detail="gateway not found")
    update_data = gateway_update.dict(exclude_unset=True)
    db.query(models.gateway).filter(models.gateway.gateway_id == gateway_id).update(update_data)
    db.commit()
    db.refresh(gateway)
    return gateway


def delete_gateway(db: Session, gateway_id : int):
    gateway = db.query(models.gateway).filter(models.gateway.gateway_id == gateway_id ).first()
    if gateway:
        db.delete(gateway)
        db.commit()
        return gateway



    
