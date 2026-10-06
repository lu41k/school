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

        select = f"INSERT INTO users (username, email, password_hash) VALUES ('{name}', '{email}', '{password}') ON DUPLICATE KEY UPDATE `username` = '{name}';"
        self.cursor.execute(select)

        self.connection.commit()
        self.connection.close()

    def select_user(self, email: str) -> tuple:
        self.__init__()

        select = f"SELECT username FROM users WHERE email = '{email}';"
        self.cursor.execute(select)

        info = self.cursor.fetchone()
        self.connection.close()

        return info

    def select_user_password(self, email: str) -> str:
        self.__init__()

        select = f"SELECT password_hash FROM users WHERE email = '{email}';"
        self.cursor.execute(select)

        info = self.cursor.fetchone()
        self.connection.close()

        return info[0]
