from sqlalchemy import (
    Table, Column, Integer, String,
    select, insert, update, delete
)
from config import engine, metadata_obj

user_table = Table(
    "users",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String(150), nullable=False, unique=True),
    Column("password", String(150)),
)
metadata_obj.create_all(engine)

def get_users():
    with engine.connect() as connection:
        stmt = select(user_table)
        return list(connection.execute(stmt))
def get_user_by_username(username:str):
    with engine.connect() as connection:
        stmt = select(user_table).where(user_table.c.username == username)
        return connection.execute(stmt).first()

def add_user(username:str, password:str):
    with engine.connect() as connection:
        stmt = insert(user_table).values(username=username, password=password)
        connection.execute(stmt)
        connection.commit()

def update_user(username:str, new_username:str):
     with engine.connect() as connection:
        stmt = update(user_table).where(user_table.columns.username == username).values(username=new_username)
        connection.execute(stmt)
        connection.commit()

def delete_user(username:str):
     with engine.connect() as connection:
        stmt = delete(user_table).where(user_table.columns.username == username)
        connection.execute(stmt)
        connection.commit()

users = get_users()
for user in users:
    print(user)

# # a = get_user_by_username("rgerg")
# # print(a)
    
# delete_user("vali")