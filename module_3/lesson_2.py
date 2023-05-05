import psycopg2
from psycopg2.extras import DictCursor

conn = psycopg2.connect(
    database='p11_db',
    user='postgres',
    password='1',
    cursor_factory=DictCursor
)

cur = conn.cursor()

# CREATE
#
# # 1ta qoshish
#
# data = ('1', 'last_name', 'address', 6)
# query = 'INSERT INTO student(first_name, last_name, address, age) values (%s, %s, %s, %s)'
# cur.execute(query, data)
#
#
# # kop qoshish
# data = [
#     ('1', 'last_name', 'address', 6),
#     ('2', 'last_name', 'address', 7),
#     ('3', 'last_name', 'address', 8),
#     ('4', 'last_name', 'address', 9),
# ]
# query = 'INSERT INTO student(first_name, last_name, address, age) values (%s, %s, %s, %s)'
# cur.executemany(query, data)
#
# conn.commit()
# conn.close()
#
# # # READ
# query = 'select * from student'
# cur.execute(query)
# students = cur.fetchall()
# for student in students:
#     print(student['first_name'])


# # UPDATE
# data = ('ozgardi ism', 2)
# query = 'update student set first_name = %s where id = %s'
# cur.execute(query, data)
# conn.commit()


# # DELETE
# data = (2, )
# query = 'delete from student where id = %s'
# cur.execute(query, data)
# conn.commit()
from datetime import datetime

datetime.now().strftime('')

'interval - 7 days'
'''

magazin

create table product(
    id serial primary key,
    name varchar(255) not null,
    price integer not null,
    amount integer not null
);

primary key - not null + unique

create table users(
    id serial primary key,
    name varchar(255) not null,
    email varchar(255) not null unique,
    username varchar(255) not null unique,
    is_client bool default true,
    password varchar(255) not null,
    year integer not null,
    registered_at timestamp default now()
);

create table product
(
    id         serial primary key,
    name       varchar(255) not null,
    price      integer      not null,
    owner_id   integer      not null references users (id) on delete cascade,
    created_at timestamp default now()
);


create table orders
(
    id         serial primary key,
    product_id integer not null references product (id) on delete cascade,
    users_id   integer not null references users (id) on delete cascade,
    amount     integer not null,
    created_at timestamp default now()
);





bcrypt + pg + psycopg2

1. login
    -username
    -password
2. register
    -name
    -username
    -password
    -year
    
3. exit

users, product, order


client (default balance 5000)
    1. buy product
    2. check balance
    3. history
    4. exit

merchant
    1. show all products (id, name, price)
    2. show product (id, name, price, amount)
    3. my added products
    4. add product
    5. remove product
    6. change product
    7. report
        1. daily
        2. weekly
        3. monthly
    8. send report (jami sotilgan pruductlar soni va qancha savdo bo'lgani pochtasiga yuboriladi)
    9. exit



mypy, decorator, generator, iterator

'''

