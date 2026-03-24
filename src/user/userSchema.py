from pydantic import BaseModel


class UserPayload(BaseModel):
    __tablename__ = 'user_payload'
    name:str
    password:str

class UserReadPayload():
    offset:int
    limit:int
class User:
    id:str
    name:str