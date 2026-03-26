from ..db.connection import get_session
from ..db.models import Transaction, get_now, TransactionStatus

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
        print('')
        print(data)
        print('')
        print('')
        # data.updated_date = get_now()
        data.status = status

        print(data)
        print('')

        db.add(data)
        db.commit()
        db.refresh(data)
        return data
    except Exception as e:
        print('❌ Error on update transaction status.')
        print(e)
