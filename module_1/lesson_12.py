# s = '((())())()())('
#
# while s.find('()') != -1:
#     s = s.replace('()', '')
#
# if s == '':
#     print('Togri qavs')
# else:
#     print('Notogri qavs')
#

# )
# task = '((a)(bd))(fds(f2f(3)f))' # togri
#
# s = '())'
# stack = []
#
# for i in s:
#     if i == '(':
#         stack.append(i)
#     elif len(stack) and stack[-1] == '(':
#         stack.pop()
#     else:
#         stack.append(i)
#
# if len(stack):
#     print('Notogri qavs')
# else:
#     print('Togri qavs')

# task = '((a)(bd))(fds(f2f(3)f))'
# stack = []

# for i in task:
#     if i.isalpha() or i.isdigit():
#         continue
#     elif i == '(':
#         stack.append(i)
#     elif len(stack) and stack[-1] == '(':
#         stack.pop()
#     else:
#         stack.append(i)
#
# print("Wrong" if len(stack) else "True")
# print(('True', 'Wrong')[bool(stack)])
# print(('Wrong', 'True')[not stack])
#
# task = ')()'
# stack = []
#
# for i in task:
#     if i not in '()':
#         continue
#     if i == '(':
#         stack.append('(')
#     elif i == ')' and len(stack):
#         stack.pop()
#     else:
#         stack.append(i)
# print(not bool(stack))
#
# s = '(()[()])'
# stack = []
#
# for i in s:
#     if i in '([{':
#         stack.append(i)
#     elif len(stack) and (
#             stack[-1] == '(' and i == ')' or
#             stack[-1] == '[' and i == ']' or
#             stack[-1] == '{' and i == '}'):
#         stack.pop()
#     else:
#         stack.append(i)
#
# print(not stack)
# 3
#

# s = "abbaca"
#
# stack = []
#
# for i in s:
#     if len(stack) and stack[-1] == i:
#         stack.pop()
#     else:
#         stack.append(i)
#
# print(''.join(stack))


# s = "lEeeetcode"


