from fastapi import APIRouter, HTTPException
from . import userService
from .userSchema import UserPayload, User


router = APIRouter(
    prefix='/user',
    tags=['Users'],
)
        
@router.get('')
async def read_users(offset:int = 0, limit:int=10):
    try:
        users = await userService.read_users(limit=limit, offset=offset)
        if not users:
            raise HTTPException(status_code=400, detail='Error on get users')
        
        return [{"id": user.id, "name": user.name} for user in users]
    except Exception as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
        print(e)

@router.get('/{user_id}')
async def get_user(user_id:str):
    try:    
        user = await userService.find_user(user_id)
    
        if not user:
            raise HTTPException(status_code=400, detail='Error on get user')
        return {
            "id": user.id,
            "name": user.name
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=e.status_code, detail=e.detail)
        
@router.delete('/{user_id}')
async def delete_user(user_id:str):
    try:    
        user = await userService.delete_user(user_id)
    
        if not user:
            raise HTTPException(status_code=400, detail='Error on delete user')
        return {"message": "User deleted."}
    except Exception as e:
        print(e)
        return {"message": "User not deleted."}