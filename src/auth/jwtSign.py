import time
import jwt 
import os

from uuid import uuid4
from fastapi import Depends, HTTPException, Security
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
JWT_SECRET = os.getenv('JWT_SECRET')
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
AUDIENCE = 'api-bancaria'


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

# Solicita que o token seja passado via header
token_header = APIKeyHeader(name='api-key', auto_error=False)

# Pega token passado pelo header
async def get_token(token: str = Security(token_header)):

    if not token:
        raise HTTPException(status_code=401, detail='Invalid token.')
    
    decoded = await decode_jwt(token)

    if not decoded:
        raise HTTPException(status_code=401, detail='Invalid or expired token.')

    return token


async def sign_JWT(user_id:str):
    try:
        now = time.time()

        jti = uuid4().hex

        payload = {
            "iss": "",
            "sub": user_id,
            "aud": AUDIENCE,
            "exp": now * + (60 * 30),
            "iat": now,
            "nbf": now,
            "jti": jti
        }

        print(f'Created with secret = {JWT_SECRET}')
        

        token = jwt.encode(payload, key=JWT_SECRET, algorithm=ALGORITHM,)

        print('token')
        print(token)

        return token
    except Exception as e:
        print(f'An Exception ocurred: {e}')
        raise HTTPException(status_code=400, detail='')
    

async def decode_jwt(token:str):
    try:
        decode_token = jwt.decode(token, key=JWT_SECRET, algorithms=[ALGORITHM], audience=AUDIENCE)

        print(f'decode_token {decode_token}')

        sub = decode_token.get('sub')
        if not sub:
            raise HTTPException(status_code=401, detail='User not founded.')
        exp = decode_token.get('exp')

        return decode_token if exp >= time.time() else False
    except Exception as e:
        print(e)
        return False