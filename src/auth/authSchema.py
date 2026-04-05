from pydantic import BaseModel


class LoginPayload(BaseModel):
    email: str="danilo@email.com"
    password:str="123456"

class SignUpPayload(BaseModel):
    __tablename__ = 'user_payload'
    name:str = 'Danilo Schleu'
    email:str = 'danilo@email.com'
    password:str = '123456'