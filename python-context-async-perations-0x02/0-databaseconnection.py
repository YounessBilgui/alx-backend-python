import sqlite3

class DatabaseConnection:
    def __init__(self, query):
        self.conn = None
        self.query = query
        self.cursor = None

    def __enter__(self):
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()


query = "SELECT * FROM users"

with DatabaseConnection(query) as cursor:
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
