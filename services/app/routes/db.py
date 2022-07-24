"""
Example DB for test features
"""

from tools.debug_logger import Logger
from tools.patterns import MetaSingleton

logger = Logger()

class DB(metaclass = MetaSingleton):
    def __init__(self):
        self.dbs = [{}, {}]

    def add(self, block, db:int=0):
        print(db, block)
        id = len(self.dbs[db]) + 1
        self.dbs[db][id] = block

        logger.log(f"Success ADD")

        return id

    def delete(self, id, db=0):
        logger.log(f"DELETE \ ID: {id},  DB: {db}")

        try:
            block = self.dbs.pop(id)
        except KeyError as e:
            logger.log_exception(f"DELETE: {e}")
            return False

        logger.log("Success DELETE")

        return block

    def get_last_block(self, db=0):
        logger.log(f"GET_LAST_BLOCK \ DB: {db}")

        id = len(self.dbs[db])
        block = self.dbs[db].get(id)

        logger.log("Success GET_LAST_BLOCK")

        return block


    def print(self, db=0):
        logger.log("PRINT TABLE \ DB: {db}")

        for num, value in enumerate(self.dbs[db].values()):
            logger.log(f"ID: {num} BLOCK: {value.dict()}")

        return True
