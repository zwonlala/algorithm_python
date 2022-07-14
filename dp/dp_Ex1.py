INF = int(1e9)
X = int(input())

arr = [0] * 30001

def calc(n):
    if n == 1:
        arr[n] = 0
        return

    arr[n] = INF
    if n % 5 == 0 :
        arr[n] = min(arr[n], arr[n//5] + 1)
    if n % 3 == 0:
        arr[n] = min(arr[n], arr[n//3] + 1)
    if n % 2 == 0:
        arr[n] = min(arr[n], arr[n//2] + 1)
    
    arr[n] = min(arr[n], arr[n-1] + 1)

for i in range(1, X + 1):
    calc(i)

print(arr[X])
print(arr)
    
