from fastapi import APIRouter, HTTPException
from . import userService
from .userSchema import UserPayload


router = APIRouter(
    prefix='/user',
    tags=['Users'],
)

@router.post('',)
async def create_user(user:UserPayload):
    try:
        print('▶️ Entrou na rota')
        user = await userService.create_user(user)
        print(user)
        if not user:
            raise HTTPException(status_code=400, detail='Error on create user')
        return dict(user)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail='Error on create user')
        
@router.get('')
async def read_users(offset:int = 0, limit:int=10):
    try:
        users = await userService.read_user(data={
            limit,
            offset
        })
        print(users)
        if not users:
            raise HTTPException(status_code=400, detail='Error on get users')
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail='Error on get users')
        
@router.get('/{user_id}')
async def get_user(user_id:str):
    try:
        print()
        users = await userService.find_user(user_id)
        print(users)
        if not users:
            raise HTTPException(status_code=400, detail='Error on get users')
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail='Error on get users')