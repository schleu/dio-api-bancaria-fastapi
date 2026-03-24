from fastapi import HTTPException
from typing import List
from . import userDB
from .userSchema import UserPayload, User, UserReadPayload
from ..db import models
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)


def encrypt_password(password:str):
    return password_hash.hash(password)



async def create_user(payload:UserPayload)->User:
    try:
        print('▶️ User Service')

        encrypted_password = encrypt_password(payload.password)

        user = models.User(
            name=payload.name,
            password=encrypted_password
        )
        
        # Alternativa mais curta
        #user = models.User(**payload.dict())
      
        user_created = await userDB.create_user(user=user)
        return user_created
    except Exception as e:
        print(e)


async def read_user(data:UserReadPayload)->List[User]:
    try:
        print('▶️ User Service')
        user_created = await userDB.get_users(limit=data.limit, offset=data.offset)
        return user_created
    except Exception as e:
        print(e)


async def find_user(user_id:str)->User:
    try:
        print('▶️ User Service')
        if not user_id:
            raise HTTPException(status_code=400, detail='User id request.')
        
        user = await userDB.get_user(user_id)

        if not user:
            raise HTTPException(status_code=404, detail='User not founded')
        return user
    except Exception as e:
        print(e)

