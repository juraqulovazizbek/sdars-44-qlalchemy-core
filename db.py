import psycopg2
from config import config


with psycopg2.connect(
    database = config.DB_NAME,
    user = config.DB_USER,
    password = config.DB_PASS,
    host = config.DB_HOST,
    port = config.DB_PORT
) as connection:

    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, username VARCHAR(150) NOT NULL UNIQUE , password VARCHAR(150))")
    # cursor.execute("INSERT INTO users (username, password) VALUES ('ALI', '5445') , ('Vali', '8787'); ")

    name = input("username: ")
    password = input("password: ")

    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (name, password))

    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()
    
    for user in users:
        print(user[0], user[1], user[2])

    connection.commit()