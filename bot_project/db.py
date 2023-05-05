import psycopg2
import os

con = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='77',
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT')
)


def create_table():
    query = '''
    CREATE TABLE IF NOT EXISTS history(
        id serial primary key,
        user_id bigint not null ,
        msg varchar(4096),
        created timestamp default now()
    );
    '''
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    cur.close()
