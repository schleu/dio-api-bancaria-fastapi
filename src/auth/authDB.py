from ..db.connection import get_session
from ..db.models import Transaction, get_now, TransactionStatus
from sqlmodel import select
from sqlalchemy import desc
from datetime import datetime

db = get_session()

async def create_transaction(data:Transaction):
    try:
        db.add(data)
        db.commit()
        db.refresh(data)
        return data
    except Exception as e:
        print('❌ Error on create transaction.')
        print(e)

async def update_transaction_status(data:Transaction, status:TransactionStatus):
    try:
        # data.updated_date = get_now()
        data.status = status

        db.add(data)
        db.commit()
        db.refresh(data)
        return data
    except Exception as e:
        print('❌ Error on update transaction status.')
        print(e)

async def  get_transactions_by_account_id(account_id:str, date_limit:datetime, offset:int, limit: int):

    print('date_limit')
    print(date_limit)
    data = db.exec(
        select(Transaction)
        .where(Transaction.account_id ==  account_id)
        .where(Transaction.created_date >= date_limit)
        .offset(offset)
        .limit(limit)
        .order_by(desc(Transaction.created_date))
    ).all()

    print(data)

    return data