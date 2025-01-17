from src.config.env_config import SWAPI_URI
from src.cache import get_requester_one_day_cache


def get_planet_apparition_counter(planet_name: str) -> int:
    final_uri = get_final_uri(planet_name)
    requests = get_requester_one_day_cache()
    response = requests.get(final_uri)
    return get_apparitions(response.json())


def get_final_uri(planet_name: str) -> str:
    return f"{SWAPI_URI}?search={planet_name}"


def get_apparitions(planet_json: dict) -> int:
    results = planet_json["results"]

    if len(results) == 0:
        return 0

    planet = results[0]
    return len(planet['films'])
