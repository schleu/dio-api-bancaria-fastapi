from .userDB import User_Db
from .userSchema import UserPayload

class User_Service():
    async def create_user(user:UserPayload):
        try:
            User_Db.create_user(user)
            pass
        except Exception as e:
            print(e)
