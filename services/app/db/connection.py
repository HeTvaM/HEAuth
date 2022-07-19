from pymongo import MongoClient
from bson.objectid import ObjectId


class Connection:

    def __init__(self, connection_data, db_name, open_table, super_table):
        self._tables = {open_table: MongoClient(connection_data)[db_name][open_table],
                        super_table: MongoClient(connection_data)[db_name][super_table]}
        pass

    async def add_block(self, table_name, block):
        self._tables[table_name].insert_one(block)
        pass

    async def delete_block(self, table_name, block_id):
        block = await self.search_by_id(table_name, block_id)
        self._tables[table_name].delete_one(block)
        pass

    async def show_table(self, table_name):
        return self._tables[table_name].find()

    async def get_last_block(self, table_name):
        return self._tables[table_name].find().sort('_id', -1)[0]

    async def search_by_id(self, table_name, block_id):
        return self._tables[table_name].find_one(ObjectId(block_id))

    # return True if block with token not found

    async def verify(self, token):
        block = self._tables['open'].find_one({'token': {"$eq": token}})
        return True if block is None else False

    pass
