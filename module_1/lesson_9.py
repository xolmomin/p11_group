# t = 26, 7, 4, 5
# l = [8, 4, 2, 9]
# s = {8, 32, 5, 7, 2}
# d = {6: 8, 5: 4, 3: 9, 2: 8}  # key
# s = 'hello world 51235'
#
# print(sorted(t))  # tuple
# print(sorted(l))  # list
# print(''.join(sorted(s)))  # str
#
# print(sorted(s))  # set
# print(sorted(d.items()))  # dict
# print(sorted(d.items(), key=lambda i: i[1]))  # dict
#
# dd = dict([(5, 4), (6, 8), (2, 8), (3, 9)])
# print(dd)


# 10:30
# 1) odd(toq), even(juft) - 10-min
# 3 7 7 2 6 8

# a = [8, 2, 7, 7, 3, 6, 6, 6, 2, 2, 2]
# a = [7, 4, 2, 5, 7, 6, 9, 3]
#
# a.sort(key=lambda i: (i % 2 == 0, i))
# print(a)


# 2) top 3 - 5-min
# 2 6 7

# # 1-version
# a = [8, 2, 7, 7, 3, 6, 6, 6, 2, 2, 2]
# from collections import Counter
# print(*dict(Counter(a).most_common(3)).keys())


# # 2-version
# a = [8, 2, 7, 7, 3, 6, 6, 6, 2, 2, 2]
# d = {}
#
# for i in a:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1
#
# d = sorted(d.items(), key=lambda i: i[1])[-3:]
# d = dict(d)
# print(*d.keys())


# # 3-version
# a = [8, 2, 7, 7, 3, 6, 6, 6, 2, 2, 2]
# d = {}
#
# for i in a:
#     d[i] = d.get(i, 0) + 1
#     #
#     # if i in d.keys():
#     #     d[i] = d[i] + 1
#     # else:
#     #     d[i] = 0 + 1
#
# d = sorted(d.items(), key=lambda i: i[1])[-3:]
# d = dict(d)
# print(*d.keys())

# ll = [
#      (True, 8),
#      (True, 6),
#      (False, 7),
#      (True, 6),
#      (True, 4),
#      (False, 3),
#      (True, 2),
# ]
# ll.sort()
# for i in ll:
#      print(i)

# l = [
#      # (8, 6, 3),
#      # (2, 3, 7),
#      # (8, 2, 8),
#      # (5, 6, 2),
#      # (8, 4, 6),
#      # (5, 7, 9)
# ]
# # l.sort()
# # for i in l:
# #     print(i)
# #
# l.sort(key=lambda i: (i % 2 == 0, i))
# print(l)

# a = [7, 4, 2, 5, 1, 6, 9, 3]
# a.sort(key=lambda i: (not i & 1, i if i & 1 else -i))
# print(a)
# toq osuvchi, juft kamayuvchi
# 1 3 5 7 9 6 4 2

# # 2)
# l = ['name', 'hello', 'word', 'list', 'tuple', 'valijon', 'alijon', 'python']
# # uoaie, length
# l.sort(key=lambda word: (sum(i in 'uoaie' for i in word), len(word)))
# print(l)
#
# # 3)
# d = {
#     'key1': 'botirjon',
#     'key2': 'valijon',
#     'key3': 'toshmat',
#     'key4': 'eshmat',
#     'key5': 'botirjon 2'
# }
#
# d = sorted(d.items(), key=lambda i: -len(i[1]))
# print(dict(d))

# # 4)
# a = [7, 4, 2, 5, 1, 6, 9, 3, 8]
# 6 kichiklar sonlar kamayuvchi, juft osuvchi, toq kamayuvchi
# 5 4 3 2 1 6 8 9 7

