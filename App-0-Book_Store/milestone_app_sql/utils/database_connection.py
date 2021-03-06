import sqlite3


class DatabaseConnection:
    def __init__(self, host):
        self.connection = None  # criando a propriedade que guardará a conexão
        self.host = host

    def __enter__(self) -> sqlite3.Connection:
        self.connection = sqlite3.connect('data.db')
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()
