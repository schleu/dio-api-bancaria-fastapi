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

class TransactionType: Literal['withdraw','deposit']

class TransactionStatus: Literal['processing','success','error']

class Transaction:
    id:str
    user_id:str
    amount:float
    type: TransactionType
    status:TransactionStatus
    created_at: datetime
    updated_at: datetime