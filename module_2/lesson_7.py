# # nxn
#
#
# # [0, 0, 0, 0, 0, 0],
# # [0, 1, 2, 3, 4, 0],
# # [0, 6, 1, 3, 4, 0],
# # [0, 2, 2, 9, 4, 0],
# # [0, 3, 2, 3, 1, 0],
# # [0, 0, 0, 0, 0, 0],
# #
# # matrix = [
# #     [1, 2, 3, 4],
# #     [6, 7, 3, 8],
# #     [8, 2, 9, 9],
# #     [3, 2, 3, 2],
# # ]
# # from itertools import chain
# # from math import sqrt, ceil
# #
# # l = list(filter(lambda x: x % 2, chain(*matrix)))
# # n = ceil(sqrt(len(l)))
# # l += [0] * (n ** 2 - len(l))
# #
# # matrix = [l[i: i + n] for i in range(0, len(l), n)]
# #
# # for row in matrix:
# #     print(row)
#
# # 1, 3, 7
# # 3, 9, 3
# # 3, 1, 0
# '''
#
# 1 2 3 4
# 6 7 3 8
# 8 2 9 9
# 3 2 3 2
#
# 1 6 8 3 2 3 4 8 9 2
# '''
#
# matrix = [
#     [1, 2, 3, 4],
#     [6, 7, 3, 8],
#     [8, 2, 9, 9],
#     [3, 2, 3, 2],
# ]
# n = len(matrix)
# for i in matrix:
#     print(i)
#
# # v0
# list_ = []
# s = len(matrix)
# for i, v in enumerate(zip(*matrix)):
#     s -= 1
#     for j in range(len(v)):
#         if i == 0 or i == len(v) - 1 or s == j:
#             list_.append(v[j])
# print(list_)
#
# # list_ = []
# # s = len(matrix)
# # v1
# # for i, v in enumerate(zip(*matrix)):
# #     for j in range(len(v)):
# #         if i == 0 or i == len(v) - 1 or s - i  - 1 == j:
# #             list_.append(v[j])
#
# # v2
# s = len(matrix)
# list_ = [v[j]
#          for i, v in enumerate(zip(*matrix))
#          for j in range(len(v))
#          if not i or i == len(v) - 1 or s - i - 1 == j]
#
# print(list_)
#
# #
# # l = len(matrix)
# # matrix = [[0] * l] + matrix + [[0] * l]
# # for row in matrix:
# #     row.append(0)
# #     row.insert(0, 0)
# #
# # for i in matrix:
# #     print(i)

