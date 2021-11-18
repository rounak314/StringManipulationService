from pymongo import MongoClient
import configuration
import logging as logger


class StringManipulationStorage:
    def __init__(self):
        self.db = configuration.application_db
        self.collection = configuration.string_collection
        self.mongo_obj = MongoClient(configuration.mongo_uri)
        self.database = self.mongo_obj[configuration.application_db]

    def insert_data(self, data):
        try:
            logger.info(str(self.__module__))
            collection = self.database[configuration.string_collection]
            collection.insert_one(data)

        except Exception as ex:
            logger.error(str(ex))
            raise Exception(str(ex))

    def fetch_all_records(self):
        try:
            logger.info(str(self.__module__))
            collection = self.database[configuration.string_collection]
            result = list(collection.find())
            response = []
            if result:
                response = result

            return response

        except Exception as ex:
            logger.error(str(ex))
            raise Exception(str(ex))

    def fetch_record_by_id(self, record_id):
        try:
            logger.info(str(self.__module__))
            collection = self.database[configuration.string_collection]
            condition = {'id': record_id}
            result = collection.find(condition)

            response = {}
            if result:
                response = result[0]

            return response

        except Exception as ex:
            logger.error(str(ex))
            raise Exception(str(ex))

    def update_record_by_id(self, record_data):
        try:
            logger.info(str(self.__module__))
            collection = self.database[configuration.string_collection]
            condition = {'id': record_data.get('id', '')}
            collection.update_one(condition, {'$set': record_data})

        except Exception as ex:
            logger.error(str(ex))
            raise Exception(str(ex))