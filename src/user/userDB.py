from typing import Annotated
from fastapi import Query, HTTPException
from sqlmodel import select
from ..db.connection import get_session
from ..db.models import User

db = get_session()

async def get_users(
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100
)->list[User]:
    try:
        users = db.exec(select(User.id, User.name).offset(offset).limit(limit)).all()
    
        return users
    except Exception as e:
        print('❌ Error on get users.')
        print(e)


async def get_user_by_id(
    user_id:str
)->User:
    try:
        user = db.exec(select(User).where(User.id == user_id).where(User.deleted == "0")).first()
    
        return user
    except Exception as e:
        print(f'❌ Error on get user with id {user_id}.')
        print(e)


async def get_user_by_email(
    email:str
)->User:
    try:
        user = db.exec(select(User).where(User.email == email).where(User.deleted == "0")).first()
    
        return user
    except Exception as e:
        print(f'❌ Error on get user with id {email}.')
        print(e)


async def create_user(user:User):
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except Exception as e:
        print('❌ Error on create an user.')
        print(e)

async def delete_user(user_id:str)->bool:
    try:
        user = db.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Hero not found")

        user.deleted = True

        db.add(user)
        db.commit()
        db.refresh(user)

        return True
    except Exception as e:
        print('❌ Error on create an user.')
        print(e)
        print('---')
        return False


async def update_user():
    try:
        pass
    except Exception as e:
        print('❌ Error on create an user.')
        print(e)
        print('---')