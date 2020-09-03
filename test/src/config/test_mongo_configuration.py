import unittest

from pymongo.database import Database
from src.config.mongo_config import MongoConfig


class TestMongoConfiguration(unittest.TestCase):

    def setUp(self):
        self.__mongo_configuration = MongoConfig()

    def test_should_return_pymongo_database(self):
        self.assertEqual(Database, type(self.__mongo_configuration.database))


if __name__ == "__main__":
    unittest.main()
