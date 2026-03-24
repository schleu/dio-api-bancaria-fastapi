from typing import Annotated
from fastapi import Query
from sqlmodel import select
from ..db.connection import get_session
from ..db.models import User

db = get_session()

async def get_users(
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100
)->list[User]:
    try:
        print('▶️ Get Users Database')
        users = db.exec(
            select(User)
                .offset(offset)
                .limit(limit)
        ).all()
    
        return users
    except Exception as e:
        print('❌ Error on get users.')
        print(e)
        print('---')


async def get_user(
    user_id:str
)->User:
    try:
        print('▶️ Get Users Database')
        user = db.get(User, user_id)
    
        return user
    except Exception as e:
        print('❌ Error on get users.')
        print(e)
        print('---')


async def create_user(user:User):
    try:
        print(user)
        print('▶️ Create User Database')
        db.add(user)
        db.commit()
        db.refresh(user)

        print('[DB] User Created ')
        return user
    except Exception as e:
        print('❌ Error on create an user.')
        print(e)
        print('---')

async def delete_user():
    try:
        pass
    except Exception as e:
        print('❌ Error on create an user.')
        print(e)
        print('---')


async def update_user():
    try:
        pass
    except Exception as e:
        print('❌ Error on create an user.')
        print(e)
        print('---')