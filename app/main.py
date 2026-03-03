from fastapi import FastAPI
from app.api.user_routes import router as user_router
from app.api.aircraft_routes import router as aircraft_router
from app.api.flight_routes import router as flight_router
from app.api.mission_routes import router as mission_router
from app.api.pilot_routes import router as pilot_router
from app.api.telemetric_routes import router as telemetric_router
from app.core.database import SQLModel, engine

app = FastAPI()

app.include_router(user_router)
app.include_router(aircraft_router)
app.include_router(flight_router)
app.include_router(mission_router)
app.include_router(pilot_router)
app.include_router(telemetric_router)


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)