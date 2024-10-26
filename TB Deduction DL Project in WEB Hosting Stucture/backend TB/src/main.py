from fastapi import FastAPI, status, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException


from .api_router import router

from .database import database
from typing import *




# Define application
app = FastAPI(
    title="TB Dedection using DL CNN APP",
    description="TB Dedection By Jai CCP app",
    version="0.1",
)

app.include_router(router)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )


@app.get("/")
def index():
    
    return {"message": "Welcome to Jai CCP app"}


@app.on_event("startup")
async def startup() -> None:
    

    await database.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    
    await database.disconnect()


@app.get("/healthcheck", include_in_schema=False)
async def healthcheck() -> Dict[str, str]:
    return {"status": "ok"}
