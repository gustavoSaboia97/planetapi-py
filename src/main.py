from fastapi import FastAPI
from src.routes.planet_routes import planet_router

app = FastAPI()

app.include_router(planet_router)
