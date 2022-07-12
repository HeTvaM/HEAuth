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
    OPEN_TABLE_NAME="open"
    CLOSE_TABLE_NAME="close"

    def __init__(self, connection_data, db_name):
        self._open_table = Table(connection_data, db_name, self.OPEN_TABLE_NAME)
        self._close_table = Table(connection_data, db_name, self.CLOSE_TABLE_NAME)

    def close_table_add(self, super_block):
        self._close_table.add_block(super_block)


class Table:
    def __init__(self, connection_data, db_name, table_name):
        self._table = MongoClient(connection_data)[db_name][table_name]

    @check_failure
    def add_block(self, block):
        self._table.insert_one(block)

    @check_failure
    def del_block(self, block):
        self._table.delete_one(block)

    @check_failure
    def get_table(self):
        return self._table.find()

    @check_failure
    def get_last_block(self):
        return self._table.find().sort('_id', -1)[0]
