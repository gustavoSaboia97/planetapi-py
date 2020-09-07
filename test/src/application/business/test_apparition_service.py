import unittest
from unittest.mock import patch, MagicMock
from src.application.business.apparition_service import get_planet_apparition_counter

json_response = {
    "results": [
        {
            "name": "Tatooine",
            "films": [
                "http://swapi.dev/api/films/1/",
                "http://swapi.dev/api/films/3/",
                "http://swapi.dev/api/films/4/",
                "http://swapi.dev/api/films/5/",
                "http://swapi.dev/api/films/6/"
            ]
        }
    ]
}


class TestApparitionService(unittest.TestCase):

    @patch('src.application.business.apparition_service.get_requester_one_day_cache')
    def test_should_get_apparitions_on_swapi(self, requests_mock) -> None:
        planet_name = "Tatooine"

        response = MagicMock()

        requests_mock_cached = requests_mock.return_value
        requests_mock_cached.get.return_value = response
        response.json.return_value = json_response

        response = get_planet_apparition_counter(planet_name)

        requests_mock_cached.get.assert_called()
        self.assertEqual(5, response, "Wrong apparition quantity")


if __name__ == "__main__":
    unittest.main()
