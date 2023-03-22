import psycopg2
from decouple import config


class DB:
    database = config('DATABASE')
    host = config('HOST')
    user = config('USERNAME')
    password = config('PASSWORD')
    port = config('PORT')

    def __init__(self):
        self.conn = psycopg2.connect(database=self.database,
                                     host=self.host,
                                     user=self.user,
                                     password=self.password,
                                     port=self.port)
        self.cursor = self.conn.cursor()
