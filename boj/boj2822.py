# arr = map(int, input().split())
dic = dict();
for i in range(8):
    # dic.append({i+1 : }int(input()));
    dic[i+1] = int(input());

# print(dic);

sorted(dic, key= lambda x: x[1]);
print(dic);
