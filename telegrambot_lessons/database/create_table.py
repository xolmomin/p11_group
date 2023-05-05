from telegrambot_lessons.database.db import cur


def create_table_product():
    query = '''
    CREATE TABLE IF NOT EXISTS product(
        id serial primary key,
        name varchar(255) not null
    );
    '''
    cur.execute(query)


def create_table_users():
    query = '''
    CREATE TABLE IF NOT EXISTS users(
        user_id varchar(55) primary key,
        first_name varchar(255) not null,
        last_name varchar(255),
        username varchar(255),
        created_at timestamp default now() not null
    );
    '''
    cur.execute(query)


def create_table_category():
    query = '''
    CREATE TABLE IF NOT EXISTS category(
        id serial primary key,
        name varchar(255) not null
    );
    '''
    cur.execute(query)


def run():
    create_table_users()
