#___CREATE____
CREATE_DB_TABLE = """CREATE TABLE open
                   (id serial PRIMARY KEY NOT NULL,
                   login character(20),
                   date timestamp without time zone,
                   ip inet,
                   status character(20));"""

#___SELECT___
SELECT_ALL = "SELECT * FROM open"
SEARCH_BY_ID = "SELECT * FROM open WHERE id = {id}"
GET_LAST_ID = "SELECT * FROM open WHERE id = (SELECT MAX(id) FROM open)"

#___DELETE____
DELETE_BLOCK = "DELETE FROM open WHERE id = %s"
DELETE_ALL = "TRUNCATE open"
RESET_PRIMARY_KEY = "ALTER SEQUENCE open_id_seq RESTART; \
                     UPDATE open SET id = DEFAULT;"

#___INSERT___
OPEN_INSERT_BLOCK = "INSERT INTO open (login, date, ip, status) VALUES (%s, %s, %s, %s)"
