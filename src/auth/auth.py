from fastapi import APIRouter, HTTPException
from . import authService as service
from .authSchema import LoginPayload, SignUpPayload
from src.user import userService


router = APIRouter(
    prefix='/auth',
    tags=['auth'],
)

@router.post('/sign-in')
async def sign_in(payload:LoginPayload):
    try:
        email = payload.email
        password = payload.password
        token = await service.sign(email, password)
   
        if not token:
            raise HTTPException(status_code=400, detail='Error on login')
        
        return {
            'access_token':token,
            'type':'Baerer'
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    
@router.post('/sign-up')
async def sign_up(payload:SignUpPayload):
    try:
        user = await userService.create_user(payload)
        
        if not user:
            raise HTTPException(status_code=400, detail='Error on create user')
        
        return {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=e.status_code, detail=e.detail)