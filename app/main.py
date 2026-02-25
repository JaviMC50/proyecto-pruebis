from fastapi import FastAPI
from app.api.user_routes import router
from app.core.database import SQLModel, engine

app = FastAPI()

app.include_router(router)

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)