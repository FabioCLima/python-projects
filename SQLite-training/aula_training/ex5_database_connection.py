import sqlite3


class DatabaseConnection:
    def __init__(self, host) -> None:
        self.connection = None
        self.host = host

    def __enter__(self):
        self.connection = sqlite3.connect('dados_alunos.db')
        return self.connection

    def __exit__(self, *args):
        self.connection.commit()
        self.connection.close()
