'''
6 6
-50 53 53 54 67 -8
41 -77 57 -54 43 -59
-94 47 36 8 92 -8
51 -5 55 -57 20 -34
-36 71 42 18 53 -80
69 -62 16 -94 64 -16   (-23)

169 -49 81 30 68 -23
92 -94
'''

# # v1
# n, m = map(int, input().split())
#
# result = []
# minn = float('inf')
# maxx = float('-inf')
#
# for i in range(n):
#     l = list(map(int, input().split()))
#     minn = min(min(l), minn)
#     maxx = max(max(l), maxx)
#     result.append(sum(l))
#
# print(result)
# print(maxx, minn)

# # v2
# n, m = map(int, input().split())
#
# list_ = []
# result = []
# for i in range(n):
#     l = list(map(int, input().split()))
#     result.append(sum(l))
#     list_.extend(l)
#
# print(result)
# print(max(list_), min(list_))


# lambda, filter
# '''
# Doston
# 6
# '''
#
# s = input()
# a, b = map(int, input().split())
# a, b = a - 1, b - 1
# '''
# doston
# 4 1
# '''
# if a > b:
#     if b == 0:
#         s = s[a:: -1]
#     else:
#         s = s[a:b - 1: -1]
# else:
#     s = s[a:b + 1]
#
# s = s[a:: -1] if b == 0 else s[a:b - 1: -1] if a > b else s[a:b + 1]
#
# print(s)
# list, tuple, set
#
# str
# s = [2, 4, 5, [3, 4, 5]]
# h =
# s = 'hello'
# s = 'hello' + '1'


# def add(a, b):
#     print(a + b)
#
#     #
#     # return None
#     # return
#
# print(add(5, 6))
# anonymous function


# def add(a, b):
#     # for
#     # while
#     # if
#     return a + b
#
# s = '2 3 4 5 6 7'
# l = [2, 3.0, 4, 5.0, 6, 7.0]
#
# # toq bolsa int
# # juft float
#
# l = list(map(lambda a: int(a) + 2, s.split()))
# print(l)
# s = '2 3 4 5 6 7'
# l = list(map(lambda a: int(a) if int(a) % 2 else float(a), s.split()))
# l = list(map(lambda a: int(a) if int(a) & 1 else float(a), s.split()))
# print(l)

# map, zip, enumerate, range, filter

# s = '2.23 3 4.2 5 6 7'
# s = [2.23, 3, 4.2, 6, 7]
'''
agar 5 ❌
2.23
2
'''
toq = list(filter(lambda a: int(a) & 1, s.split()))
juft = list(filter(lambda a: not int(a) & 1, s.split()))
print(juft)
print(toq)

# map(int, s.split())

# print(add(3, 4))
# print((lambda a, b: a + b)(3, 4))


'''


'''
