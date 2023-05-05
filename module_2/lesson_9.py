# # CustomList
# # append, append_left, append_middle
# #
# # a.append_left(6)
# #
# #
# # class CustomList(list):
# #     def append_left(self, n):
# #         # self[:] = [n] + self
# #         self.insert(0, n)
# #
# #     def append_middle(self, n):
# #         self.insert(len(self) // 2, n)
# #
# #
# # a = [2, 3, 4, 5, 6]
# # l = CustomList(a)
# #
# # l.append_left(9)
# # l.append_middle(55)
# # # l.pop(6)
# # print(l)
# #
# #
# # a = [
# #     ((False, False, False), False, 'h'),
# # ]
# #
# # a.sort()
# # for i in a:
# #     print(i)
#
# # l = [1, 6, 2, 4, 6, 7, 9]
# # l.sort(key=lambda i: (i & 1, i))
# # print(l)
#
# #
# # s = 'helloworlda736289'
# # vowels = 'auoie'
# # s = ''.join(
# #     sorted(s,
# #            key=lambda i: (
# #                (i.isdigit(), i.isdigit() and not int(i) & 1, i.isdigit() and (-int(i) if not int(i) & 1 else int(i))),
# #                i in vowels,
# #                -ord(i) if i in vowels else i
# #            )
# #            )
# # )
# #
#
# # print(s)
#
# # dhlllrwooea379862
# # dhlllrwooea379862
#
# # s = ''.join(sorted(s, key=lambda i: (i not in 'aioeu', i)))
# # print(s)
#
# # a = [7, 3, 6, 2, 8, 9]
# # 8 6 2 3 7 9
# # a.sort(key=lambda i: (i & 1, i if i & 1 else -i))
# # print(a)
#
#
# # nested list
# # a = [2, 3, [3], [3], [5, [2]]]                #    -> 3
#
# # # v1
# # a = str(a)
# #
# # max_level = 0
# # count = 0
# # for i in a:
# #     if i == '[':
# #         count += 1
# #     elif i == ']':
# #         count -= 1
# #     if count > max_level:
# #         max_level = count
# #
# # print(max_level)
#
#
# # # v2
# # a = [2, 0, [], 1, [2, [2, 3, 5, [3], 2]], 4, 5]  # -> 4
#
# # v2.1
# # def max_level(l):
# #     if type(l) == list:
# #         return 1 + max([max_level(i) for i in l], default=0)
# #     return 0
#
# # v2.2
# # def max_level(l):
# #     return 1 + max([max_level(i) if isinstance(i, list) else 0 for i in l], default=0)
# #
# #
# # print(max_level(a))
#
#
#
#
# '''
# joriy faylning yonidagi fayl nomlaridagi eng kop unli harf ishlatilgan
# faylning ichidagi eng kop uchragan 5ta belgi
#
# '''
#
# import os
# from collections import Counter
#
# max_count = 0
# filename = ''
# for i in os.listdir():
#     n = sum(map(lambda x: x in 'auoie', i))
#     if n > max_count:
#         max_count = n
#         filename = i
#
# with open(filename) as f:
#     data = f.read()
#     result = Counter(data).most_common(5)
#     print(filename)
#     print(*result)


a = ('1', '2')

d = {}
t = d.fromkeys(('name', 'value'), a)
print(t)