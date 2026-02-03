from mysql.connector import connect
from config import host, user, password


class Database:
    def __init__(self):
        self.connection = connect(
            host=host,
            user=user,
            password=password
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

        select = f"INSERT INTO users (name, email, password, register_gate) VALUES ({name}, {email}, {password}, "
        self.cursor.execute(select)

        info = self.cursor.fetchone()
        self.connection.close()

        date = info[0]

        return date
