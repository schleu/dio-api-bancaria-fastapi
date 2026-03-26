from typing import Annotated
from fastapi import Query
from sqlmodel import select
from sqlalchemy import func, desc

from ..db.connection import get_session
from ..db.models import User, Account
from ..db.schemas import TransactionType

db = get_session()

async def get_accounts_by_user(
    user_id: str,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100
)->list[User]:
    try:
        users = db.exec(
                select(Account)
                .where(Account.user_id == user_id)
                .offset(offset)
                .limit(limit)
            ).all()
        print(users)
    
        return users
    except Exception as e:
        print('❌ Error on get users.')
        print(e)


async def create_account(data:Account):
    try:
        db.add(data)
        db.commit()
        db.refresh(data)

        return data
    except Exception as e:
        print('❌ Error on create an Account.')
        print(e)

def get_last_agency():
    try:
        last_agency = db.exec(
            select(Account.agency).order_by(desc(Account.agency))
        ).first()
        
        return last_agency
    except Exception as e:
        print('❌ Error on create an Account.')
        print(e)

async def get_account_amount_by_agency(agency:int):
    try:
        data = db.exec(
            select(func.count())
            .select_from(Account)
            .where(Account.agency == agency)
        ).one()
        
        return data
    except Exception as e:
        print('❌ [DB] Error on create an Account.')
        print(e)


async def get_balance(account_id:str):
    try:
        data = db.exec(
            select(Account.balance)
            .where(Account.id == account_id)
        ).one()
        
        return data
    except Exception as e:
        print(f'❌ [DB] Error on get balance for {account_id}.')
        print(e)

async def update_balance(account_id:str, value:float, type:TransactionType ):
    try:
        print('update_balance')
        data = db.get(Account,account_id)

        if type == 'deposit':
            data.balance += value
        else:
            data.balance -= value

        db.add(data)
        db.commit()
        db.refresh(data)
        
        return data
    except Exception as e:
        db.rollback()
        print('❌ [DB] Error on update balance.')
        print(e)
    finally:
        pass