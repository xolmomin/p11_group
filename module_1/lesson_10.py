# from collections import Counter
#
# nums = [1,1,1,1]
# summa = 0
# for i in Counter(nums).values():
#     summa += i * (i - 1) // 2
#
# print(summa)
import copy
import time

# typing hinting

# interpreter, compiler
# dynamic, static


# int a = 4;
#
# def add(a: str, b: str = 'Hello') -> int:
#     return int(a + b)
#
#
# print(add('11', '15') + 1)
# mypy


# sequence
# slice, slicing

# s = 'hello world'
# s[2:]


# mutable - set, list, dict


# a = [1, 5, 8, 2, 3]

# b = a.copy()
# b = a[:]
# b = a[::]
# b = list(a)
# from copy import copy
# b = copy(a)

# a = 'hello'
# b = a
#
#
# # a += 'world'
# # print(a)
# # print(b)
# print(hex(id(a)))
# print(hex(id(b)))

# a = 'hello world'
#
# b = 'hello world'
#
# a += ' 1'
# # is, ==
# print(a == b)
# print(a is b)
# print(a)
# print(b)
# print(hex(id(a)))
# print(hex(id(b)))


# nested list
# from copy import deepcopy
#
# a = [6, 3, [7, 2, 3, [2, 3, 4]]]
# b = deepcopy(a)
#
# print(hex(id(a[2])))
# print(hex(id(b[2])))
#
# a[2].append(5)
#
# print(hex(id(a[2])))
# print(hex(id(b[2])))
# print(a)
# print(b)
# print(type(datetime.now()))
# a = '5342'
#
#
#
# # print(isinstance(a, int))
# if type(a) == str:
#     print('bu str')


# from os import system
# from datetime import datetime, date, timedelta, time,timezone,tzinfo
#
# t = timezone('US/Eastern')
# print(t.utc)
#
# # datetime.now('')


# date1 = datetime(year=2000, month=8, day=15, hour=15, minute=19)
# result = date1 - timedelta(days=18)
# print(result)

# time, date, datetime

# print(time()) # vaqt
# print(date(1990, 5, 16)) # sana
# print(datetime.now()) # toliq

# date1 = datetime(year=2000, month=8, day=3, hour=15, minute=19)
# date2 = datetime(year=2005, month=8, day=3, hour=15, minute=19)
# print((date2 - date1).total_seconds())

# s = '27 January 11:14:15'
# result = datetime.strptime(s, '%d %B %H:%M:%S')
# print(result)

# current_date = datetime.now()
# result = current_date.strftime('%d %B %H:%M:%S')
# # system('clear')
# print(result)  # 27 January 11:14:15

# a = 'hello 3221'
# b = 'world'
#
# print(a)
# address = "1.1.1.1"
# result = address.replace('.', '[.]')
# print(result)

#
# s = "is2 sentence4 This1 a3"
#
#
# # v2
# # l = ' '.join(map(lambda i: i[:-1], sorted(s.split(), key=lambda i: i[-1])))
# # print(l)
#
# # v1
# # l = list(map(lambda i: (i[:-1], int(i[-1])), s))
# # l = list(sorted(l, key=lambda i: i[-1]))
# # l = ' '.join([i for i, v in l])
# # print(l)


names = ["Mary", "John", "Emma"]
heights = [180, 165, 170]



print(list(zip(names, heights)))
# "Mary", "Emma", "John"