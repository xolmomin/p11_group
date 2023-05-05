# 45 - 30min
#
# from math import log, cos
#
# x, y = input().split()
# x, y = int(x), int(y)
#
# z = log(abs((x + y) ** 2 + (abs(y) + 2) ** (1 / 2) - (x - ((x * y) / ((x ** 2) / 2 - 5))))) + (
#         (cos(x + y) ** 2) / (x + y) ** (1 / 3))
# print(f'{z:.2f}')

# x, y, z = input().split()
# x, y, z = int(x), int(y), int(z)
#
#
# if x + z > y and :
#     print("Yes")
# else:
#     print("No")

# from math import sin, cos, sqrt, e
#
# a, x, y = input().split()
# a, x, y = int(a), float(x), float(y)
# TT = sqrt(y * 2 + e * x + sqrt(e * 2 + (a) / x * 2 + 2)) + cos(x) ** 2 / sin(x * x) + pow(cos(x), 3)
# print(f'{TT:.2f}')
#
# from math import sqrt
#
# a, b, c = input().split()
# a, b, c = float(a), float(b), float(c)
#
# d = b ** 2 - 4 * a * c
# if d > 0 and a != 0:
#     x1 = ((-1 * b) + sqrt(d)) / (2 * a)
#     x2 = ((-1 * b) - sqrt(d)) / (2 * a)
#     print(f'{x1:.2f} {x2:.2f}')
# elif d < 0:
#     print("No")

# from math import sqrt, tan, cos,sin
#
# x = float(input())
#
# AA = sqrt((2 * tan(x + 2) - cos(x + 2 ** x)) / (1 + cos(x + 2) ** 2)) + sin(x ** 2) / (x ** 2 + 3)
# print(f"{AA:.2f}")

# from math import cos
#
# a, b, c, d, x = input().split()
# a, b, c, d, x = int(a), int(b), int(c), int(d), float(x)
#
# if a == 0 and b - c < 0:
#     y1 = 0
# else:
#     y1 = (a * x * x + b * x + c) / (x * a ** 3 + a * a + a ** (b - c))
#
# y2 = cos(abs((a * x + b) / (c * x + d + 2 ** c)))
# s = y2 + y1
#
# print(f'{s:.2f}')
#
#
# from math import sqrt, exp, sin, log
#
# a, x, y = input().split()
# a, x, y, = int(a), float(x), float(y)
#
# w2 = sqrt(exp(x * y) - x * sin(a * x) - (x * x + 2) / (abs(x) + 5)) \
#      + sqrt(log(x * x + 2) + 5)
#
# print(f'{w2:.2f}')
# from math import factorial
#
# n = int(input())
#
# S = 0
#
# for i in range(1, n + 1):
#     S += (-1) ** (i - 1) / factorial(2 * i - 1)
#
# print(f'{S:.4f}')
#
# # 61, 62, 64
#
# # 68-misol
# from math import factorial
#
# n, x = input().split()
# n, x = int(n), int(x)
#
# S = 0
#
# for i in range(1, n + 1):
#     S += x ** i / factorial(i)
#
# print(f'{S:.3f}')
# # 79 - misol
# from math import cos, pi
# a = int(input())
# x = - pi / 2
# h = pi / 19
#
# S = 0
# while x <= pi:
#     S += a ** (a / 3) + x * x * cos(a * x)
#     x += h
#
# print(f'{S:.2f}')
# 80, 81, 82
# a = 1.5
# b = 6
# step = 1.5
# while a <= b:
#     print(a, end=' ')
#     a += step
#
# h = 'hello'
# print(h.count('l'))
# 96-misol
#
# from math import log
#
# x, y, c, d = map(int, input().split())
#
# S = 0
# for k in range(1, x + 1):
#     S += (-1) ** k * (k + 1) / (k ** 3 + k ** 2 + 1)
#
# P = 1
# for i in range(1, y + 1):
#     P *= (i ** 3 + abs(i - 9)) / (log(i) + 7 * i)
#
# SP = 1
# for n in range(1, c + 1):
#     _SP = 0
#     for m in range(1, d + 1):
#         _SP += (-1) ** m * log(m + 5) / (m ** (n + 3) + n * m)
#     SP *= _SP
#
# print(f'{S:.2f} {P:.2f} {SP:.2f}')
# 98, 99
# from math import e, sqrt
#
# x, y, c, d = map(int, input().split())
#
# s = 0
# for k in range(1, x + 1):
#     s += k ** 3 + e ** k
#
# p = 1
# for a in range(3, y + 1):
#     p *= a * x / sqrt(a ** 2 + x ** 2)
#
# sp = 0
# for i in range(1, c + 1):
#     _sp = 1
#     for j in range(1, d + 1):
#         _sp *= (i * x + j ** 2) / sqrt(i ** 2 + j * y)
#     sp += _sp
#
# print(f'{s:.2f} {p:.2f} {sp:.2f}')

# from math import sin, cos
#
# import math as m  # alias
#
# m.cos()
# m.log()

# a = [23, 6, 2, -5, 8, 20]
# sum, min, max, len, print, range, enumerate
# built-in function

# print(min(a))
# minimal = a[0]
#
# for i in a:
#     if i < minimal:
#         minimal = i

# print(minimal)

# int = 2
#
# print(int)
#
# s = '12'
#
# print(int(s))


# iterable - list, str, tuple, dict, set
# container - tuple, list, dict, set
# sequence - list, str, dict, tuple

# a = [2, 3, 4, 5]
#
# a[2]

# import keyword
#
# print(keyword.kwlist)

