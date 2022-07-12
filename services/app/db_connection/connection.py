from pymongo import MongoClient


class Connection:

    def __init__(self, connection_data, db_name, open_table, super_table):
        self.open_table = Table(connection_data, db_name, open_table)
        self.__super_table = Table(connection_data, db_name, super_table)
        pass

    def add_super_block(self, super_block):
        # delete block from open table self.open_table.delete_block()
        self.__super_table.add_block(super_block)
        pass

    pass


class Table:

    def __init__(self, connection_data, db_name, table_name):
        self.__table = MongoClient(connection_data)[db_name][table_name]
        pass

    def add_block(self, block):
        self.__table.insert_one(block)
        pass

    def delete_block(self, block):
        self.__table.delete_one(block)
        pass

    def show_table(self):
        return self.__table.find()

    def get_last_block(self):
        return self.__table.find().sort('_id', -1)[0]

    pass
