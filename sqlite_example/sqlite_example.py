"""Another example of a sqlite workflow you might find useful for SC 2"""
import sqlite3
import pandas


def create_table(conn):
    curs = conn.cursor()
    create_statement = """
      CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name CHAR(20),
        favorite_color CHAR(20),
        least_favorite_color CHAR(20)
      );
    """
    curs.execute(create_statement)
    curs.close()
    conn.commit()


def insert_data(conn):
    curs = conn.cursor()
    my_data = [
        ("George", "blue", "blue"),
        ("Samantha", "yellow", "orange"),
        ("Craig", "green", "black")
    ]

    for person in my_data:
        insert_statement = """
          INSERT INTO students (name, favorite_color, least_favorite_color)
          VALUES (
            {},
            {},
            {}
          ); 
        """.format(person[0], person[1], person[2])
        curs.execute(insert_statement)

    curs.close()
    conn.commit()


if __name__ == "__main__":
    # Create Connection to our database
    conn = sqlite3.connect("example_db.sqlite3")
    create_table(conn)
    insert_data(conn)
