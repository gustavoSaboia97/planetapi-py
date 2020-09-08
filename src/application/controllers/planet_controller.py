from src.application.business import PlanetService
from src.application.models.api import Planet
from src.util.logger import get_logger

logger = get_logger()


class PlanetController:

    def __init__(self):
        self.__service = PlanetService()

    def add_planet(self, planet: Planet) -> dict:
        logger.info(f"[PLANET CONTROLLER] Received data to create new Planet {planet.name}")
        planet = self.__service.create_planet(planet)
        return planet.to_dict()

    def get_planets(self) -> list:
        logger.info(f"[PLANET CONTROLLER] Getting all registered planets")
        return self.__service.get_planets()

    def get_planet_by_id(self, planet_id: str) -> dict:
        logger.info(f"[PLANET CONTROLLER] Getting planet by it's id {planet_id}")
        planet = self.__service.get_planet_by_id(planet_id)
        return planet.to_dict()

    def get_planet_by_name(self, planet_name: str) -> dict:
        logger.info(f"[PLANET CONTROLLER] Getting planet by it's name {planet_name}")
        planet = self.__service.get_planet_by_name(planet_name)
        return planet.to_dict()

    def delete_planet(self, planet_id: str) -> None:
        logger.info(f"[PLANET CONTROLLER] Deleting planet by id {planet_id}")
        self.__service.delete_planet_by_id(planet_id)
