from fastapi import APIRouter, HTTPException
from . import transactionService as service
from .transactionSchema import DepositPayload, WithdrawPayload


router = APIRouter(
    prefix='/transaction',
    tags=['transactions'],
)

@router.post('/deposit')
async def create_deposit(payload:DepositPayload):
    try:
        transaction = await service.create_deposit(payload)
   
        if not transaction:
            raise HTTPException(status_code=400, detail='Error on deposit')
        
        return transaction
    except Exception as e:
        print(e)
        raise HTTPException(status_code=e.status_code, detail=e.detail)

@router.post('/withdraw')
async def create_withdraw(payload:WithdrawPayload):
    try:
        transaction = await service.create_withdraw(payload)
   
        if not transaction:
            raise HTTPException(status_code=400, detail='Error on deposit')
        
        return transaction
    except Exception as e:
        print(e)
        raise HTTPException(status_code=e.status_code, detail=e.detail)

@router.get('/historic')
async def get_historic(
        account_id:str='d3280a33-ab8c-40ed-b812-8ba027bede0b', 
        period:int=2, 
        offset:int=0, 
        limit: int=10
    ):
    try:
        MAX_PERIOD_DAYS  =  60

        if period > MAX_PERIOD_DAYS:
            raise HTTPException(status_code=400, detail=f'Max period is {MAX_PERIOD_DAYS} days')


        data = await service.get_transactions(account_id, period, offset, limit)

        return {
            "result": data
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=e.status_code, detail=e.detail)