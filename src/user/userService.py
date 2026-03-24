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
        encrypted_password = encrypt_password(payload.password)

        user = models.User(
            name=payload.name,
            email=payload.email,
            password=encrypted_password
        )

        # Alternativa mais curta
        #user = models.User(**payload.dict())

        user_finded = await userDB.get_user_by_email(payload.email)

        if user_finded:
            raise HTTPException(status_code=400, detail='User already exist.')
        
      
        user_created = await userDB.create_user(user=user)
        return user_created
    except Exception as e:
        print(e)


async def read_users(offset:int = 0, limit:int=10)->List[User]:
    try:
        user_created = await userDB.get_users(limit=limit, offset=offset)
        return user_created
    except Exception as e:
        print(e)


async def find_user(user_id:str)->User:
    try:
        if not user_id:
            raise HTTPException(status_code=400, detail='User id request.')
        
        user = await userDB.get_user_by_id(user_id)

        if not user:
            raise HTTPException(status_code=404, detail='User not founded')
        return user
    except Exception as e:
        print(e)

async def delete_user(user_id:str)->User:
    try:
        if not user_id:
            raise HTTPException(status_code=400, detail='User id request.')
        
        user = await userDB.delete_user(user_id)

        return user
    except Exception as e:
        print(e)

