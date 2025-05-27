import sqlite3

class ExecuteQuery:
    """
    Context manager for executing a query with parameters, managing the connection and execution.
    """
    def __init__(self, db_name, query, params=None):
        self.db_name = db_name
        self.query = query
        self.params = params or ()
        self.conn = None
        self.cursor = None
        self.results = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query, self.params)
        self.results = self.cursor.fetchall()
        return self.results

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
if __name__ == "__main__":
    db_file = "example.db"  # Change this to your database file
    query = "SELECT * FROM users WHERE age > ?"
    param = (25,)

    with ExecuteQuery(db_file, query, param) as results:
        for row in results:
            print(row)

