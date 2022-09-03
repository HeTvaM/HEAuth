import psycopg2

from tools.patterns import MetaSingleton

from .query import *

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

        self.create_tables(0)
        self.create_tables(1)

        logger.log(f"Вы подключены к - {record}")

    def create_tables(self, tablename):
        try:
            if tablename:
                self.__cursor.execute(CREATE_DB_TABLE)
            self.__cursor.execute(CREATE_DB_CLOSE_TABLE)
        except psycopg2.errors.DuplicateTable:
            pass

    def add(self, table_id, data):
        logger.log(f"ADD DATA - {data}")

        query = f"""
        INSERT INTO {table} ({', '.join([key for key in data.keys()])})
        VALUES ({', '.join([f'{{{i}}}' for i in range(len(data))])})
        """

        logger.log(f"ADD QUERY - {query}")

        self.__cursor.execute(
            query.format(
                *[value for value in data.values()]
            )
        )

        self.__cursor.execute(
            GET_LAST_ID.format("open")
        )

        return self.__cursor.fetchone()[0]


    def add_open(self, data):
        self.__cursor.execute(
            OPEN_INSERT_BLOCK.format(
                data["login"],
                data["timestamp"],
                data["ip"],
                data["status"]
            )
        )

        self.__cursor.execute(
            GET_LAST_ID.format("open")
        )

        return self.__cursor.fetchone()[0]

    def add_close(self, data):
        self.__cursor.execute(
            CLOSE_INSERT_BLOCK.format(
                data["login"],
                data["ip"],
                data["open_data"],
                data["close_data"],
                data["actions"]
            )
        )

        self.__cursor.execute(
            GET_LAST_ID.format("close")
        )

        return self.__cursor.fetchone()[0]

    def delete_block(self, table, id):
        self.__cursor.execute(
            DELETE_BLOCK.format(table, id)
        )
        return True

    def get_table(self, table):
        self.__cursor.execute(
            SELECT_ALL.format(table)
        )
        return self.__cursor.fetchall()

    def get_last_block(self, table):
        self.__cursor.execute(
            GET_LAST_ID.format(table)
        )
        return self.__cursor.fetchone()

    def search_by_id(self, table, id):
        self.__cursor.execute(
             SEARCH_BY_ID.format(table, id)
        )
        return self.__cursor.fetchone()

    def reset(self, table):
        self.__cursor.execute(
            DELETE_ALL.format(table)
        )
        self.__cursor.execute(
            RESET_PRIMARY_KEY.format(table)
        )
        return True

    def close_connection(self):
        self.__cursor.close()
        self.conn.close()
