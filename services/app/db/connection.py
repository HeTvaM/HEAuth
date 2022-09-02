import psycopg2

from tools.patterns import MetaSingleton

from .query import (
    VERSION,
    CREATE_DB_TABLE,
    GET_LAST_ID,
    SELECT_ALL,
    OPEN_INSERT_BLOCK,
    SEARCH_BY_ID,
    DELETE_BLOCK,
    DELETE_ALL,
    RESET_PRIMARY_KEY
)

from tools.debug_logger import Logger
from tools.config import (
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT
)

logger = Logger()

class Connection(metaclass = MetaSingleton):
    def __init__(self):
        self.conn = psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        self.conn.autocommit = True
        self.__cursor = self.conn.cursor()
        self.__cursor.execute(VERSION)
        record = self.__cursor.fetchone()

        try:
            self.__cursor.execute(CREATE_DB_TABLE)
        except psycopg2.errors.DuplicateTable:
            pass

        logger.log(f"Вы подключены к - {record}")

    def add(self, data):
        logger.log(f"ADD DB DATA: {data}")

        self.__cursor.execute(
            OPEN_INSERT_BLOCK, (
                data["login"],
                data["timestamp"],
                data["ip"],
                data["status"]
            )
        )

        self.__cursor.execute(
            GET_LAST_ID
        )

        return self.__cursor.fetchone()[0]

    def delete_block(self, id):
        self.__cursor.execute(
            DELETE_BLOCK, (id)
        )
        return True

    def get_table(self):
        self.__cursor.execute(SELECT_ALL)
        return self.__cursor.fetchall()

    def get_last_block(self):
        self.__cursor.execute(GET_LAST_ID)
        return self.__cursor.fetchone()

    def search_by_id(self, id):
        self.__cursor.execute(
             SEARCH_BY_ID, (id)
        )
        return self.__cursor.fetchone()

    def reset(self):
        self.__cursor.execute(DELETE_ALL)
        self.__cursor.execute(RESET_PRIMARY_KEY)
        return True

    def close_connection(self):
        self.__cursor.close()
        self.conn.close()
