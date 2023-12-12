'''
Database module for Bunker marketplace.
'''
import mysql.connector
import configparser
class Database:
    def __init__(self):
        self.connection = None
    def connect(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        host = config.get('database', 'host')
        port = config.get('database', 'port')
        username = config.get('database', 'username')
        password = config.get('database', 'password')
        database = config.get('database', 'database')
        self.connection = mysql.connector.connect(
            host=host,
            port=port,
            user=username,
            password=password,
            database=database
        )
    def disconnect(self):
        if self.connection:
            self.connection.close()
    def execute_query(self, query, params=None):
        cursor = self.connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result