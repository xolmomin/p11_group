'''
iterable
iterator
iter
next

generator
'''

# from collections import Counter, defaultdict, namedtuple
from itertools import chain, product, cycle, repeat, accumulate, groupby, dropwhile, takewhile, zip_longest, starmap, \
    permutations, compress, combinations
from typing import Iterable, Any


#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6, 7, 8],
#     [7, 8, 100, 2],
# ]

# zip_longest(*matrix, =2)
# print(list(zip_longest(*matrix)))
# def zip_longest():

# eng katta son bilan toldirish kk, yetmay qolganiga


# matrix = zip(*zip_longest(*matrix, fillvalue=max(chain(*matrix))))
#
# for i in matrix:
#     print(i)

# for i in list(zip_longest(*matrix, fillvalue=0)):
#     print(i)

# print(sum(chain(*matrix)))

# class Student:
#
#     def __init__(self, name: str, age: int) -> None:
#         self.name = name
#         self.age = age
#
# s1 = Student('Botirjon', 15)
# print(s1.name)

# Student = namedtuple('Student', ['name', 'age'])
#
# s1 = Student('Botirjon', 15)
# print(s1[0])

# Vali

# stack(LIFO), queue(FIFO)
'''
2, 3, 4, 5
5, 2, 3, 4
'''


# def adding(*args):
#     return list(chain(*args))

# def adding(*args):
#     return [j for i in args for j in i]


# a = adding([2, 3, 4], [1, 2], [1])  # -> [2,3,4,1,2,1]
# print(a)
#
# class deque(list):
#
#     def appendleft(self, _x: Any) -> None:
#         self.insert(0, _x)
#
#     def extendleft(self, t: Iterable) -> None:
#         self[:] = list(t)[::-1] + self
#
#     def rotate(self, n: int):
#         n %= len(self)
#         n *= -1
#         self[:] = self[n:] + self[:n]
#
#     def popleft(self) -> Any:
#         return self.pop(0)
#
#     def is_empty(self) -> bool:
#         # return bool(self)
#         return not self


# a = [1, 2, 3, 4]
# d = deque(a)
# d.rotate(25)
# print(d)
# d.insert(0, 0)
# print(d)
# d.append(111)
# print(d)

# print(d.is_empty())


# 10:43
#
# def rotate(l: list, n: int):
#     n *= -1
#     l[:] = l[n:] + l[:n]
#
# n = 4
# a = [2, 3, 4, 5]
# b = a.copy()
#
#
# print(a, 'orginal')
# rotate(a, n)
# print(a)
# d = deque(b)
#
#
# d.rotate(n)
# print(d)

# def print_hello():
#     yield '1'
#     yield '2'
#     yield '3'
#     print('hello')
#
#
# a = list(print_hello())
# print(a)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# for i in print_hello():
#     # if i == '3':
#     #     break
#     print(i)

# b = (i for i in range(10))
#
# print(type(b), b)
# print(b[-1])
#
# a = [2, 3, 4]
# a = set(a)
# i = a.__iter__()
# print(next(i))
# print(next(i))
# print(next(i))

