# '''
# module - python file
#
# package - module lar yigindisi va __init__.py
# folder, directory, papka
#
# absolute & relative path
# '''
# from numpy.distutils.fcompiler import environment
#
# # context manager
# #
# # class CustomContextManager:
# #
# #     def __enter__(self):
# #         print('kirish')
# #
# #     def __exit__(self, exc_type, exc_value, traceback):
# #         print('chiqish')
# #
# #
# # with CustomContextManager():
# #     print('ichida')
# #
# # # scope
# # #
# # # for i in range(2, 3):
# # #     print(i)
# # #
# # #
# # #
# # # def add(a):
# # #  print(a)
# # #  print(a)
# # #  if True:
# # #             print(1)
# # #             print(20)
# # #
# # #
# # # # enter exit
# # # with open('lesson_1.py', 'r') as f:
# # #     with open('lesson_2.py', 'r') as f2:
# # #         print(f)
#
#
# # os, hashlib,
# #
# #
# # import httpx
# # import pandas
# # import aiogram
# #
# # python3 -m venv nomi1 (httpx)
# # python3 -m venv nomi2 (aiogram)
# # virtual environment
# #
# '''
# venv, pip
#
# pip3 install aiogram
#
# pip3 list
# pip3 freeze
# pip3 freeze > requirements.txt
# pip3 install -r requirements.txt
# pip3 uninstall
#
# source venv/bin/activate
# . venv/bin/activate
#
# deactivate
#
# python
# pyhon
#
# mkdir
# ls
# touch
# cat
# rm -r
# pwd
# cd
#
#
#
# 3ta venv
#
# 1) httpx, pyyaml (venv1.txt)
#
# 2) aiogram, requests (venv2.txt)
#
# 3) fastapi, httpx (venv3.txt)
#
# '''
#

# psycopg2
# psycopg2-binary


# crud - create, read, update, delete


# CRUD - create, read, update, delete
# import psycopg2
# from psycopg2.extras import DictCursor
#
# conn = psycopg2.connect(
#     database='p11_db',
#     user='postgres',
#     password='1',
#     cursor_factory=DictCursor
# )
#
# cur = conn.cursor()

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

'''

magazin

create table product(
    id serial primary key,
    name varchar(255) not null,
    price integer not null,
    amount integer not null
);


1. show all products (id, name, price)
2. show product (id, name, price, amount)
3. add product
4. remove product
5. change product
6. exit


decorator, generator, iterator

'''

