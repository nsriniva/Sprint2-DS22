"""Basic SQLite to PostGreSQL Data Pipeline"""

import sqlite3
import psycopg2
from queries import *


# Connecting to PostGreSQL DB
dbname = "?"
user = "?"
password = "?"
host = "?"

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
pg_curs = pg_conn.cursor()


# Connecting to Sqlite DB
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()


# Pipeline functions
def execute_query(curs, query=SELECT_ALL):
    result = curs.execute(query)
    return result


def populate_pg_character_table(pg_curs, characters_list):
    for character in characters_list:
        # character = (1, 'Aliquid iste optio reiciendi', 0, 0, 10, 1, 1, 1, 1)
        insert_statement = """
          INSERT INTO charactercreator_character
          (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
          VALUES {};
        """.format(character[1:])
        pg_curs.execute(insert_statement)
    pg_conn.commit()


if __name__ == "__main__":
    execute_query(pg_curs, CREATE_CHARACTER_TABLE)
    get_characters = execute_query(sl_curs, GET_CHARACTERS).fetchall()
    populate_pg_character_table(pg_curs, get_characters)
