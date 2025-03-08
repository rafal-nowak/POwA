# Dependency Inversion Principle (DIP) – wysokopoziomowe moduły nie zależą od niskopoziomowych

from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def connect(self):
        pass


class MySQLDatabase(Database):
    def connect(self):
        return "Connecting to MySQL"


class Application:
    def __init__(self, database: Database):
        self.database = database

    def start(self):
        print(self.database.connect())

if __name__ == "__main__":
    # Przykład użycia
    mysql_db = MySQLDatabase()
    app = Application(mysql_db)
    app.start()