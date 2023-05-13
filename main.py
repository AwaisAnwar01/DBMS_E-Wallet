from fastapi import FastAPI,HTTPException,Query,Depends,status
from typing import Optional,List
# from pydantic import BaseModel
import mysql.connector
import time
from database import Base,engine,SessionLocal
from models import User
#from . import models,schemas
from sqlalchemy.orm import Session
from pymysql.err import IntegrityError
from pydantic import ValidationError

import sys
sys.path.append(r'/Users/awais/Documents/DBMS_Project/main.py') 
import models , schemas , crud
from crud import create_user, read_users, read_user, update_user, delete_user
models.Base.metadata.create_all(bind=engine)


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

while True:
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="Qwert!098765",
            database="Digital_Wallet"
        )
        print("Connected")
        break


    except Exception as error:
        print("Connection Failed")
        print("Error", error)
        time.sleep(2)


mycursor = mydb.cursor()

# create a new user
@app.post("/users/", response_model=schemas.UserBase)
def create_user_api(user: schemas.UserCreate, db: Session = Depends(get_db)):
     db_user = create_user(db=db, user=user)
     return schemas.UserBase.from_orm(db_user)


# get all users
@app.get("/users/", response_model=List[schemas.User])
def read_users_api(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = read_users(db=db, skip=skip, limit=limit)
    return users


# get a specific user by id
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user_api(user_id: int, db: Session = Depends(get_db)):
    return read_user(db=db, user_id=user_id)


# update a user by id
@app.put("/users/{user_id}", response_model=schemas.User)
def update_user_api(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    return update_user(db=db, user_id=user_id, user=user)


# delete a user by id
@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user_api(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db=db, user_id=user_id)


# CRUD operations for Member entity

#create a new member

@app.post("/members/", response_model=schemas.Member)
def create_member_api(member: schemas.MemberCreate, db: Session = Depends(get_db)):
    try:
        processed_by_id = member.processed_by_id
        print(processed_by_id)
        return crud.create_member(db=db, member=member)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))
    
    
# get all members
@app.get("/members/", response_model=List[schemas.Member])
def read_members(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    members = crud.get_members(db, skip=skip, limit=limit)
    return members

# get a specific member by id
@app.get("/members/{member_id}", response_model=schemas.Member)
def read_member(member_id: int, db: Session = Depends(get_db)):
    db_member = crud.get_member(db, member_id=member_id)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return db_member

# update a member by id
@app.put("/members/{member_id}", response_model=schemas.Member)
def update_member(member_id: int, member_update: schemas.MemberUpdate, db: Session = Depends(get_db)):
    db_member = crud.get_member(db, member_id=member_id)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return crud.update_member(db=db, member_id=member_id,member_update=member_update)


# delete a member by id``
@app.delete("/members/{member_id}", response_model=schemas.Member)
def delete_member(member_id: int, db: Session = Depends(get_db)):
    db_member = crud.get_member(db, member_id=member_id)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return crud.delete_member(db=db, member_id = member_id)



# API's for operations of currency_supported entity

# Adding a New currency 

@app.post("/currency_supported/", response_model=schemas.currency_supported)
def add_currency(currency_supported: schemas.add_currency,  db: Session = Depends(get_db)):
    try:
        return crud.add_currency(db=db, currency_supported=currency_supported)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))
    

    
 #get all currencies
@app.get("/currency_supported/", response_model=List[schemas.currency_supported])
def read_currencies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    currencies = crud.get_currencies(db, skip=skip, limit=limit)
    return currencies

# get a specific currency by id
@app.get("/currency_supported/{currency_id}", response_model=schemas.currency_supported)
def read_currency(currency_id: int, db: Session = Depends(get_db)):
    db_currency = crud.get_currency(db, currency_id=currency_id)
    if db_currency is None:
        raise HTTPException(status_code=404, detail="Currency not found")
    return db_currency

# update a currency by id
@app.put("/currency_supported/{currency_id}", response_model=schemas.currency_supported)
def update_currency(currency_id: int, currency_update: schemas.update_currency, db: Session = Depends(get_db)):
    db_currency = crud.get_currency(db, currency_id= currency_id)
    if db_currency is None:
        raise HTTPException(status_code=404, detail="currency not found")
    return crud.update_currency(db=db, currency_id=currency_id, currency_update= currency_update)



# delete a currency by id
@app.delete("/currency_supported/{currenc_id}", response_model=schemas.currency_supported)
def delete_currency(currency_id: int, db: Session = Depends(get_db)):
    db_currency = crud.get_currency(db, currency_id=currency_id)
    if db_currency is None:
        raise HTTPException(status_code=404, detail="currency not found")
    return crud.delete_currency(db=db,currency_id = currency_id)  


@app.delete("/members/{member_id}", response_model=schemas.Member)
def delete_member(member_id: int, db: Session = Depends(get_db)):
    db_member = crud.get_member(db, member_id=member_id)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return crud.delete_member(db=db, member_id = member_id)
