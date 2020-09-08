import unittest

from unittest.mock import patch

from src.application.business.planet_service import PlanetService
from src.application.models.api.planet import Planet

from src.error import ObjectAlreadyExistsError, ObjectNotFoundError


class TestPlanetService(unittest.TestCase):

    @patch('src.application.business.planet_service.PlanetRepository')
    def setUp(self, planet_repo_mock) -> None:
        self.__planet_repo = planet_repo_mock.return_value
        self.__planet_service = PlanetService()

    @patch('src.application.business.planet_service.get_planet_apparition_counter')
    def test_should_create_planet(self, apparition_getter_mock) -> None:
        planet = Planet(name="Tatooine", terrain="Arid", climate="Desert")
        expected_planet = Planet(id="5c7c0c22fd8a2f36f6cdea65", name="Tatooine", terrain="Arid", climate="Desert")
        apparition_counter = 5

        self.__planet_repo.get_planet_by_name.return_value = None
        self.__planet_repo.add_new_planet.return_value = expected_planet
        apparition_getter_mock.return_value = apparition_counter

        response = self.__planet_service.create_planet(planet)

        self.__planet_repo.get_planet_by_name.assert_called_with(planet.name)
        self.__planet_repo.add_new_planet.assert_called_with(planet)
        self.assertEqual(expected_planet, response, "Planet response not valid")

    def test_should_raise_planet_exists(self) -> None:
        planet = Planet(name="Tatooine", terrain="Arid", climate="Desert")
        expected_planet = Planet(id="5c7c0c22fd8a2f36f6cdea65", name="Tatooine", terrain="Arid", climate="Desert")

        self.__planet_repo.get_planet_by_name.return_value = expected_planet

        self.assertRaises(ObjectAlreadyExistsError, self.__planet_service.create_planet, planet)

    @patch('src.application.business.planet_service.get_planet_apparition_counter')
    def test_should_get_planets(self, apparition_getter_mock) -> None:
        planet = Planet(name="Tatooine", terrain="Arid", climate="Desert")
        expected_planets = [planet]
        apparition_counter = 5

        self.__planet_repo.get_all_planets.return_value = expected_planets
        apparition_getter_mock.return_value = apparition_counter

        response = self.__planet_service.get_planets()

        self.__planet_repo.get_all_planets.assert_called_with()
        self.assertEqual(expected_planets, response, "Planet list response not valid")

    @patch('src.application.business.planet_service.get_planet_apparition_counter')
    def test_should_get_planet_by_id(self, apparition_getter_mock) -> None:
        planet_id = "5c7c0c22fd8a2f36f6cdea65"
        expected_planet = Planet(id="5c7c0c22fd8a2f36f6cdea65", name="Tatooine", terrain="Arid", climate="Desert")
        apparition_counter = 5

        self.__planet_repo.get_planet_by_id.return_value = expected_planet
        apparition_getter_mock.return_value = apparition_counter

        response = self.__planet_service.get_planet_by_id(planet_id)

        self.__planet_repo.get_planet_by_id.assert_called_with(planet_id)
        self.assertEqual(expected_planet, response, "Planet by id response not valid")

    def test_should_raise_that_planet_with_refered_id_dont_exists(self) -> None:
        planet_id = "5c7c0c22fd8a2f36f6cdea65"
        expected_planet = None

        self.__planet_repo.get_planet_by_id.return_value = expected_planet

        self.assertRaises(ObjectNotFoundError, self.__planet_service.get_planet_by_id, planet_id)

    @patch('src.application.business.planet_service.get_planet_apparition_counter')
    def test_should_get_planet_by_name(self, apparition_getter_mock) -> None:
        planet_name = "Tatooine"
        expected_planet = Planet(id="5c7c0c22fd8a2f36f6cdea65", name="Tatooine", terrain="Arid", climate="Desert")
        apparition_counter = 5

        self.__planet_repo.get_planet_by_name.return_value = expected_planet
        apparition_getter_mock.return_value = apparition_counter

        response = self.__planet_service.get_planet_by_name(planet_name)

        self.__planet_repo.get_planet_by_name.assert_called_with(planet_name)
        self.assertEqual(expected_planet, response, "Planet by name response not valid")

    def test_should_raise_that_planet_with_refered_name_dont_exists(self) -> None:
        planet_name = "Tatooine"
        expected_planet = None

        self.__planet_repo.get_planet_by_name.return_value = expected_planet

        self.assertRaises(ObjectNotFoundError, self.__planet_service.get_planet_by_name, planet_name)

    def test_should_delete_planet_by_name(self) -> None:
        planet_id = "5c7c0c22fd8a2f36f6cdea65"

        self.__planet_service.delete_planet_by_id(planet_id)

        self.__planet_repo.delete_planet.assert_called_with(planet_id)


if __name__ == "__main__":
    unittest.main()
