#___CREATE____
CREATE_DB_TABLE = """CREATE TABLE open
                   (id serial PRIMARY KEY NOT NULL,
                   login character(20),
                   date timestamp without time zone,
                   ip inet,
                   status character(20));
                   """

CREATE_DB_CLOSE_TABLE = """CREATE TABLE close
                        (id serial PRIMARY KEY NOT NULL,
                        login character(20),
                        ip inet,
                        open_date timestamp without time zone,
                        close_date timestamp without time zone,
                        activity jsonb);
                        """

#___SELECT___
VERSION = "SELECT version();"
SELECT_ALL = "SELECT * FROM {0}"
SEARCH_BY_ID = "SELECT * FROM {0} WHERE id = {1}"
GET_LAST_ID = "SELECT * FROM {0} WHERE id = (SELECT MAX(id) FROM open)"

#___DELETE____
DELETE_BLOCK = "DELETE FROM {0} WHERE id = {1}"
DELETE_ALL = "TRUNCATE {0}"
RESET_PRIMARY_KEY = "ALTER SEQUENCE {0}_id_seq RESTART; \
                     UPDATE {0} SET id = DEFAULT;"

#___INSERT___
OPEN_BlOCK_DATA = "INSERT INTO open (login, date, ip, status) VALUES ({0}, {1}, {2}, {3})"
CLOSE_BLOCK_DATA = """INSERT INTO close (login, ip, open_date, close_date, activity)
                   VALUES ({0}, {1}, {2}, {3}, {4})
                   """
