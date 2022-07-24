import psycopg2

from tools.debug_logger import Logger

from query import {
    SELECT_ALL,
    OPEN_INSERT_BLOCK,
    SEARCH_BY_ID,
    DELETE_BLOCK
}

logger = Logger()

class Connection:
    name = os.getenv(DB_NAME, "Blocks")
    user = os.getenv(DB_USER, "blocks")
    password = os.getenv(DB_PASSWORD, "12345")
    host = os.getenv(HOST,"127.0.0.1")
    port = os.getenv(PORT,"5432")

    def __init__(self):
        conn = psycopg2.connect(
            database=self.name, user=self.user, password=self.password,
            host=self.host, port=self.port
        )
        conn.autocommit = True
        self.__cursor = conn.cursor().execute("SELECT version();")
        record = self.__cursor.fetchone()

        logger.log(f"Вы подключены к - {record}")

    def add(self, table_name, block):
        self.__cursor.execute(
            open_table_insert_query.format(
                table_name=table_name, login=block.login, date=block.date,
                ip=block.ip, status=block.status
            )
        )

        id = self.__cursor.fetchone()[0]
        return id

    def delete_block(self, table_name, id):
        self.__cursor.execute(
            delete_block_query.format(
                table_name=table_name, id=id
            )
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
