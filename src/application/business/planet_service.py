from src.application.repository import PlanetRepository
from src.application.business.aparition_service import get_planet_apparition_counter
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
        planet.apparition_counter = get_planet_apparition_counter(planet.name)

        return planet

    def get_planets(self) -> list:
        logger.debug(f"[PLANET SERVICE] Getting all registered planets")

        planets = self.__planet_repo.get_all_planets()

        for planet in planets:
            planet.apparition_counter = get_planet_apparition_counter(planet.name)

        return planets

    def get_planet_by_id(self, planet_id: str) -> Planet:
        logger.debug(f"[PLANET SERVICE] Getting planet with id {planet_id}")
        planet = self.__planet_repo.get_planet_by_id(planet_id)

        if planet is None:
            raise ObjectNotFoundError(f"Name {planet_id}")

        planet.apparition_counter = get_planet_apparition_counter(planet.name)

        return planet

    def get_planet_by_name(self, planet_name: str) -> Planet:
        logger.debug(f"[PLANET SERVICE] Getting planet with name {planet_name}")
        planet = self.__planet_repo.get_planet_by_name(planet_name)

        if planet is None:
            raise ObjectNotFoundError(f"Name {planet_name}")

        planet.apparition_counter = get_planet_apparition_counter(planet.name)

        return planet

    def delete_planet_by_id(self, planet_id: str) -> None:
        logger.debug(f"[PLANET SERVICE] Deleting planet with id {planet_id}")
        planet = self.__planet_repo.get_planet_by_id(planet_id)

        if planet is None:
            raise ObjectNotFoundError(f"ID {planet_id}")

        self.__planet_repo.delete_planet(planet_id)
