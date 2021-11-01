getDiv = lambda x: int(x) % 42;
li = [];

# 여기 입력을 list comprehension을 사용하여 입력받는 방법이 있나..?
for _ in range(10):
    li.append(getDiv(input()));
print(len(list(set(li))));

# 집합 set의 원소 개수 구하는 법 -> len()