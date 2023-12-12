'''
Registration module for Bunker marketplace.
'''
from database import Database
class Registration:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def register(self):
        db = Database()
        db.connect()
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        db.execute_query(query, (self.username, self.password))
        db.disconnect()
        return True