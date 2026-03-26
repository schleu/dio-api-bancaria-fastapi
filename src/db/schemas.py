from typing import Literal
from datetime import datetime

class User:
    id:str
    name:str
    password:str

class Account:
    id: str
    agency:int
    number:int
    user_id:str

TransactionType = Literal['withdraw','deposit']

TransactionStatus = Literal['processing','success','error']

class Transaction:
    id:str
    account_id:str
    amount:float
    type: TransactionType
    status:TransactionStatus
    created_at: datetime
    updated_at: datetime