from src.application.repository import PlanetRepository
from src.application.models.api import Planet
from src.error import ObjectAlreadyExistsError, ObjectNotFoundError
from src.util.logger import get_logger

logger = get_logger()


class PlanetService:

    def __init__(self):
        self.__planet_repo = PlanetRepository()

    def create_planet(self, planet: Planet) -> Planet:
        logger.debug(f"[PLANET SERVICE] Validating existence of planet {planet.name}")
        existent_planet = self.__planet_repo.get_planet_by_name(planet.name)

        if existent_planet is not None:
            raise ObjectAlreadyExistsError(planet.name)

        logger.debug(f"[PLANET SERVICE] Identified new planet {planet.name}")
        logger.debug(f"[PLANET SERVICE] Registering it {planet.name}")
        planet = self.__planet_repo.add_new_planet(planet)

        return planet

    def get_planets(self) -> list:
        logger.debug(f"[PLANET SERVICE] Getting all registered planets")
        return self.__planet_repo.get_all_planets()

    def get_planet_by_id(self, planet_id: str) -> Planet:
        logger.debug(f"[PLANET SERVICE] Getting planet with id {planet_id}")
        planet = self.__planet_repo.get_planet_by_id(planet_id)

        if planet is None:
            raise ObjectNotFoundError(f"Name {planet_id}")

        return planet

    def get_planet_by_name(self, planet_name: str) -> Planet:
        logger.debug(f"[PLANET SERVICE] Getting planet with name {planet_name}")
        planet = self.__planet_repo.get_planet_by_name(planet_name)

        if planet is None:
            raise ObjectNotFoundError(f"Name {planet_name}")

        return planet

    def delete_planet_by_id(self, planet_id: str) -> None:
        logger.debug(f"[PLANET SERVICE] Deleting planet with id {planet_id}")
        planet = self.__planet_repo.get_planet_by_id(planet_id)

        if planet is None:
            raise ObjectNotFoundError(f"ID {planet_id}")

        self.__planet_repo.delete_planet(planet_id)
