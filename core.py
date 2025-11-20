from sqlalchemy import (
    Table, Column, Integer, String,
    select, insert, update, delete,
)
from config import engine, metadata_obj


user_table = Table(
    "users",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String(127), unique=True, nullable=False),
    Column("password", String(255)),
)
metadata_obj.create_all(engine)

def get_users():
    with engine.connect() as connection:
        stmt = select(user_table)
        return list(connection.execute(stmt))

def get_user_by_username(username: str):
    with engine.connect() as connection:
        stmt = select(user_table).where(user_table.columns.username==username)
        return connection.execute(stmt).first()

def add_user(username: str, password: str):
    with engine.connect() as connection:
        stmt = insert(user_table).values(username=username, password=password)
        connection.execute(stmt)
        connection.commit()

def update_user(username: str, new_username: str):
    with engine.connect() as connection:
        stmt = update(user_table).where(user_table.columns.username==username).values(username=new_username)
        connection.execute(stmt)
        connection.commit()

def delete_user(username: str):
    with engine.connect() as connection:
        stmt = delete(user_table).where(user_table.columns.username==username)
        connection.execute(stmt)
        connection.commit()

# add_user('sami', '321')
# users = get_users()
# print(users)
# user = get_user_by_username('fnakjsbdfj')
# print(user)
# update_user('ali', 'gani')
# delete_user('vali')