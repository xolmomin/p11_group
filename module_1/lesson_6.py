# 114, 115, 116
#
# from decimal import Decimal, getcontext, ROUND_HALF_UP
# getcontext().rounding = ROUND_HALF_UP
#
# input()
# l = list(map(int, input().split()))
# m = max(l)
#
# for i in l:
#     print(f'{Decimal(i / m):.2f}')

#
# input()
# l = list(map(int, input().split()))
# k = int(input())
#
# summa = 0
# for i in l:
#     if i > k:
#         summa += i
# # summa = sum([i for i in l if i > k])
#
# print(summa)


# enumerate, range, zip, map, filter, reduce
# a = '1 6 2 8 3'
# l = a.split()
# l = ['1', '6', '2', '8', '3']
# n, m = map(int, input().split())
#

# '''
# 3 4
# ab hb t yt
# ebvf 43b jyt4 32ft
# fhj fhjk f33 f34h
# '''
#
# n, m = map(int, input().split())
# result = []
# for i in range(n):
#     result.append(input().split())
#
# index = m = 0
#
# for i, v in enumerate(result):
#     s = 0
#     for j in v:
#         for k in j:
#             if k.isdigit():
#                 s += 1
#     if m < s:
#         m = s
#         index = i
#
# print(index + 1, m)
# for i in result:
#     print(i)


# s = 'hello worldt728538'
# print(len([i for i in s if i.isdigit()]))
#
#
# print(sum(i.isdigit() for i in s))

# s = 'hello world123214'
# count = 0
#
# for i in s:
#     count += i.isdigit()
#
# print(count)
# print()

# n, m = map(int, input().split())
# result = []
# m = 0
# index = 0
# for i in range(n):
#     s = sum(map(len, input().split()))
#     if m < s:
#         m = s
#         index = i
#
# print(index + 1)

# matrix = [list(map(int, input().split())) for i in range(n)]
#
# columns = list(map(sum, zip(*matrix)))
#
# for row in matrix:
#     if sum(row) in columns:
#         print(True)
#         break
# else:
#     print(False)


'''
https://www.programiz.com/python-programming/list
https://www.programiz.com/python-programming/methods/list

https://www.programiz.com/python-programming/set
https://www.programiz.com/python-programming/methods/set

https://www.programiz.com/python-programming/string
https://www.programiz.com/python-programming/methods/string

https://www.programiz.com/python-programming/dictionary
https://www.programiz.com/python-programming/methods/dictionary

mutable(ozgaruvchi) - list, set, dict
immutable (ozgarmas) - int, float, bool, str, tuple
hashable - int, float, bool, str, tuple
unhashable - list, set, dict, tuple
iterable - list, str, tuple, dict, set
container - tuple, list, dict, set
sequence - list, str, dict, tuple

dict - keyi hashable, value esa ixtiyoriy boladi
set - ichidagi elementlar hashable bolishi kk

146-tadan 100tasi min



3 3
1 0 1
2 7 3
2 3 2
'''
# list, matrix, str, dict
# list, set, tuple
#

# matrix = [list(map(int, input().split())) for i in range(n)]
#
# # matrix = []
# # for i in range(n):
# #     matrix.append(list(map(int, input().split())))
#
#

'''
set
s1 = {1, 3, 2}
s2 = {1, 2, 3}
s1.intersection(s2)

print(s2.difference_update(s1))


.discard(8)
s.remove(8)


s = 'hello'
s = s + 'i'


a = [2]

a.extend()
a.append(2)

[2, 2]
'''
# for row in matrix:
#     print(row)
'''
3 4
6 2 7 8
2 4 5 7
8 3 1 9
'''

# a = []
# a = [
#     [6, 2, 7, 8],
#     [2, 4, 5, 7],
#     [8, 3, 1, 9]
# ]
#
#
# for i in zip(*a):
#     print(sum(i))
#

#
# print(list(map(int, l)))
# for i in map(int, l):
#     print(i, end=' ')

# for i, v in enumerate(l):
#     l[i] = int(l[i])
#
# print(l)

#
# a = [2, 3, 4, 5]
# b = [7, 2]
# c = [9, 1, 3]

# print(list(zip(a, b, c)))


# l = list(range(1, 50))
# print(l)

# a = [7, 2, 3, 5, 8, 1]
#
# for i in range(2, len(a), 2):
#     print(a[i])

#
# for index, value in enumerate(a, 1):
#     print(index, value)


# min, max, sum, zip, enumerate, range, len - builtin function

# a = [2, 3, 5]
#
# a.append(2)

'''
position based - orni boyicha
keyword based - kaliti boyicha
'''


# default
# a = 2
#
# def add(b, c):  # params
#     print(a)
#     return a + b + c
#
# print(add(1, c=3))  # argument

# separate_chars

# 'hello wor432ld'
# 'helloworld'


def separate_chars(s):
    result = ''
    for i in s:
        if i.isalpha():
            result += i

    return result


s = 'hello312'
print(separate_chars(s))
