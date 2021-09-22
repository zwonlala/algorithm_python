t = int(input())
for _ in range(t):
    n = int(input())
    dict = {}
    for _ in range(n):
        key, value = input().split()
        dict[int(key)] = value
    # print(dict)
    max_key = max(dict.keys())
    # print("//" , max_key)
    print(dict[max_key])