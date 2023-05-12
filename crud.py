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
import pdb ;pdb.set_trace()
def create_member(db: Session, member: schemas.MemberCreate, processed_by_id: int):
    db_member = models.Member(**member.dict(), processed_by_id=processed_by_id)
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member



def get_member(db: Session, member_id: int):
    return db.query(Member).filter(Member.id == member_id).first()


def get_members(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Member).offset(skip).limit(limit).all()


def update_member(db: Session, member: Member, member_update: MemberUpdate):
    for key, value in member_update.dict(exclude_unset=True).items():
        setattr(member, key, value)
    db.add(member)
    db.commit()
    db.refresh(member)
    return member


def delete_member(db: Session, member: Member):
    db.delete(member)
    db.commit()
    return member
