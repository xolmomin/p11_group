# def rec(s: str):
#     if s:
#         return rec(s[1:]) + s[0]
#     return ''
#
# s = '123456'
# print(rec(s))
#

# print(''.join(reversed(s)))


# # v1
# def split(s, c: int = 1):
#     if len(s) <= c:
#         return s + '0' * (c - len(s))
#     return s[:c] + ' ' + split(s[c:], c + 1)
#
# s = '1234'
#
# result = split(s)
# print(result)


# # v2
# s = '1234'
# result = ''
# c = 1
# while len(s) >= c:
#     result += s[:c] + ' '
#     s = s[c:]
#     c += 1
# result += s + '0' * (c - len(s))
# print(result)


# # 1 23 456 7000

# waaBaAbTe
# aaBaAb
# Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"











