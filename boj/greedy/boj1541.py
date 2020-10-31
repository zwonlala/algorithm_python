# # <Runtime Error 난 코드>
# expression = input()
#
# for i in range(len(expression)):
#     ch = expression[i]
#     if (ch == '-'):
#         expression = expression[:i]+ '-' + '(' + expression[i+1:]
#         # print(expression)
#
# reverse = expression[::-1]
#
# for i in range(len(reverse)):
#     ch = reverse[i]
#     if (ch == '-'):
#         reverse = reverse[:i]+ '-' + ')' + reverse[i+1:]
#         # print(reverse)
#
# expression = reverse[::-1]
#
# expression = '(' + expression + ')'
#
# # print(expression)
# print(eval(expression))
