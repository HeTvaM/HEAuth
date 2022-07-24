import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

user_query = 'CREATE USER {username} WITH PASSWORD {password}'
db_query = 'CREATE DATABASE {database_name}'
create_open_table_query = 'CREATE TABLE {table_name} (ID INT PRIMARY KEY NOT NULL,' \
                          ' Login CHARACTER VARYING(40),' \
                          ' Date TIMESTAMP,' \
                          'IP INET, ' \
                          'STATUS CHARACTER VARYING(120));'

"""
    username - name for create new user of db, user_password - password for new user,
    db_name - name of created db, open, close - names of table
"""


def set_settings(username, user_password, db_name, open_table_name, close_table_name):
    conn = psycopg2.connect(database="postgres", user="postgres",
                            password="12345", host="127.0.0.1", port="5432")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    cursor.execute(db_query.format(database_name=db_name))
    conn.close()

    conn = psycopg2.connect(database=db_name, user="postgres",
                            password="12345", host="127.0.0.1", port="5432")
    cursor = conn.cursor()
    cursor.execute(create_open_table_query.format(table_name=open_table_name))
    conn.commit()
    conn.close()
    pass


if __name__=="__main__":
    set_settings(
        username="Danila",
        user_password="12345",
        db_name="blocks",
        names_tables=["open","super"]
    )
