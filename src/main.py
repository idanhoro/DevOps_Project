from time import sleep
import os
import random
import mariadb


def start():
    conn = get_db_conn()
    cursor = get_cursor(conn)

    while os.environ.get("RUN_APP") == "true":
        randomNumber = random.randint(0, 255)
        insert_entry(conn, cursor, randomNumber)
        sleep(60)
    conn.close()


def main():
    start()


def get_db_conn():
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
    return conn.cursor()


def insert_entry(conn, cursor, num: int):
    try:
        cursor.execute(
            "INSERT INTO randoms (random_num) VALUES (?)", (num,))
        print(f"{num} was inserted into the database")
    except (mariadb.Error, mariadb.Warning) as e:
        print(e)
    conn.commit()


if __name__ == "__main__":
    main()
