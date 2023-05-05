matrix = [
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4]
]

# 1, 1, 1, 1
# 2, 2, 2, 2
# 3, 3, 3, 3
# 4, 4, 4, 4


'''

n sonini 1ta raqamini ochirish orqali eng kichik songa aylantirish kk
n = 311615

n sonini 2ta raqamini ochirish orqali eng kichik songa aylantirish kk
n = 311615

n sonini 3ta raqamini ochirish orqali eng kichik songa aylantirish kk
n = 311615

'''

#
# def solve(n, k):
#     i = 1
#     while k:
#         if n[i - 1] > n[i]:
#             n = n[:i - 1] + n[i:]
#             k -= 1
#             i -= 1
#             n = n.lstrip('0')
#             if len(n) <= i and not n:
#                 break
#         else:
#             i += 1
#     n = n.lstrip('0')
#     if not n:
#         return '0'
#     return n[:-k] if k else n
#
#
# k = 1
# n = '112'
#
# print(solve(n, k))


# def rec(s):
#     l = s.find('[')
#     if not ~l:
#         return s
#     print(s)
#     for i in range(len(s)):
#         if s[i].isdigit():
#             break
#     return s[:i] + int(s[i:l]) * rec(s[l + 1:s.rfind(']')])
#
#
#
# s = "3[a]2[bc]"
# result = ''
#
# n = -1
#
# # while (l := s.find('[')) != -1:
# while ~(l := s.find('[')):
#     n = 1
#     if s[:l]:
#         n = int(s[:l])
#     result += n * s[l + 1:s.find(']')]
#     s = s[s.find(']') + 1:]
#
# print(result + s)
#
# def rec(s):
#     p = s.find('[')
#     if p == -1:
#         return s
#     fi = ''
#     for i in s:
#         if i.isdigit():
#             break
#         else:
#             fi += i
#     return fi + int(s.lstrip(fi).split('[', 1)[0]) * rec(''.join(s.split('[', 1)[1].rsplit(']', 1)))
#
#
# if __name__ == '__main__':
#     print(rec(a))

