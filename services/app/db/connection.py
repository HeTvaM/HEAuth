from pymongo import MongoClient
from bson.objectid import ObjectId


class Connection:

    """
        connection_data - string for connection to db, db_name - name of db,
     open_table - name of table, super_table - name of super table
    """

    def __init__(self, connection_data, db_name, open_table, super_table):
        self._tables = {open_table: MongoClient(connection_data)[db_name][open_table],
                        super_table: MongoClient(connection_data)[db_name][super_table]}
        pass

    # return id of block

    async def add_block(self, table_name, block):
        created_block = self._tables[table_name].insert_one(block)
        return created_block.inserted_id

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
