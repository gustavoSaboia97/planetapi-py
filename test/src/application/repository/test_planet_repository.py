import unittest

from unittest.mock import patch

from src.application.models.api import Planet
from src.application.repository.planet_repository import PlanetRepository


class TestPlanetRepository(unittest.TestCase):

    @patch('src.application.repository.planet_repository.MongoConfig')
    def setUp(self, mongo_config_mock) -> None:
        self.__mongo_config_instance = mongo_config_mock.return_value
        self.__database = mongo_config_mock.database
        self.__planet_repository = PlanetRepository()

    def test_should_add_new_planet(self) -> None:
        new_planet = Planet(
            name="Tatooine",
            terrain="Arid",
            climate="Desert"
        )

        self.__planet_repository.add_new_planet(new_planet)
        self.assertTrue(self.__mongo_config_instance.database.planet_collection.insert_one.called)

    def test_should_get_all_planets(self) -> None:
        self.__planet_repository.get_all_planets()
        self.assertTrue(self.__mongo_config_instance.database.planet_collection.find.called)

    def test_should_get_planet_by_id(self) -> None:
        self.__planet_repository.get_planet_by_id("5c7c0c22fd8a2f36f6cdea65")
        self.assertTrue(self.__mongo_config_instance.database.planet_collection.find.called)

    def test_should_get_planet_by_name(self) -> None:
        self.__planet_repository.get_planet_by_name("Tatooine")
        self.assertTrue(self.__mongo_config_instance.database.planet_collection.find.called)

    def test_should_delete_planet_by_id(self) -> None:
        self.__planet_repository.delete_planet("5c7c0c22fd8a2f36f6cdea65")
        self.assertTrue(self.__mongo_config_instance.database.planet_collection.delete_one.called)


if __name__ == "__main__":
    unittest.main()
