'''
load = file -> object
loads - str -> object
dump = object -> file
dumps = object -> str
'''

#
# '''
# 2-3 level
# {
#     'module_1': {
#         'invalid.json': 'file',
#         'invalid_comments.json': 'file',
#         'lesson_1.py': 'file'
#     }
#     'module_2': {
#         'albums.json': 'file',
#         'districts.json': 'file',
#         'lesson_1.py': 'file',
#         'test123': {
#             '1.py': 'file',
#             '2.py': 'file',
#         }
#     },
#     'data.json': 'file',
#     'districts.csv': 'file'
# }
#
# '''


#
# import json
# d = {
#     'name': 'Botirjon',
#     'chars': ['''а''', 'э', 'ы', 'у', 'о', 'я', 'е', 'ё', "ю", "и"]
# }
#
# with open('test.json', 'w') as f:
#     json.dump(d, f, indent=2, ensure_ascii=False)
#
#
# with open('test.json') as f:
#     d = json.load(f)
#
# print(d)
#
# result = json.dumps(d, ensure_ascii=False)
# print(type(result), result)
#
#
# s = json.loads(result)
#
# print(type(s), s)
#
#
# d = {
#     'json': ['activities', 'albums', 'comments', 'data.test'],
#     'py': ['lesson_1', 'lesson_2', 'lesson_3'],
#     'csv': ['regions', 'districts']
# }
#
#
# 'data.test.json'.rsplit('.')
# 'test.json'.split('.')
#
#
# import json
# import os
# from collections import defaultdict
#
# data = defaultdict(list)
#
# for i in os.listdir():
#     if os.path.isfile(i):
#         name, ext = i.rsplit('.', 1)
#         data[ext].append(name)
#
# with open('data.json', 'w') as f:
#     json.dump(data, f, indent=2)


# from dataclasses import dataclass, asdict, astuple


# decorator

# @dataclass(init=True, repr=False, eq=True, order=False, unsafe_hash=False, frozen=False)
# @dataclass(init=True, repr=False, eq=True, order=False, frozen=False, kw_only=True)
# class Student:
#     id: int
#     name: str
#     age: int
#
# s1 = Student(1, "botirjon1", 16)
#
# print(s1)

# s = {s1}
# print(s)


# l = [1, 2, 3]
#
# print(hash(l))


# class Student:
#     __slots__ = ['id', 'name', 'age']
#
#     def __init__(self, id, name, age) -> None:
#         self.id = id
#         self.name = name
#         self.age = age
#
# s1 = Student(1, 'Botirjon', 15)
# s1.address = 'Toshkent'
# s1.email = 'botirjon@gmail.com'
#
# print(s1.name)
# print(s1.address)
# print(s1.email)

# print(asdict(s1))
# print(astuple(s1))

#
# def fun(address, a, b, c, /, nimadir, d, t, e, *, id, name, age):
#     print(id, name, age, address)
#
#
# '''
# position based - orni boyicha
# keyword based - kaliti boyicha
# '''
#
# fun(12, 2, 3, 4,  2, 3, 21,e=4, name='Botirjon', age=15, id=23)
# fun(1, 'Botirjon', 15)

'''
l = [2, 3, 4]

multiply(3)
add(5)
slice(1, 3)

'''
#
#
# class List(list):
#     def multiply(self, n: int) -> None:
#         for i in range(len(self)):
#             self[i] *= n
#
#     def add(self, n: int) -> None:
#         for i in range(len(self)):
#             self[i] += n
#
#     def slice(self, a: int, b: int) -> None:
#         self.clear()
#         self.extend(self[a - 1: b])
#
#         self = self[a - 1: b]
#
#
# l = List([2, 3, 4])
# print(l)
# l.add(1)
# print(l)
# l.multiply(2)
# print(l)
# l.slice(1, 2)
# print(l)


a = [2, 3, 4, 5]

print(hex(id(a)))

# a[:] = a[1:3]
# print(hex(id(a)))
print(a)

a[:] = a[:]
print(hex(id(a)))
print(a)


