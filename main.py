from fastapi import FastAPI

from contextlib import  asynccontextmanager

from db import create_tables, delete_tables
from router import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    await create_tables()
    print("on")
    yield
    print("off")

app = FastAPI(lifespan=lifespan)

app.include_router(task_router)
