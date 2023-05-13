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
    


    
