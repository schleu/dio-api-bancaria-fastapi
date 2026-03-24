from pydantic import BaseModel
from typing import Literal






class TransactionIn(BaseModel):
    transaction: Literal["withdraw", "deposit"]
    account: str
    amount:float


class User():
    id:str
    name:str

class UserAccount():
    id: str
    id_user:str
    number_account: int
    amount: float


class LoginOut:
    access_token:str

class LoginIn(BaseModel):
    user_id:str