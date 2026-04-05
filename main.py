from src.db.models import create_db_and_tables
from contextlib import asynccontextmanager
from fastapi import FastAPI
from dotenv import load_dotenv
from src.user.user import router as UserRouter
from src.account.account import router as AccountRouter
from src.transactions.transactions import router as TransactionRouter
from src.auth.auth import router as AuthRouter
from typing import AsyncGenerator
from fastapi import Depends, HTTPException, Security
from src.auth.jwtSign import get_token
import os

def clear_terminal():
    # Check the operating system name
    if os.name == 'nt':
        # Command for Windows
        _ = os.system('cls')
    else:
        # Command for Linux/macOS (posix)
        _ = os.system('clear')


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # Load the ML model
    print('---')
    print('⌛ Initializing server')
    yield 
    clear_terminal()
    create_db_and_tables()
 
app = FastAPI(lifespan=lifespan)
load_dotenv()

# @app.on_event('startup')
# def on_startup():
#     print('---')
#     print('⌛🟢 Initializing server')


@app.get("/")
def get_data():
    return "hello world!"

#, auth:str=Depends(get_token)
# app.add_route(UserRouter)
app.include_router(AuthRouter)
app.include_router(UserRouter, dependencies=[Depends(get_token)])
app.include_router(AccountRouter, dependencies=[Depends(get_token)])
app.include_router(TransactionRouter, dependencies=[Depends(get_token)])