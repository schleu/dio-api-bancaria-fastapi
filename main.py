from src.db.models import create_db_and_tables
from contextlib import asynccontextmanager
from fastapi import FastAPI
from dotenv import load_dotenv
from oauth import router as OauthRouter
from src.user.user import router as UserRouter
from typing import AsyncGenerator
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

# app.add_route(UserRouter)
app.include_router(UserRouter)