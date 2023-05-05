# a = 2
# b = a
# b = 7
from copy import copy

# a = [2, 3, 4]
#
# print(hex(id(a)))
# a.append(15)
# print(hex(id(a)))
#
# s = 'hello'
# print(hex(id(s)))
# s = s + ' world'
# print(hex(id(s)))
#

# b = a[:]
# b = a[::]
# b = a.copy()
# b = copy(a)

# b.append(8)
# print('a', a)
# print('b', b)
# mutable - agar shu object shu objectni ozgartirmoqchi bolsak,
# xotiradagi manzili ozgarmasa
# mutable - id ozgarmasa, content ozgarsa
# object - 3ta (id, type, content)

'''
mutable(ozgaruvchi) - list, set, dict
immutable (ozgarmas) - int, float, bool, str, tuple
hashable - int, float, bool, str, tuple
unhashable - list, set, dict, tuple
iterable - list, str, tuple, dict, set
container - tuple, list, dict, set
sequence - list, str, dict, tuple

'''
# from string import ascii_lowercase

# print(ascii_lowercase)

# for i, v in enumerate(ascii_lowercase, 1):
#     print(f'{v}({i})', end=' ')

# hello -> 8 5 12 12 15 (shifrlash crypt - encode)
# 8 5 12 12 15 -> hello (deshifrlash decrypt - decode)
# hash
# s = {2, 3, True, '5', [2, 3, 4]}
# print(s)

# a = [2, 3, 4]
# print(hash(a))

# list, tuple, str - set, dict
# packing, unpacking

# packing
# a = 5, 6, 7
# print(a, type(a))

# unpacking
# n, m, l = a
# print(n, m, l)

# a = 3
# b = 3
# a = b = 3
# a = ('olcha.uz', 'root')

# a = (5, 6)
# print(type(a))
# a = [2, 5, 4, 5, 6, 7]
# print(a[len(a) // 2], a[len(a) // 2 - 1])

#
# print(a)

# a.extend([2, 2, 3, 4])
# print(a)

# a.remove(4)
# print(a)
# a.reverse()
# print(a)

# a.sort(reverse=True)

# print(a)
# print(a.index(4, 2))
# for i, v in enumerate(a):
#     if v & 1:  # i % 2 == 1
#         print(i, v)
#    0  1  2  3  4
#   -5 -4 -3 -2 -1
# print(a.count(4))
# print(a[-3], a[2])
# print(a)
# print(a.count(2))
# print(a)

#
# for i in a:
#     print(i, end=' ')
#
# print()
# for i, v in enumerate(a):
#     print(v, end=' ')
#
# print()
# for i in range(len(a) - 1, -1, -2):
# # for i in range(4, 2, -1):
#     print(a[i], end=' ')


# a[::-1]
# a.reverse()
# task-1

# a = [5, 7, 9, 2, 4, 5, 8, 1]
#
# for i in range(len(a) // 2):  # 0, 1, 2, 3
#     print(a[-i - 1], a[i])
#
# task-2
# 1, 5, 8, 7, 5, 9, 4, 2


# a = [10, 5, 7, 9, 2, 4, 5, 8, 1, 9]
# l = list(map(int, input().split()))
# a, b = map(int, input().split())

# print(max(l[a - 1: b]))  # slicing, slice

# a = [10, 5, 7, 9, 2, 4, 5, 8, 1, 9]
# print(a[:len(a) // 2])
# print(a[:len(a) // 2 - 1:-1])
# polindrom

# s = '1234321'
#
# m = len(s) // 2
#
# for i in range(m):
#     if s[i] != s[len(s) - i - 1]:
#         print('palindrom emas')
#         break
# else:
#     print('palindrom')
# from string import ascii_lowercase
# s = 'hello world, pythonchilar'
#
# print(chr(98))
# print(ord('a'))
#
# unli = 'ouiae'
# count = 0
# for i in s:
#     if i not in unli and i in ascii_lowercase:
#         count += 1
# print(count)

# count = 0
# for i in s:
#     if i == 'o' or i == 'u' or i == 'i' or i == 'a' or i == 'e':
#         count += 1
# print(count)
#
# count = 0
# for i in range(len(s)):
#     if s[i] == 'o' or s[i] == 'u' or s[i] == 'i' or s[i] == 'a' or s[i] == 'e':
#         count += 1
# print(count)

#
# s = 'acbTbca'
#
# m = len(s) // 2
#
# for i in range(m):
#     if s[m + i + 1] != s[m - i - 1]:
#         print('palindrom emas')
#         break
# else:
#     print('palindrom')
#
#


# a = [2, 3, 4, 5]
#
# for i in a:
#     print(i, end=' ')
#     if i == 5:
#         break
# else:
#     print('joyida')

# print(len(s))

# print(s[::-1])
# a = [2, 3, 4]
# a.sort()
# a.reverse()

# print(a[len(a) // 2:][::-1])

# print(a[:4])  # 0, 1, 2, 3
# print(a[2::2])  # 0, 1, 2, 3
# print(a[4:2:-1])  # 0, 1, 2, 3
# print(a[::-1])  # 0, 1, 2, 3

# 3 6 2 3 5 7 8
# 1 3


# count = 0
# for i in a:
#     count += 1
#
# print(count)
# print(len(a))
# a.sort()
#
# maxi = a[0]
# for i in a:
#     if maxi < i:
#         maxi = i
# print(maxi)
#
# maxi2 = a[0]
# for i in a:
#     if i != maxi and maxi2 < i:
#         maxi2 = i
# print(maxi2)
#

# task-5
# 2chi eng kattasi

# max, min, sum ❌
