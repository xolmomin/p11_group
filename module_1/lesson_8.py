# # # https://algo.ubtuit.uz/problem/166
# # def g(a, b):
# #     return (a * a + b * b) / (a * a + 2 * a * b + 3 * b * b + 4)
# #
# #
# # t, s = map(float, input().split())
# #
# # s = g(1.2, s) + g(t, s) + g(2 * s - 1, s * t)
# #
# # print(f'{s:.2f}')
# #
#
# '''
# +a 4
# -b 2
# h  4
#
# 2, 6
# '''
# # 0232
#
# # # https://algo.ubtuit.uz/problem/232
# # a, b, h = map(int, input().split())
# # count = result = 0
# #
# # if a >= h:
# #     print(1)
# # elif a > b:
# #     while h >= result:
# #         result += a
# #         count += 1
# #         if h <= result:
# #             break
# #         result -= b
# #     print(count)
# # else:
# #     print(-1)
#
#
# # num = input()
# # t = sum(map(lambda x: int(num[x]), range(0, len(num), 2)))
# # j = sum(map(lambda x: int(num[x]), range(1, len(num) + 1, 2)))
# # print('yes') if t == j else print('no')
# #
# # # 224
#
# # n = input()
# # sums1 = sum(map(int, (l for l in n[::2])))
# # sums2 = sum(map(int, (l for l in n[1::2])))
# # print("yes" if sums1 == sums2 else "no")
#
#
# # a = input()
# #
# # if int(a[0]) + int(a[2]) + int(a[4]) == int(a[1]) + int(a[3]) + int(a[5]):
# #     print('yes')
# # else:
# #     print('no')
#
#
# # # 238
# # from math import sqrt
# # n = int(input())
# # if int(sqrt(n)) ** 2 == n:
# #     print(1)
# # else:
# #     print(0)
# #
# # '''
# # 18 = 1,2,3,6,9,18
# # 19 = 1, 19
# # 50 = 1,  2, 5, 10, 25, 50
# # 100 = 1, 2, 4, 5, 10, 20, 25, 50, 100
# # '''
#
# # n = int(input())
# # count = 0
# # for i in range(1, (n + 1) // 2):
# #     if n % i == 0:
# #         count += 1
# #
# # e = count % 2
# # print(e)
# # from pprint import pprint
#
# '''
# 1 2 3 5 8 13 21 34 55
#
# 1 - 1
# 2 - 2
# 3 - 3
# 4 - 5
#
# '''
# #
# # n = 9
# # a1 = 1
# # a2 = 1
# #
# # for i in range(n - 1):
# #     a1 = a1 + a2
# #     a2 = a1 - a2
# #
# # print(a1)
#
#
# # set, dict
# # student = {
# #     'name': 'Botirjon 2',
# #     'age': 15,
# #     'address': 'Toshkent viloyati'
# # }
# # # yoshi < 15 va juft
# #
# #
# # d = [
# #     {
# #         'name': 'botirjon',
# #         'age': 18,
# #         'address': 'Toshkent'
# #     },
# #     {
# #         'name': 'botirjon',
# #         'age': 13,
# #         'address': 'Toshkent'
# #     },
# #     {
# #         'name': 'botirjon',
# #         'age': 14,
# #         'address': 'Toshkent'
# #     }
# # ]
# # for i in d:
# #     if i['age'] < 15 and i['age'] % 2 == 0:
# #         i.update(student)
# #
# #
# # pprint(d)
# # d = {
# #     ['name', 3, 4, 5]: 'botirjon',
# #     ('name', 3, 4, 5): 'botirjon',
# #     'age': 15,
# #     'address': 'Toshkent'
# # }
# #
# # # d['age'] = 12
# # # d['age'] = 12
# # d.update({
# #     'age': 13,
# #     'address': 'Samarqand',
# # })
# #
# # print(d)
# # 16 <
#
# # t = d.popitem()
# # t = d.pop('age123')
# # del d['age']
# # print(t)
# # print(d)
#
# # for key, value in d.items():
# #     print(key, value)
#
# # d['class'] = '7-sinf'
# # d['age'] = 20
# # d['age'] = None
#
# # print(d.get('age123'))
# # print(d['age123'])
#
# # d = {}
# #
# # d.update({1: 2})
# # print(d)
# # s = 'hhello 1 23'
# # d = {}
# # list comprehension
# # dict comprehension
# #
# # for i in s:
# #     if d.get(i):
# #         d[i] += 1
# #     else:
# #         d[i] = 1
# # d = {}
# # result = {d.update({i: d[i] + 1}) if d.get(i) else d.update({i: 1}) for i in s}
# # print(d)
#
# # if d.get(i):
# #     d[i] += 1
# # else:
# #     d[i] = 1
#
# # print(d)
#
# # d = {
# #     'h': 1,
# #     'e': 1,
# #     'l': 3,
# #     'o': 2,
# #     ' ': 1,
# #     'w': 1,
# #     'r': 1,
# #     'd': 1
# # }
# #
# # print(d)
# #
#
# # s = 'hello world 123460'
# #
# # d = {
# #     'h': 0
# # }
# # for i in s:
# #     if i in d.keys():
# #         d[i] += 1
# #     else:
# #         d[i] = 1
# #
# # pprint(d)
#
#
#
# # from collections import Counter
#
#
# from collections import Counter
# s = 'hello world'
# print(Counter(s).most_common(2))

# a = [2, 3, 4, 5, 6]
# [2, 4, 6, 3, 5]

# products = [
#     {
#         'name': 'nok',
#         'count': 28,
#         'price': 14000
#     },
#     {
#         'name': 'olma',
#         'count': 20,
#         'price': 17000
#     },
# ]
#
# name = input('Tovar nomini kiriting: ')
#
# for student in products:
#     if student['name'] == name:
#         print('bazada borsiz !')
#         break
# else:
#     print('baza yoq! ')


# from pprint import pprint
#
# products = [
#     {
#         'name': 'nok',
#         'count': 28,
#         'price': 14000
#     },
#     {
#         'name': 'olma',
#         'count': 20,
#         'price': 17000
#     },
# ]
#
# def buy_product(name, count):
#     for product in products:
#         if product['name'] == name:
#             if product['count'] < count:
#                 print('Yetarlimas !')
#                 break
#             product['count'] -= count
#     print('Tovar olindi ! ')
#
# while True:
#     text = '''
#     1. buy product
#     2. show products
#     3. exit
#
#     '''
#     key = input(text + 'bolimni kiriting: ')
#
#     if key == '1':
#         name = input('Product nomini kiriting: ')
#         count = int(input('nechta olmoqchisiz: '))
#         buy_product(name, count)
#     elif key == '2':
#         pprint(products)
#     elif key == '3':
#         print('Tugadi ! ')
#         break
# users, products
# users
# username, age, balance

# products
# name, price, count

# users = []  # 10ta username
#

# from os import system
# while True:
#     s = input('nimadir kiriting ! ')
#     if s == 'c':
#         system('clear')
#     else:
#         print(s)
#

'''

users, products
users
username, age, balance

products
name, price, count

users = []  # 10ta username


switch user
check balance
buy product
show products
exit

'''
