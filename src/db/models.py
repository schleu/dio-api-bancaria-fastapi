from typing import Optional, List
from datetime import datetime, timezone
from uuid import uuid4

from sqlmodel import Field, SQLModel, Relationship, Session
from .schemas import TransactionStatus
from .connection import engine

def create_id():
    return str(uuid4())

class User(SQLModel, table=True):
    id: str | None = Field(default_factory=create_id, primary_key=True)
    name: str = Field(index=True)
    email: str = Field(index=True)
    password: str = Field(index=True)
    deleted:bool = Field(default=False)
    accounts: List["Account"] = Relationship(back_populates='user')


def get_now():
    return datetime.now(timezone.utc)

class Account(SQLModel, table=True):
    id: str | None = Field(default_factory=create_id, primary_key=True)
    status: str = Field(index=True, default='actived')
    created_date: datetime = Field(index=True, default_factory=get_now)
    updated_date: datetime = Field(index=True, default_factory=get_now)
    agency: int = Field(index=True)
    number: int = Field(index=True)
    balance:float = Field(default=0)
    user_id: str | None = Field(default=None, foreign_key='user.id')
    user: Optional["User"] = Relationship(back_populates='accounts')
    transactions: List["Transaction"] = Relationship(back_populates='account')

class Transaction(SQLModel, table=True):
    id: str | None = Field(default_factory=create_id, primary_key=True)
    ammount: float = Field(index=True)
    status: str = Field(index=True, default='processing')
    created_date: datetime = Field(index=True, default_factory=get_now)
    updated_date: datetime = Field(index=True, default_factory=get_now)
    type:str = Field(index=True)
    account_id: str | None = Field(default=None, foreign_key='account.id')
    account: Optional["Account"] = Relationship(back_populates='transactions')


def populate_tables():
    with Session(engine) as session:
        # cria usuário
        user = User(
            id="a33b4dc5-0740-4118-9e0a-fa38c16a93b3",
            name="Danilo",
            email="danilo@email.com",
            password="123456"
        )

        session.add(user)
        session.commit()
        session.refresh(user)

        # cria conta vinculada ao usuário
        account = Account(
            id="d3280a33-ab8c-40ed-b812-8ba027bede0b",
            agency=1,
            number=1,
            user_id=user.id
        )

        session.add(account)
        session.commit()

    print('✅ Database created with initial data')


def create_db_and_tables():
    try:
        print('⌛ Creating database')
        SQLModel.metadata.create_all(engine)
        populate_tables()
        print('✅ Database created')
    except Exception as e:
        print('🔴 Error on create database')
        print(f'Error: {e}')