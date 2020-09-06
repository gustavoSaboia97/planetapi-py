from fastapi import APIRouter, status
from .components.url_builder import UrlBuilder
from src.application.models.api import Planet
from src.application.controllers import PlanetController

planet_router = APIRouter()
url_builder = UrlBuilder()

controller = PlanetController()


@planet_router.post(url_builder.planet_uri, status_code=status.HTTP_201_CREATED)
def add_planet(planet: Planet) -> dict:
    return controller.add_planet(planet)


@planet_router.get(url_builder.planet_uri, status_code=status.HTTP_200_OK)
def get_planets() -> list:
    return controller.get_planets()


@planet_router.get(url_builder.planet_by_id_uri, status_code=status.HTTP_200_OK)
def get_planet_by_id(planet_id: str) -> dict:
    return controller.get_planet_by_id(planet_id)


@planet_router.get(url_builder.planet_by_name_uri, status_code=status.HTTP_200_OK)
def get_planet_by_name(planet_name: str) -> dict:
    return controller.get_planet_by_name(planet_name)


@planet_router.delete(url_builder.planet_by_id_uri, status_code=status.HTTP_204_NO_CONTENT)
def delete_planets(planet_id: str) -> str:
    return controller.delete_planet(planet_id)
