from typing import Optional, List
from datetime import datetime
from uuid import uuid4

from sqlmodel import Field, SQLModel, Relationship
from .schemas import TransactionStatus
from .connection import engine


class User(SQLModel, table=True):
    id: str | None = Field(default=uuid4(), primary_key=True)
    name: str = Field(index=True)
    password: str = Field(index=True)
    accounts: List["Account"] = Relationship(back_populates='user')


class Account(SQLModel, table=True):
    id: str | None = Field(default=uuid4(), primary_key=True)
    agency: int = Field(index=True)
    number: int = Field(index=True)
    user_id: str | None = Field(default=None, foreign_key='user.id')
    user: Optional["User"] = Relationship(back_populates='accounts')
    transaction: Optional["Transaction"] = Relationship(back_populates='accounts')


class Transaction(SQLModel, table=True):
    id: str | None = Field(default=uuid4(), primary_key=True)
    ammount: int = Field(index=True)
    account_id: str | None = Field(default=None, foreign_key='account.id')
    account: Optional["Account"] = Relationship(back_populates='transactions')
    status: str = Field(index=True, default='processing')
    created_date: datetime = Field(index=True, default=datetime.now())
    updated_date: datetime = Field(index=True, default=datetime.now())

def create_db_and_tables():
    try:
        print('⌛ Creating database')
        SQLModel.metadata.create_all(engine)
        print('✅ Database created')
    except Exception as e:
        print('🔴 Error on create database')
        print(f'Error: {e}')