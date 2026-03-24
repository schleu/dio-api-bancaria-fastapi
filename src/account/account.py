
from fastapi import APIRouter, HTTPException
from . import accountService, accountSchema


router = APIRouter(
    prefix='/account',
    tags=['Account'],
)

@router.post('')
async def create_account(payload:accountSchema.AccountPayload):
    try:
        account = await accountService.create_account(payload.user_id)
        if not account:
            raise HTTPException(status_code=400, detail='Error on create account')
        return account
    except Exception as e:
        print(e)
        
@router.get('/{user_id}')
async def get_agencies_by_user(user_id:str, offset:int = 0, limit:int=10):
    agencies = await accountService.get_accounts_by_user(user_id, offset, limit)

    return [agency for agency in agencies]