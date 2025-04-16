from fastapi import FastAPI
from contextlib import asynccontextmanager
from routers.rout_api import router_get
from rep_db.database import create_tables, delete_tables



@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База создана")
    yield
    print("Выключение")

app = FastAPI(lifespan=lifespan)
app.include_router(router_get)