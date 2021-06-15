from fastapi import FastAPI
from db import databases
from users.router import router as userrouter
from starlette.requests import Request

app = FastAPI()

@app.on_event("startup")
async def startup():
    await databases.connect()

@app.on_event("shutdown")
async def shutdown():
    await databases.disconnect()

app.include_router(userrouter)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.connection = databases
    response = await call_next(request)
    return response
