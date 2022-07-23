import psycopg2


select_all_query = 'SELECT * FROM {table_name}'

open_table_insert_query = 'INSERT INTO {table_name} (Login, Date, IP, STATUS) VALUES ({login}, {date}, {ip}, {status})'

search_by_id_query = 'SELECT * FROM {table_name} WHERE id = {id}'

delete_block_query = 'DELETE FROM {table_name} WHERE id = {id}'


class Connection:

    def __init__(self, dbname, user, password, host, port):
        conn = psycopg2.connect(database=dbname, user=user, password=password, host=host, port=port)
        conn.autocommit = True
        self._cursor = conn.cursor()
        self._cursor.execute("SELECT version();")
        record = self._cursor.fetchone()
        print("Вы подключены к - ", record, "\n")
        pass

    # return id of block

    async def add_block(self, table_name, block):
        self._cursor.execute(open_table_insert_query.format(
            table_name=table_name, login=block.login, date=block.date, ip=block.ip, status=block.status))
        block_id = self._cursor.fetchone()[0]
        return block_id

    async def delete_block(self, table_name, block_id):
        self._cursor.execute(delete_block_query.format(table_name=table_name, id=block_id))
        pass

    async def show_table(self, table_name):
        self._cursor.execute(select_all_query.format(table_name=table_name))
        return self._cursor.fetcall()

    async def get_last_block(self, table_name):
        self._cursor.execute(select_all_query.format(table_name=table_name))
        return self._cursor.fetchone()[0]

    async def search_by_id(self, table_name, block_id):
        self._cursor.execute(search_by_id_query.format(table_name=table_name, id=block_id))
        return self._cursor.fetchone()

    # return True if block with token not found

    async def verify_all_table(self, token):
        pass

    pass
