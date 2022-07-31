import psycopg2

from tools.debug_logger import Logger

from query import {
    SELECT_ALL,
    OPEN_INSERT_BLOCK,
    SEARCH_BY_ID,
    DELETE_BLOCK
}

from tools.config import (
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT
)

logger = Logger()

class Connection:
    def __init__(self):
        conn = psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.autocommit = True
        self.__cursor = conn.cursor().execute("SELECT version();")
        record = self.__cursor.fetchone()

        logger.log(f"Вы подключены к - {record}")

    def add(self, data):
        self.__cursor.execute(
            open_table_insert_query.format(
                table_name="open",
                status=data["status"]
                login=data["login"],
                date=data["date"],
                ip=data["ip"]
            )
        )

        return self.__cursor.fetchone()[0]

    def delete_block(self, id, table_name="open"):
        self.__cursor.execute(
            delete_block_query.format(
                table_name=table_name, id=id
            )
        )
        return True

    def get_table(self, table_name="open")):
        self.__cursor.execute(
            select_all_query.format(table_name=table_name)
        )
        return self.__cursor.fetcall()

    def get_last_block(self, table_name="open")):
        self.__cursor.execute(
            select_all_query.format(table_name=table_name)
        )
        return self.__cursor.fetchone()[0]

    def search_by_id(self, id, table_name="open")):
        self.__cursor.execute(
             search_by_id_query.format(
                 table_name=table_name, id=id
            )
        )
        return self.__cursor.fetchone()
