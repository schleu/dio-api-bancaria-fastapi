from pydantic import BaseModel


class UserPayload(BaseModel):
    __tablename__ = 'user_payload'
    name:str = 'Danilo Schleu'
    email:str = 'danilo@email.com'
    password:str = '123456'

class UserReadPayload():
    offset:int = '100'
    limit:int
class User():
    id:str
    name:str