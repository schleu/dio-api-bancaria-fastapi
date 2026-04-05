from fastapi import HTTPException
from datetime import datetime, timedelta
from . import authDB as db
from . import authSchema as schema
from ..db.models import Transaction
from ..user import userService
from . import jwtSign
import jwt
import os


async def sign(email, password):
    user = await userService.sign_in(email, password)

    if not user:
        raise HTTPException(status_code=400, detail='Email or Password is invalid.')

    token = await jwtSign.sign_JWT(user.id)
    
    
    return token
