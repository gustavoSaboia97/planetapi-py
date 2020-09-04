from fastapi import APIRouter, status
from .components.url_builder import UrlBuilder
from src.application.models.api import Planet


planet_router = APIRouter()
url_builder = UrlBuilder()


@planet_router.post(url_builder.planet_uri, status_code=status.HTTP_201_CREATED)
def add_planet(planet: Planet) -> dict:
    return {}


@planet_router.get(url_builder.planet_uri, status_code=status.HTTP_200_OK)
def get_planets() -> list:
    return []


@planet_router.get(url_builder.planet_uri + "/{planet_id}", status_code=status.HTTP_200_OK)
def get_planet(planet_id: str) -> dict:
    return {}


@planet_router.get(url_builder.planet_uri, status_code=status.HTTP_200_OK)
def get_planet(planet_name: str) -> dict:
    return {}


@planet_router.get(url_builder.planet_uri, status_code=status.HTTP_204_NO_CONTENT)
def delete_planets():
    return None

