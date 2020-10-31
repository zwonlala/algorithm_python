N = int(input())
times = list(map(int, input().split()))
times.sort()

ANS = 0;
for i in range(N):
    ANS += (N-i) * times[i]

print(ANS)