import time
from typing import Annotated
from uuid import uuid4

import jwt 
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPBearer
from pydantic import BaseModel
import os

SECRET = os.getenv('SECRET',"U.*izc$3=&a0^1kKs)+0BJ9xcDnchz*A")
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class AccessToken(BaseModel):
    iss:str #(Issuer)
    sub:int #(Subject)
    aud:str #(Audience)
    exp:float #(Expiration Time)
    iat:float #(Issued At)
    nbf:float #(Not Before Time)
    jti:str #(JWT ID)

class JWTToken(BaseModel):
    access_token: AccessToken


async def sign_JWT(user_id:int):
    try:
        if not SECRET:
            print(f'Secret not found')
            raise HTTPException(status_code=500, detail="Error Server x022")

        now = time.time()

        jti = uuid4().hex

        payload = {
            "iss": "",
            "sub": user_id,
            "aud": "api-bancaria",
            "exp": now * + (60 * 30),
            "iat": now,
            "nbf": now,
            "jti": jti
        }

        token = jwt.encode(payload, SECRET, algorithm=ALGORITHM)

        return { "access_token":  token}
    except Exception as e:
        print(f'An Exception ocurred: {e}')
        raise HTTPException(status_code=400, detail='')
    

async def decode_jwt(token:str):
    try:
        decode_token = jwt.decode(token, SECRET, audience="api-bancaria", algorithms=ALGORITHM)

        print(f'decode_token {decode_token}')

        _token = JWTToken.model_validate({ "access_token": decode_token })

        print(f'_token ')
        print(f'{_token}')
        print(f'{_token.access_token}')

        return _token if _token.access_token.exp >= time.time() else False
    except Exception:
        return False