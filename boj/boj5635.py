import datetime;

t = int(input())
dic = dict();
for _ in range(t):
    name, d, m, y = input().split()
    bd = datetime.date(int(y), int(m), int(d))
    dic[bd] = name

res = sorted(dic.keys())
print(dic[res[-1]], dic[res[0]], sep='\n');