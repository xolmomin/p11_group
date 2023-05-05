# # import json
# import httpx
#
# '''
# load
# loads
# dump
# dumps
#
# with open
# open
#
#
# mode
#
# '''
#
# '''
# http methods
# GET(olish), POST(yaratish), PUT(ozgartirish), PATCH(ozgartirish), DELETE(ochirish)
# http status codes
# 2xx (information), 3xx(redirect), 4xx (client error), 5xx (server error)
#
# https://jsonplaceholder.typicode.com/
#
# https://jsonplaceholder.typicode.com/
#
# '''
#
#
# try:
#     response = httpx.get('https://google.com')
#     print(response.status_code)
# except httpx.ConnectError as e:
#     print('internet yoq!')
#
#
# # import os
# #
# # if not os.path.exists('data.json'):
# #     with open('data.json', 'w'):
# #         pass
# #
# # file = open('data.json')
# # d = file.read(10)
# # print(d)
#
# # try:
# #     file = open('data.json')
# #     d = file.read(10)
# #     print(d)
# # except FileNotFoundError as e:
# #     with open('data.json', 'w'):
# #         pass
# #     print('Xato chiqdi', e)
# # else:
# #     print('Xato chiqmadi')
# #
# # print('oxiri')
#
#
# from pprint import pprint
#
# import httpx
# import json
#
#
# def write_data(filename: str) -> None:
#     url = f'https://jsonplaceholder.typicode.com/{filename}'
#     response = httpx.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         with open(f'{filename}.json', 'w') as f:
#             json.dump(data, f, indent=2)
#     print(f'{filename} faylga yozildi!')
#
# names = ('posts', 'comments', 'albums', 'photos', 'todos', 'users')
# for name in names:
#     write_data(name)
#
# import csv
# import json
#
# regions: list[dict] = []
#
# with open('../regions.csv') as f:
#     f.readline()
#     for _id, name in csv.reader(f):
#         regions.append({
#             'id': int(_id),
#             'name': name
#         })
#
# with open('regions.json', 'w') as f:
#     json.dump(regions, f, indent=2)

#
# import csv
# import json
#
# districts: list[dict] = []
#
# with open('../districts.csv') as f:
#     f.readline()
#     for _id, name, region in csv.reader(f):
#         districts.append({
#             'id': int(_id),
#             'name': name,
#             'region': int(region)
#         })
#
# with open('districts.json', 'w') as f:
#     json.dump(districts, f, indent=2)

#
# import json
#
# with open('districts.json') as f:
#     districts: list[dict] = json.load(f)
#
# with open('regions.json') as f:
#     regions: list[dict] = json.load(f)
#
# for region in regions:
#     sub_district = []
#     for district in districts:
#         if district['region'] == region['id']:
#             sub_district.append({
#                 'id': district['id'],
#                 'name': district['name'],
#             })
#     region['districts'] = sub_district
#
#
# with open('task_regions.json', 'w') as f:
#     json.dump(regions, f, indent=2)
#
#
#

'''
homework

1.
task_posts.json (postga tegishli commentlar bn birga)
task_users.json (userga tegishli postlar va albumlar bn birga)
task_albums.json (userga tegishli postlar bn birga)


2.
task2_users.json (userlar albumlari bn birga album esa photos lari bn birga)


3. 
request orqali


3ta project (restaran, magazin, oquv markaz)
restaran
ofisant
mijoz


ekrandan product(name, price, quantity)
shularni json faylga yozadigan qilish kk

Olma 15 150
Redmi 250 48

[
    {
        "name": "Olma",
        "price": 15,
        "quantity": 150
    },
    {
        "name": "Redmi",
        "price": 250,
        "quantity": 48
    }
]


https://www.boredapi.com/api/activity
url dan type ga qarab alohida ajratib jsonga yozish

'''
#
# import httpx
#
# base_url = 'https://jsonplaceholder.typicode.com/'
# posts = httpx.get(base_url + 'posts').json()
#
# def remove_key(item):
#     item.pop('postId')
#     return item
#
# for post in posts[:5]:
#     post_comments = httpx.get(base_url + f'comments?postId={post["id"]}').json()
#     post['comments'] = list(map(remove_key, post_comments))
#
# with open('task_posts.json', 'w') as f:
#     json.dump(posts, f, indent=2)


