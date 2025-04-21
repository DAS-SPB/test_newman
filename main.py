from fastapi import FastAPI
from endpoints import create_user, get_user

PREFIX = "/simple_app"

simple_app = FastAPI()

simple_app.include_router(router=create_user.router, prefix=PREFIX)
simple_app.include_router(router=get_user.router, prefix=PREFIX)


@simple_app.get("/simple_app/health")
def healthcheck():
    return {"status": "OK"}
