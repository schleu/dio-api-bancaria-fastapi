from pydantic import BaseModel


class UserPayload(BaseModel):
    name:str
    password:str
    password:str