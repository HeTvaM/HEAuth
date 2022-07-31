import os
import psycopg2

from tools.debug_logger import Logger

from .query import (
    SELECT_ALL,
    OPEN_INSERT_BLOCK,
    SEARCH_BY_ID,
    DELETE_BLOCK
)

logger = Logger()

def handler_for_exception(func):
    def wrapper(cls, db=None, *args, **kwargs):
        if not db == cls.cur_table and db:
            cls.cur_table = db

        try:
            res = func(cls,*args,**kwargs)
        except Exception as e:
            logger.log_exception(e)
            return None, False

        return res, True

class Connection:
    name=os.environ["DB_NAME"]
    user=os.environ["DB_USER"]
    password=os.environ["DB_PASSWORD"]
    host=os.environ["DB_HOST"]
    port=os.environ["DB_PORT"]

    def __init__(self):
        with psycopg2.connect( \
            database=self.name, 
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        ) as conn:
            conn.autocommit = True
            self.__cursor = conn.cursor().execute("SELECT version();")

        self.cur_table = "open"
        logger.log(f"Вы подключены к - {self.__cursor.fetchone()}")

    def add(self, table_name, block):
        self.__cursor.execute(
            open_table_insert_query.format(
                table_name=table_name,
                login=block.login,
                date=block.date,
                ip=block.ip,
                status=block.status
            )
        )

        id = self.__cursor.fetchone()[0]
        return id

    def delete_block(self, table_name, id):
        self.__cursor.execute(
            delete_block_query.format(table_name=table_name, id=id)
        )
        return True

    def get_table(self, table_name):
        self.__cursor.execute(
            select_all_query.format(table_name=table_name)
        )
        return self.__cursor.fetcall()

    def get_last_block(self, table_name):
        self.__cursor.execute(
            select_all_query.format(table_name=table_name)
        )
        return self.__cursor.fetchone()[0]

    def search_by_id(self, table_name, id):
        self.__cursor.execute(
             search_by_id_query.format(table_name=table_name, id=id)
        )
        return self.__cursor.fetchone()
