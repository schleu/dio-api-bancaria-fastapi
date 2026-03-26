from fastapi import APIRouter, HTTPException
from . import transactionService as service
from .transactionSchema import DepositPayload, TransactionPayload


router = APIRouter(
    prefix='/transaction',
    tags=['transactions'],
)

@router.post('/deposit')
async def create_deposit(payload:DepositPayload):
    try:
        print('rota de deposito')
        transaction = await service.create_deposit(payload)

        print('')
        print('')
        print('')
        print('transaction')
        print(transaction)
        print('')
        print('')
        print('')
    
        # if not user:
        #     raise HTTPException(status_code=400, detail='Error on create user')
        
        return transaction
    except Exception as e:
        print(e)
        raise HTTPException(status_code=e.status_code, detail=e.detail)

# @router.post('/withdraw')
# async def create_withdraw(user:TransactionPayload):
#     try:
#         user = await service.create_transaction(user)
        
#         if not user:
#             raise HTTPException(status_code=400, detail='Error on create user')
        
#         return {
#             "id": user.id,
#             "name": user.name,
#             "email": user.email
#         }
#     except Exception as e:
#         print(e)
#         raise HTTPException(status_code=e.status_code, detail=e.detail)

# @router.get('/historic')
# async def get_historic(account_id:str):
#     try:
#         user = await service.create_transaction(user)
        
#         if not user:
#             raise HTTPException(status_code=400, detail='Error on create user')
        
#         return {
#             "id": user.id,
#             "name": user.name,
#             "email": user.email
#         }
#     except Exception as e:
#         print(e)
#         raise HTTPException(status_code=e.status_code, detail=e.detail)