from bson.objectid import ObjectId
from pymongo import MongoClient
from pymongo.errors import OperationFailure, PyMongoError

def check_failure(func):
    def wrapper(*args, **kwargs):
        try:
            res = func(args, kwargs)
        except (AutoReconnect, ConnectionFailure) as e:
            return e, False

        return res, True


class Connection:
    OPEN_TABLE_NAME  = "open"
    CLOSE_TABLE_NAME = "close"

    def __init__(self, connection_data, db_name):
        self._tables = {
             self.OPEN_TABLE_NAME: MongoClient(
                  connection_data
             )[db_name][self.OPEN_TABLE_NAME]

             #self.CLOSE_TABLE_NAME: MongoClient(
             #     connection_data
             #)[db_name][self.CLOSE_TABLE_NAME]
        }

    async def add(self, table_name, block):
        created_block = self._tables[table_name].insert_one(block)
        return created_block.inserted_id

    async def delete(self, table_name, block_id):
        block = await self.search_by_id(table_name, block_id)
        self._tables[table_name].delete_one(block)

    async def show_table(self, table_name):
        return self._tables[table_name].find()

    async def get_last_block(self, table_name):
        return self._tables[table_name].find().sort('_id', -1)[0]

    async def search_by_id(self, table_name, block_id):
        return self._tables[table_name].find_one(ObjectId(block_id))

    async def verify(self, token):
        block = self._tables['open'].find_one({'token': {"$eq": token}})
        return not block is None

    pass
