from fastapi import APIRouter, HTTPException
from .userService import User_Service
from .userSchema import UserPayload

router = APIRouter(
    prefix='/user',
    tags=['Users']
    )



@router.post('')
async def create_user(user:UserPayload):

    try:
        user = User_Service.create_user()
        if not user:
            raise HTTPException()
        return user
    except Exception as e:
        print(e)
        
