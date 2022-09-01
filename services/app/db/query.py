CREATE_DB_TABLE = """CREATE TABLE open
                   (id serial PRIMARY KEY NOT NULL,
                   login character(20),
                   date timestamp without time zone,
                   ip inet,
                   status character(20));"""

SELECT_ALL = "SELECT * FROM open"
OPEN_INSERT_BLOCK = "INSERT INTO open (login, date, ip, status) VALUES (%s, %s, %s, %s)"
SEARCH_BY_ID = "SELECT * FROM open WHERE id = {id}"
DELETE_BLOCK = "DELETE FROM open WHERE id = %s"
GET_LAST_ID = "SELECT * FROM open WHERE id = (SELECT MAX(id) FROM open)"
