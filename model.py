from datetime import datetime

from db import DB


class Tweets:

    @staticmethod
    def create_table():
        with DB().conn as conn, conn.cursor() as cursor:
            cursor.execute('''CREATE TABLE tweets (
            id SERIAL PRIMARY KEY,
            device VARCHAR(255),
            tweet_url VARCHAR(255) NOT NULL UNIQUE,
            user_url VARCHAR(255),
            user_location VARCHAR(255),
            username VARCHAR(255) NOT NULL,
            content TEXT NOT NULL,
            publish_date VARCHAR(255),
            created_date TIMESTAMP DEFAULT NOW(),
            hashtags VARCHAR(255) NOT NULL 
            );
            
            -- Optional index on the 'username' field
            CREATE INDEX idx_username ON tweets (username);
            ''')

    @staticmethod
    def save(device, tweet_url, user_url, user_location, username, content, publish_date,
                 hashtags= None):
        with DB().conn as conn, conn.cursor() as cursor:
            cursor.execute('''INSERT INTO tweets 
            (device, tweet_url, user_url, user_location, username, content, publish_date, hashtags)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);''',
                           (device, tweet_url, user_url, user_location, username,
                            content, publish_date, hashtags))


    @staticmethod
    def get_item(id):
        with DB().conn as conn, conn.cursor() as cursor:
            cursor.execute("SELECT * FROM tweets WHERE id = %s", (id,))
            result = cursor.fetchone()
            if result:
                return result
            else:
                return None

    @staticmethod
    def get_all_items():
        with DB().conn as conn, conn.cursor() as cursor:
            cursor.execute("SELECT * FROM tweets")
            result = cursor.fetchall()
            if result:
                return result
            else:
                return None