from src.config.mongo_config import MongoConfig
from src.application.models.api import Planet
from pymongo.collection import ObjectId


class PlanetRepository:

    def __init__(self):
        self.__mongo_configuration = MongoConfig()
        self.__database = self.__mongo_configuration.database
        self.__planet_collection = self.__database.planet_collection
        self.__planet_collection.create_index("name", unique=True)

    def add_new_planet(self, planet: Planet) -> Planet:
        inserted_planet = self.__planet_collection.insert_one(planet.to_mongo_dict())
        planet.id = str(inserted_planet.inserted_id)
        return planet

    def get_all_planets(self) -> list:
        planets = list()

        for document in self.__planet_collection.find():
            planet = Planet(
                id=str(document['_id']),
                name=str(document['name']),
                terrain=str(document['terrain']),
                climate=str(document['climate'])
            )

            planets.append(planet)

        return planets

    def get_planet_by_id(self, planet_id: str) -> Planet:
        find_query = {"_id": ObjectId(planet_id)}

        planet = None

        for document in self.__planet_collection.find(find_query):
            planet = Planet(
                id=str(document['_id']),
                name=str(document['name']),
                terrain=str(document['terrain']),
                climate=str(document['climate'])
            )

        return planet

    def get_planet_by_name(self, planet_name: str) -> Planet:
        find_query = {"name": planet_name}

        planet = None

        for document in self.__planet_collection.find(find_query):
            planet = Planet(
                id=str(document['_id']),
                name=str(document['name']),
                terrain=str(document['terrain']),
                climate=str(document['climate'])
            )

        return planet

    def delete_planet(self, planet_id: str) -> None:
        delete_query = {"_id": ObjectId(planet_id)}
        self.__planet_collection.delete_one(delete_query)
