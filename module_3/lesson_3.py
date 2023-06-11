# mat = [
#     [1, 2, 3, 1],
#     [4, 5, 6, 1],
#     [7, 8, 9, 1],
#     [7, 8, 9, 1]
# ]
#
# result = sum(mat[0] + mat[-1]) + sum(map(lambda row: row[0] + row[-1], mat[1:-1]))
# print(result)
#
#
#
# summa = 0
# for i in range(len(mat)):
#     summa += mat[i][i] + mat[i][len(mat) - i - 1]
#
# print(summa - len(mat) % 2 * mat[len(mat) // 2][len(mat) // 2])
from collections import Counter
from turtle import down

#
# summa = sum(mat[i][i] + mat[i][len(mat) - i - 1] for i in range(len(mat))) - len(mat) % 2 * mat[len(mat) // 2][
#     len(mat) // 2]
#
# print(summa)
#
# board = [
#     [".", ".", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", "p", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", "p"],
#     ["p", ".", ".", "R", ".", ".", "p", "."],
#     [".", ".", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", "p", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", "."]
# ]
#
# for i in range(8):
#     is_find = False
#     for j in range(8):
#         if board[i][j] == 'R':
#             is_find = True
#             break
#     if is_find:
#         break
#
# summa = 0
#
# for k in range(j - 1, -1, -1):  # chapga
#     if board[i][k] == 'p':
#         summa += 1
#         break
#     if board[i][k] != '.':
#         break
#
# for k in range(j + 1, 8):  # ongga
#     if board[i][k] == 'p':
#         summa += 1
#         break
#     if board[i][k] != '.':
#         break
#
# for k in range(i + 1, 8):  # pastga
#     if board[k][j] == 'p':
#         summa += 1
#         break
#     if board[k][j] != '.':
#         break
#
# for k in range(i - 1, -1, -1):  # tepaga
#     if board[k][j] == 'p':
#         summa += 1
#         break
#     if board[k][j] != '.':
#         break
#
# print(summa)


# mat = [
#     [1, 1, 0, 0, 0],
#     [1, 1, 1, 1, 0],
#     [1, 0, 0, 0, 0],
#     [1, 1, 0, 0, 0],
#     [1, 1, 1, 1, 1]
# ]
#
# k = 3
# s = map(lambda i: i[0], sorted(enumerate(map(sum, mat)), key=lambda i: i[1])[:k])
# print(list(s))
#
# s = sorted(range(len(mat)), key=lambda x: sum(mat[x]))[:k]
# print(s)


# for i in range(len(matrix) - 1):
#     if matrix[i][:-1] != matrix[i + 1][1:]:
#         return False
# return True


# for i in range(1, len(matrix)):
#     for j in range(1, len(matrix)):
#         if matrix[i][j] != matrix[i - 1][j - 1]:
#             print(False)
# print(True)
