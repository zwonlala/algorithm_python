n = int(input())
printStr = '* ' * n
for i in range(n):
    # print(printStr if i%2 == 0 else ' ' + printStr)
    print('' if i%2 == 0 else ' ', printStr, sep = '')