from typing import Annotated
from fastapi import Query
from sqlmodel import select
from ..db.connection import conn
from ..db.models import User

class User_Db():

    async def get_users(
        offset: int = 0,
        limit: Annotated[int, Query(le=100)] = 100
    ):
        try:
            users = await conn.exec(select(User).offset(offset).limit(limit))
        
            return users
        except Exception as e:
            print('❌ Error on get users.')
            print(e)
            for i in range(3): print('---')
    
    async def create_user(user:User):
        try:
            conn.add(user)
            conn.commit()
            conn.refresh(user)
            return user
        except Exception as e:
            print('❌ Error on create an user.')
            print(e)
            for i in range(3): print('---')
    
    async def delete_user():
        try:
            pass
        except Exception as e:
            print('❌ Error on create an user.')
            print(e)
            for i in range(3): print('---')
    
    async def update_user():
        try:
            pass
        except Exception as e:
            print('❌ Error on create an user.')
            print(e)
            for i in range(3): print('---')