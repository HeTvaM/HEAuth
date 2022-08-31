import psycopg2

from tools.patterns import MetaSingleton

from .query import (
    CREATE_DB_TABLE,
    GET_LAST_ID,
    SELECT_ALL,
    OPEN_INSERT_BLOCK,
    SEARCH_BY_ID,
    DELETE_BLOCK
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
        conn = psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.autocommit = True
        self.__cursor = conn.cursor()
        self.__cursor.execute("SELECT version();")
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
                table_name = "open",
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

    def delete_block(self, id, table_name="open"):
        self.__cursor.execute(
            DELETE_BLOCK.format(
                table_name=table_name, id=id
            )
        )
        return True

    def get_table(self, table_name="open"):
        self.__cursor.execute(
            SELECT_ALL.format(table_name=table_name)
        )
        return self.__cursor.fetcall()

    def get_last_block(self, table_name="open"):
        self.__cursor.execute(
            SELECT_ALL.format(table_name=table_name)
        )
        return self.__cursor.fetchone()[0]

    def search_by_id(self, id, table_name="open"):
        self.__cursor.execute(
             SEARCH_BY_ID.format(
                 table_name=table_name, id=id
            )
        )
        return self.__cursor.fetchone()
