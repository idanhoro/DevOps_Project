from time import sleep
import os
import random
import mariadb


def start():
    """
    Run the random number generator.
    """
    conn = get_db_conn()
    cursor = get_cursor(conn)
    run = True

    while run:
        random_number = random.randint(0, 255)
        insert_entry(conn, cursor, random_number)
        sleep(60)

    conn.close()

def main():
    start()

def get_db_conn():
    """
    Creating the connection with the database,
    if it doesn't succeed it will throw an exception.

    :return conn : Connection to the database.
    """
    for i in range(1, 21):
        print(f"Attempt {i} to connect the database")
        try:
            return mariadb.connect(
                user=os.environ.get("DB_USER"),
                password=os.environ.get("DB_PASS"),
                host=os.environ.get("DB_HOST"),
                port=3306,
                database=os.environ.get("DB_NAME")
            )
        except mariadb.Error as e:
            print(f'Could not connect to MariaDB on {os.environ.get("DB_USER")}@{os.environ.get("DB_HOST")}')
            sleep(3)
    exit(1)

def get_cursor(conn):
    """
    Create the cursor that will exec by the connection.

    :param conn: The connection opened at the function get_db_conn().
    :return cursor:
    """
    return conn.cursor()

def insert_entry(conn, cursor, num: int):
    """
    Insert random numbers into the SQL's table at the specific column.

    :param conn: The connection opened at the function get_db_conn().
    :param cursor: Execute commands wrapped by the connection .
    :param num: The random number generated .
    """
    try:
        cursor.execute(
            "INSERT INTO randoms (random_num) VALUES (?)", (num,))
        print(f"{num} was inserted into the database")
    except (mariadb.Error, mariadb.Warning) as e:
        print(e)
    conn.commit()


if __name__ == "__main__":
    main()
