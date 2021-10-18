t = int(input())
for _ in range(t):
    idx_str, str = input().split()
    idx = int(idx_str)
    print(str[0: idx-1], str[idx:], sep='')

# 더 줄이거나 pythonic 하게 짤 순 없는지...?