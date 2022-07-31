import os
import psycopg2

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

user_query = 'CREATE USER {username} WITH PASSWORD {password}'
db_query = 'CREATE DATABASE {database_name}'
create_open_table_query = 'CREATE TABLE {table_name} (ID INT PRIMARY KEY NOT NULL,' \
                          ' Login CHARACTER VARYING(40),' \
                          ' Date TIMESTAMP,' \
                          'IP INET, ' \
                          'STATUS CHARACTER VARYING(120));'


NAME=os.environ["DB_NAME"]
USER=os.environ["DB_USER"]
PASSWORD=os.environ["DB_PASSWORD"]
HOST=os.environ["DB_HOST"]
PORT=os.environ["DB_PORT"]
FIRST_TABLE_NAME=os.environ["DB_FIRST_TABLE"]


def set_settings():
    with psycopg2.connect(
        database=NAME,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    ) as conn:
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        conn.cursor().execute(
            db_query.format(database_name=NAME)
        )

    with psycopg2.connect(
        database=NAME,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    ) as conn:
        conn.cursor().execute(
            create_open_table_query.format(
                table_name=FIRST_TABLE_NAME
            )
        )
        conn.commit()


if __name__=="__main__":
    set_settings()
