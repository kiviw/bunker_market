'''
Login module for Bunker marketplace.
'''
from database import Database
class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def authenticate(self):
        db = Database()
        db.connect()
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        result = db.execute_query(query, (self.username, self.password))
        db.disconnect()
        if len(result) > 0:
            return True
        else:
            return False