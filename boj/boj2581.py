def isPrime(num):
    if (num == 1):
        return False
    for i in range(2, int(num**0.5) + 1):
        if (num % i == 0):
            return False
    return True


m = int(input())
n = int(input())
primeList = []
for i in range(m, n+1):
    if isPrime(i):
        primeList.append(i)
# print(primeList)
if (len(primeList) == 0):
    print(-1)
else :
    print(sum(primeList), primeList[0], sep='\n')