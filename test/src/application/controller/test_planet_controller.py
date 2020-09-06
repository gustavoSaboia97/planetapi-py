import unittest

from unittest.mock import patch

from src.application.controllers.planet_controller import PlanetController
from src.application.models.api.planet import Planet


class TestPlanetController(unittest.TestCase):

    @patch('src.application.controllers.planet_controller.PlanetService')
    def setUp(self, planet_service_mock) -> None:
        self.__planet_service = planet_service_mock.return_value
        self.__planet_controller = PlanetController()

    def test_should_add_new_planet(self) -> None:
        planet = Planet(name="Tatooine", terrain="Arid", climate="Desert")
        expected_planet = Planet(id="5c7c0c22fd8a2f36f6cdea65", name="Tatooine", terrain="Arid", climate="Desert")

        self.__planet_service.create_planet.return_value = expected_planet

        response = self.__planet_controller.add_planet(planet)

        self.__planet_service.create_planet.assert_called_with(planet)
        self.assertEqual(expected_planet, response, "Planet response not valid")

    def test_should_get_all_planets(self) -> None:
        planet = Planet(name="Tatooine", terrain="Arid", climate="Desert")
        expected_planets = [planet]

        self.__planet_service.get_planets.return_value = expected_planets

        response = self.__planet_controller.get_planets()

        self.__planet_service.get_planets.assert_called_with()
        self.assertEqual(expected_planets, response, "Planet list response not valid")

    def test_should_get_planet_by_id(self) -> None:
        planet_id = "5c7c0c22fd8a2f36f6cdea65"
        expected_planet = Planet(id="5c7c0c22fd8a2f36f6cdea65", name="Tatooine", terrain="Arid", climate="Desert")

        self.__planet_service.get_planet_by_id.return_value = expected_planet

        response = self.__planet_controller.get_planet_by_id(planet_id)

        self.__planet_service.get_planet_by_id.assert_called_with(planet_id)
        self.assertEqual(expected_planet, response, "Planet response not valid")

    def test_should_get_planet_by_name(self) -> None:
        planet_name = "Tatooine"
        expected_planet = Planet(id="5c7c0c22fd8a2f36f6cdea65", name="Tatooine", terrain="Arid", climate="Desert")

        self.__planet_service.get_planet_by_name.return_value = expected_planet

        response = self.__planet_controller.get_planet_by_name(planet_name)

        self.__planet_service.get_planet_by_name.assert_called_with(planet_name)
        self.assertEqual(expected_planet, response, "Planet response not valid")

    def test_should_delete_planet_by_id(self) -> None:
        planet_id = "5c7c0c22fd8a2f36f6cdea65"

        self.__planet_controller.delete_planet(planet_id)

        self.__planet_service.delete_planet_by_id.assert_called_with(planet_id)


if __name__ == "__main__":
    unittest.main()
