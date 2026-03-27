from fastapi import HTTPException
from datetime import datetime, timedelta
from . import transactionsDB as db
from . import transactionSchema as schema
from ..db.models import Transaction
from ..account import accountService


async def create_transaction(payload:schema.TransactionPayload):
    try:
        data = Transaction(
            account_id=payload.account_id,
            ammount=payload.amount,
            type=payload.type,
        )

        transaction = db.create_transaction(data)

        updated = await accountService.update_balance(payload.account_id, payload.amount, payload.type)
        if not updated:
            raise HTTPException(status_code=400, detail='Balance not updated')

        transaction = await db.update_transaction_status(data, 'success')

        return transaction
    except Exception as e:
        print(e)
        await db.update_transaction_status(data, 'error')


async def create_deposit(payload:schema.DepositPayload):
    print('create_deposit')
    data = schema.TransactionPayload(
        account_id=payload.account_id,
        amount=payload.amount,
        type='deposit'
    )

    transaction = await create_transaction(data)

    return transaction


async def create_withdraw(payload:schema.WithdrawPayload):
    data = schema.TransactionPayload(
        account_id=payload.account_id,
        amount=payload.amount,
        type='withdraw'
    )

    account_balance = await accountService.get_balance(payload.account_id)

    if account_balance < payload.amount:
        raise HTTPException(status_code=400, detail='Insufficient funds')

    transaction =  await create_transaction(data)
    return transaction


async def get_transactions(account_id:str, period:int, offset:int, limit:int):

    today = datetime.today()

    date_limit = today - timedelta(days=period)


    transactions = await db.get_transactions_by_account_id(account_id, date_limit, offset, limit)

    return transactions
