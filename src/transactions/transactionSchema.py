from ..db.schemas import TransactionType
from pydantic import BaseModel

class TransactionPayload(BaseModel):
    account_id: str
    amount:float
    type:TransactionType

class DepositPayload(BaseModel):
    account_id: str="d3280a33-ab8c-40ed-b812-8ba027bede0b"
    amount:float="10.0"

class WithdrawPayload(BaseModel):
    account_id: str="d3280a33-ab8c-40ed-b812-8ba027bede0b"
    amount:float="10.0"