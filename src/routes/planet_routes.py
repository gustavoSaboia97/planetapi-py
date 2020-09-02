from fastapi import APIRouter
from .components.url_builder import UrlBuilder


planet_router = APIRouter()
url_builder = UrlBuilder()


@planet_router.get(url_builder.planet_uri)
def get_planets():
    return []

