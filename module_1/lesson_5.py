'''
mutable(ozgaruvchi) - list, set, dict
immutable (ozgarmas) - int, float, bool, str, tuple
hashable - int, float, bool, str, tuple
unhashable - list, set, dict, tuple
iterable - list, str, tuple, dict, set
container - tuple, list, dict, set
sequence - list, str, dict, tuple

dict - keyi hashable, value esa ixtiyoriy boladi
set - ichidagi elementlar hashable bolishi kk
'''

# t = tuple()  # (2,)
# l = list()  # []
# s = set()  # {2}
# d = dict()  # {}
# s1 = str()  # ''
# i = int()
# print(i)

# s = {2, 3, 4, 5, 3, 3, 3}

# s.add('123')
# print(s.pop())
# s.remove('23')
# s.discard('123')
# s.update({2, 123, 4, 4})
# s1 = {1, 2, 5}
# s2 = {3, 4}
#
# print(not bool(s1.intersection(s2)))
# print(s1.isdisjoint(s2))
# print(s1.issuperset(s2))
# print(s2.issubset(s1))
# s1.intersection(s2)
# s1.intersection_update(s2)
# s1.symmetric_difference_update(s2) # s1 ^ s2
# result = s1.union(s2) # s1 | s2
# result = s2.difference(s1) # s1 - s2
# s2.difference_update(s1)
# print(s1.issubset(s2))
# print(s2.issubset(s1))
# print(s2)
# print(s1 | s2)
# print(result)

# a = [1, 2, 3, 4]
# b = [1, 2, 3, 4]
# print(hex(id(a)))
# print(hex(id(b)))
# print(a == b)  # content
# print(a is b)  # id

# s = s.copy()
# from copy import copy
# s = copy(s)

# print(s)
# s1 = 'hello'


# {'hello', 123, '23', 'a'}
# {'a', '23', 123, 'hello'}
# {'hello', 123, 'a', '23'}


# s = 'hello worlddddd'.split()
#
# result = set()
#
# for i in s:
#     result.update(set(i))i
#
# print(len(result))

# s = 'hello botir 12 12'
#
# result = set()
#
# for i in s:
#     if i.isdigit():
#         result.add(i)
#
# print(result)
# helowrd


# a = False
#
# if a:
#     print('Rost')
# else:
#     print("Yolgon")
#
# l = [123, '8rtt7', '1ab']
# digits = set()
# chars = set()
#
# chars.add('a')
# chars.add('a')
# chars.add('a')
# print(chars)
#
# for i in l:
#     for j in str(i):
#         if j.isdigit():
#             digits.add(j)
#         if j.isalpha():
#             chars.add(j)
#
# print('Raqamlar soni:', len(digits))
# print('Harflar soni:', len(chars))


# a = list(range(1, 11))
# print(a)

# result = {i: 'value' for i in a}  # dict comprehension
# result = {i for i in a}  # set comprehension
# result = [i for i in a]  # list comprehension

# result = [i + 2 if i & 1 else i * 2 for i in a]  # list comprehension
# result = [i for i in a if i % 2 == 0]  # list comprehension
# print(result)

# result = []
# for i in a:
#     if i & 1:
#         result.append(i + 2)
#     else:
#         result.append(i * 2)
#
# print(result)
# toq + 2
# juft * 2

# 1-50
# faqat toq sonlar
# agar 3 bolinsa *3 aks holda ozi chiqsin


# l = list(range(1, 51))
#
# result = [i * 3 if i % 3 == 0 else i for i in l if i % 2 == 1]
# print(result)
#




# 1-100
# 2, 7 karrali sonlar
# %7   +1
# aks holatda +2
# 2 4 6 7 8 14
#
#
# l = list(range(1, 101))
# result = [i + 1 if i % 7 == 0 else i + 2 for i in l if i % 2 == 0 or i % 7 == 0]
# print(result)
#
# '''
# 1-50
# 2,3  5  7
# %5 - 1
# %7 - 2
# %2 - 3
#
# 5 6 7 10 12 14
# 4 3 5 9
# '''
# a = range(1, 51)
# result = [i - 1 if i % 5 == 0 else i - 2 if i % 7 == 0 else i - 3 for i in a if i % 2 == 0 and i % 3 == 0 or i % 5 == 0 or i % 7 == 0]
# print(result)

# a = 9
#
# if a == 5:
#     result = '5ga teng'
# elif a == 7:
#     result = '7ga teng'
# elif a == 9:
#     result = '9ga teng'
# else:
#     result = 'oddiy son'
#
#
# result = '5ga teng' if a == 5 else '7ga teng' if a == 7 else '9ga teng' if a == 9 else 'oddiy son'
# print(result)