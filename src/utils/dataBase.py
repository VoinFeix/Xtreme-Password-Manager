import mysql.connector
from mysql.connector import Error

class DataBase:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = self.connect()

    def connect(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
            )
            print('Connected to MySql')
            return connection
        except Error as e:
            print(f"Error connecting to MySql, Error: {str(e)}")
            return None
    
    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Disconnected from MySql")

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params or ())
            cursor.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error getting query from MySql, Error: {str(e)}")
            return None
        finally: cursor.close()

    def fetch_all(self, query, params=None):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params or ())
            return cursor.fetchall()
        except Error as e:
            print(f"Error fetching all from MySql, Error: {str(e)}")
            return []
        finally: cursor.close()
    
host = 'localhost'
database = 'XTM'
user = 'admin'
password = 'admin'
# db = DataBase(host=host, database=database, user=user, password=password)
# # db.connect()


# db.execute_query("""
# INSERT INTO XTM (TITLE, EMAIL, USERNAME, PASSWORD, 2FA_KEY, WEBSITE, NOTE)\
# VALUES (%s, %s, %s, %s, %s, %s, %s)
# """)


# db.disconnect()

cnn = mysql.connector.connect(
    host=host,
    database=database,
    user=user,
    password=password
)

print(len(cnn))
