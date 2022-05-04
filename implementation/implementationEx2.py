def secToHour(time):
    return time//60//60 * 10000 + time//60%60 * 100 + time%60

def hasThree(number):
    # index = [str(number)].index('3')
    # return index != -1
    return '3' in str(number)

n = int(input())
max = n * 3600 + 59 * 60 + 59

count = 0
for i in range(max):
    hour = secToHour(i)
    if hasThree(hour):
        count += 1

print(count)


# book version

h = int(input())

count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)