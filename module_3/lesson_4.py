# decorator

# # function with params
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @decorator
# def fun(*args) -> str:
#     return sum(args)

# # decorator with params
# def decorator(key=1):
#     def wrapper(func):
#         func()
#     return wrapper
#
#
# @decorator(key=1)
# def fun():
#     print('1')
#


# # decorator and function with params
# def decorator(key):
#     def inside(func):
#         def wrapper(a, b):
#             print(key)
#             func(a, b)
#
#         return wrapper
#
#     return inside
#
#
# @decorator(key='1')
# def fun(a, b):
#     print(a, b)


# decorator(key='1')(fun)(2, 3)

# fun(2, 3)

#
# def star(func):
#     def wrapper():
#         print('*')
#         func()
#         print('*')
#     return wrapper
#
#
# def plus(func):
#     def wrapper():
#         print('+')
#         func()
#         print('+')
#     return wrapper
#
#
# @star
# def add():
#     print(6)
#
#
# add()


# # task
#
# def multiply(doubled=1):
#     def inside(func):
#         def wrapper(a, b):
#             func(a * doubled, b * doubled)
#
#         return wrapper
#     return inside
#
#
# @multiply(doubled=2)
# def fun(a, b):
#     print(a, b)
#
#
# fun(2, 3)

'''
decorator, class decorator, decorator params
task

@decorator()
def fun(word):
    return word


result = fun('123')
print(result)

decorator params (upper, lower, to_type, reverse)
(bool, bool, type, bool)


'''
#
# s = 'h321312ello|fdfs2314|te336t|'
#
# print(s.split('|'))
# s = s.split('|')[1:-1]
# print(s)
#
#
# def fun(item):
#     return ''.join(filter(lambda i: i.isdigit(), item))
#
#
# s = list(map(fun, s))
# s = max(s, key=len)
#
# print(len(s), s)

# import time
# import random as r
#
# def timer(func):
#     def wrapper(word: str):
#         start = time.time()
#         if word.isdigit():
#             word = str(int(word) + 1)
#         else:
#             word = word + '1'
#
#         result = func(word)
#
#         end = time.time()
#         print(end - start)
#         return result
#
#     return wrapper
#
#
# @timer
# def fun(word: str) -> str:
#     return word
#
#
# word = '12r3'  # + 1
# print(fun(word))


#
# @timer
# def summa_list():
#     a = list(_ for _ in range(100_000))
#     summa = 0
#     for i in a:
#         summa += i
#     print(summa)
#
#
# # [1, 2, 3, 4, 5]
# # [44312, 42897, 43, 432,423]
#
# @timer
# def summa_tuple():
#     a = tuple(_ for _ in range(100_000))
#     summa = 0
#     for i in a:
#         summa += i
#     print(summa)


# summa_list()
# summa_tuple()

# task
# 1000 summa_list, summa_tuple

# list(i for i in range(1000))
# tuple(i for i in range(1000))

#
# @timer
# def summa_n():
#     summa = 0
#     for i in range(10_000_000):
#         summa += i
#     print(summa)
#
#
# @timer
# def mul_n():
#     summa = 1
#     for i in range(1, 100):
#         summa *= i
#     print(summa)
#
#
# summa_n()
# mul_n()


# add()

# start = time.time()  # 1679632743.080275
#
#
# end = time.time()  # 1679632745.080275
#
# print(end - start)

# print(time.time())

# epoch time, unix time


# decorator(add)()


#
# @decorator
# def sub():
#     print(9)
#
# sub()
