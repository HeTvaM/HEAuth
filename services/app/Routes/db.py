"""
Example DB for test features
"""

import logging

class DB:
    def __init__(self):
        self.dbs = [{}, {}]

    def add(self, block, db=0):
        logging.info(f"ADD \ BLOCK: {block.login},  DB: {db}")
        id = len(self.dbs[db]) + 1
        self.dbs[db][id] = block
        logging.info(f"Success ADD")

        return id

    def delete(self, id, db=0):
        logging.info(f"DELETE \ ID: {id},  DB: {db}")
        try:
            block = self.dbs.pop(id)
        except KeyError as e:
            logging.error(f"DELETE: {e}")
            return False
        logging.info("Success DELETE")

        return block

    def get_last_block(self, db=0):
        logging.info(f"GET_LAST_BLOCK \ DB: {db}")
        id = len(self.dbs[db])
        block = self.dbs.get(id)
        logging.info("Success GET_LAST_BLOCK")

        return block


    def print(self, db=0):
        for key, value in self.dbs[db].items():
            print(f"ID: {id:<5} BLOCK: {value.dict():<40}")