import sqlite3

def create_table_users():
    db = sqlite3.connect('instagram.db')
    cursor = db.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        username TEXT,
        email TEXT,
        phone TEXT,
        address TEXT
    );
    ''')
    db.commit()
    db.close()

# create_table_users()

def save_users_data(*args):
    db = sqlite3.connect('instagram.db')
    cursor = db.cursor()
    cursor.execute('''
    INSERT INTO users(name, username, email, phone, address)
    VALUES (?, ?, ?, ?, ?)
    ''', args )
    db.commit()
    db.close()



def create_table_posts():
    db = sqlite3.connect('instagram.db')
    cursor = db.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       title TEXT,
       body TEXT,
       user_id INTEGER REFERENCES users(id) 
    );
    ''')
    db.commit()
    db.close()


# create_table_posts()


def save_posts_data(*args):
    db = sqlite3.connect('instagram.db')
    cursor = db.cursor()
    cursor.execute('''
    INSERT INTO posts(title, body, user_id)
    VALUES(?, ?, ?)
    ''', args)
    db.commit()
    db.close()


def create_table_comments():
    db = sqlite3.connect('instagram.db')
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comments(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email VARCHAR(150),
            body TEXT,
            post_id INTEGER REFERENCES posts(id)
        );
    ''')

# create_table_comments()

def save_comment_data(*args):
    db = sqlite3.connect('instagram.db')
    cursor = db.cursor()
    cursor.execute('''
    INSERT INTO comments(name,email,body,post_id)
    VALUES(?,?,?,?)
    ''', args)
    db.commit()
    db.close()


def create_table_albums():
    db = sqlite3.connect('instagram.db')
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS albums(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            user_id INTEGER REFERENCES users(id) 
        );
    ''')
# create_table_albums()

def save_albums_data(*args):
    db = sqlite3.connect('instagram.db')
    cursor = db.cursor()
    cursor.execute('''
    INSERT INTO albums(title,user_id)
    VALUES(?,?)
    ''', args)
    db.commit()
    db.close()

def create_table_photos():
    db = sqlite3.connect('instagram.db')
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS photos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            url TEXT,
            thumbnailUrl TEXT,
            album_id INTEGER REFERENCES albums(id) 
        );
    ''')

# create_table_photos()

def save_photos_data(*args):
    db = sqlite3.connect('instagram.db')
    cursor = db.cursor()
    cursor.execute('''
    INSERT INTO photos(title,url,thumbnailUrl,album_id)
    VALUES(?,?,?,?)
    ''', args)
    db.commit()
    db.close()
