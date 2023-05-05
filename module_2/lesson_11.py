# from functools import lru_cache
from functools import wraps


# 4 * 26 + 5376 + 4 * 26

# @lru_cache # decorator
# def fib(n):
#     if n < 3:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
# # 1 1 2 3 5 8 13
# print(fib(150))
# # def fun(a, b):
# #     return a + b


# a = fun
#
# fun.name = 'Hello'
# print(a(2, 3))
# print(fun.name)
# print(a.name)
# a = add, sub
#
# d = {
#     True: True
# }
# key - unhashable

# d = {
#     ('key', 'value'): 'value'
# }
#
# print(d.get(('key', 'value'), 'nimadir'))

# mutable

# a = 'hello'
# b = a
#
# b += '123'
#
# print(hex(id(a)), a)
# print(hex(id(b)), b)

#
# from collections import Counter
#
# d = Counter()
#
# with open('photos.txt') as f:
#     while data := f.read(5000):
#         d.update(Counter(data))
#
# if d.get(' '): d.pop(' ')
# if d.get('\n'): d.pop('\n')
#
# print(*d.most_common(1))

#
# def func(fun):
#
#     @wraps(fun)
#     def wrapper(a, b):
#         fun(a, b)
#     return wrapper
#
#
# @func
# def add(a, b):
#     return a + b
#
# @func
# def sub(a, b):
#     return a - b
#
#
# print(add.__name__)
# print(sub.__name__)
#


# generator, iterator, decorator




# from datetime import datetime
#
# date = "6th Oct 2052"
# day, month, year = date.split()
# date = ' '.join([day[:-2], month, year])
# date = datetime.strptime(date, "%d %b %Y")
# r = date.strftime("%Y-%m-%d")
# print(r)
#

# s = '1233'
#
# print(s.zfill(4))

#
# date = "6th Oct 2052"
# day, month, year = date.split()
# day = day[:-2].zfill(2)
# months = (0, "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
# m = str(months.index(month)).zfill(2)
# r = f'{year}-{m}-{day}'
# print(r)


