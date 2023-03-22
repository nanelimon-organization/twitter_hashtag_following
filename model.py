from datetime import datetime

from db import DB


class Tweets:
    def __init__(self, id, device, tweet_url, user_url, user_location, username, content, publish_date,
                 created_date=None, hashtags= None):
        self.id = id
        self.device = device
        self.tweet_url = tweet_url
        self.user_url = user_url
        self.user_location = user_location
        self.username = username
        self.content = content
        self.publish_date = datetime.strptime(publish_date, '%d-%m-%Y:%H:%M:%S')
        if created_date is None:
            self.created_date = datetime.now().strftime('%d-%m-%Y:%H:%M:%S')
        else:
            self.created_date = created_date.strftime('%d-%m-%Y:%H:%M:%S')
        self.hashtags = hashtags

    @classmethod
    def create_table(cls):
        with DB().conn as conn, conn.cursor() as cursor:
            cursor.execute('''CREATE TABLE tweets (
            id SERIAL PRIMARY KEY,
            device VARCHAR(255),
            tweet_url VARCHAR(255) NOT NULL UNIQUE,
            user_url VARCHAR(255),
            user_location VARCHAR(255),
            username VARCHAR(255) NOT NULL,
            content TEXT NOT NULL,
            publish_date TIMESTAMP,
            created_date TIMESTAMP DEFAULT NOW(),
            hashtags VARCHAR(255) NOT NULL 
            );
            
            -- Optional index on the 'username' field
            CREATE INDEX idx_username ON tweets (username);
            ''')

    def save(self):
        with DB().conn as conn, conn.cursor() as cursor:
            cursor.execute('''INSERT INTO tweets 
            (device, tweet_url, user_url, user_location, username, content, publish_date, created_date, hashtags)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);''',
                           (self.device, self.tweet_url, self.user_url, self.user_location, self.username,
                            self.content, self.publish_date, self.created_date, self.hashtags))

    @classmethod
    def get_item(cls, id):
        with DB().conn as conn, conn.cursor() as cursor:
            cursor.execute("SELECT * FROM tweets WHERE id = %s", (id,))
            result = cursor.fetchone()
            if result:
                return cls(*result)
            else:
                return None
