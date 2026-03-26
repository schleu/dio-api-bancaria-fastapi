from ..db.schemas import TransactionType
from . import accountDB, accountSchema
from ..db import models


MAX_ACCOUNT_PER_AGENCY = 5

async def get_accounts_by_user(user_id:str, offset:int = 0, limit:int=10):
    agencies = await accountDB.get_accounts_by_user(user_id, offset, limit)

    return agencies

async def gen_account_data(agency):
    amount_account = await accountDB.get_balance(agency)

    if amount_account >= MAX_ACCOUNT_PER_AGENCY:
        return {"agency": agency + 1, "number":1}
    
    return {"agency": agency, "number": amount_account+1}

async def create_account(user_id:str):
    last_agency = accountDB.get_last_agency()

    if not last_agency:
        last_agency = 1

    account = await gen_account_data(last_agency)

    agency = account['agency']
    number = account['number']
    
    account = models.Account(
        agency=agency,
        number=number,
        user_id=user_id,
    )

    result = await accountDB.create_account(account)

    return result

async def get_balance(account_id:str):
    balance = await accountDB.get_balance(account_id)
    return balance

async def update_balance(account_id:str, amount:float, type: TransactionType):
    try:
        await accountDB.update_balance(account_id, amount, type)
        return True
    except Exception as e:
        print(e)
        return False