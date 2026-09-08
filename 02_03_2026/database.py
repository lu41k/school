from mysql.connector import connect
from config import host, user, password, db_name


class Database:
    def __init__(self):
        self.connection = connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        self.cursor = self.connection.cursor()

    def select_curdate(self):
        self.__init__()

        select = "SELECT CURDATE()"
        self.cursor.execute(select)

        info = self.cursor.fetchone()
        self.connection.close()

        date = info[0]

        return date

    def add_user(self, name: str, email: str, password: str):
        self.__init__()

        select = f"INSERT INTO users (username, email, password_hash) VALUES ('{name}', '{email}', '{password}');"
        self.cursor.execute(select)

        self.connection.commit()
        self.connection.close()
