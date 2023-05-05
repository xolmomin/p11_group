# def merge(a, b):
#     l = []
#     while a and b:
#         l.append(a.pop(0) if a[0] < b[0] else b.pop(0))
#     return l + a + b
#
#
# a = [1, 2, 4, 4]
# b = [0]
#
# result = merge(a, b)
# print(result)

time = '?3:59'
hour, minute = time.split(':')


'''

2. merge two sorted list
a = [1, 2, 4, 4]
b = [2, 4, 5]

c = [1, 2, 2, 4, 4, 4, 5]

https://leetcode.com/problems/summary-ranges/
https://leetcode.com/problems/contains-duplicate-ii/

'''

# from collections import Counter
#
#
# def solve(s, goal):
#     if len(s) != len(goal):
#         return False
#     if len(set(s)) < len(s) and s == goal:
#         return True
#
#     t = ['cb', 'cd']
#     for a, b in zip(s, goal):
#         if a != b:
#             t.append(a + b)
#         if len(t) > 2:
#             return False
#
#     return len(t) == 2 and t[0] == t[1][::-1]
#
# '''
# acd
# abc
# '''
#
# s = "acd"
# goal = "abc"
# print(solve(s, goal))

# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
#
# # 1) variant
#
# nums = [0, 1, 2, 4, 5, 7]
# last = 0
# result = []
# for i in range(len(nums)):
#     if i + 1 == len(nums) or nums[i] + 1 != nums[i + 1]:
#         if last == i:
#             result.append(f'{nums[i]}')
#         else:
#             result.append(f'{last}->{nums[i]}')
#         last = i + 1
#
# print(result)
#
# # 2) variant
#
# nums = [0, 1, 2, 4, 5, 7]
# last = 0
# result = []
# for i in range(len(nums)):
#     if i + 1 == len(nums) or nums[i] + 1 != nums[i + 1]:
#         s = (f'{last}->', '')[last == i] + f'{nums[i]}'
#         result.append(s)
#         last = i + 1
#
# print(result)


# for i in range(1, len(nums)):
#     if nums[i - 1] != nums[i]:


# from itertools import groupby
#
# s = 'helllllo  worrrld'
#
# print(map(len, s))
# a = [2, 3, 4]
# l = []
# for k, v in groupby(s):
#     # ['h']
#     print(list(v), '--------', list(v))
#     # l.append((k, v))


# l = []
# for k, v in groupby(s):
#     l.append(len(list(v)))
#     # print(k, len(list(v)))
#
# print(max(l))

# l = (len(list(v)) for k, v in groupby(s))
# print(max(l))
#

# l = [(k, len(list(v))) for k, v in groupby(s)]
# print(*max(l, key=lambda i: i[1]))
