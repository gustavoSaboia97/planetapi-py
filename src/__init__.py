from src.main import app
from src.routes.planet_routes import planet_router


app.include_router(planet_router)

