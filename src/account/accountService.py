from . import accountDB, accountSchema
from ..db import models

MAX_ACCOUNT_PER_AGENCY = 5

async def get_accounts_by_user(user_id:str, offset:int = 0, limit:int=10):
    print('get_accounts_by_user')
    agencies = await accountDB.get_accounts_by_user(user_id, offset, limit)

    print('agencies')
    print(agencies)

    return agencies

async def gen_account_data(agency:int):
    amount_account = await accountDB.get_account_amount_by_agency(agency)

    if amount_account >= MAX_ACCOUNT_PER_AGENCY:
        return {"agency": agency + 1, "number":1}
    
    return {"agency": agency, "number": amount_account+1}

async def create_account(user_id:str):
    last_agency = accountDB.get_last_agency()

    if not last_agency:
        last_agency = 1
        print(f'agency actual {last_agency}')

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