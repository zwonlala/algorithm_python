# 송지원 python dict 정렬하는 법 
# - https://gomguard.tistory.com/127
dic = dict();
for i in range(8):
    # dic.append({i+1 : }int(input()));
    dic[i+1] = int(input());

# print(dic);

res = sorted(dic.items(), key= lambda x: x[1]);
# print(res);

# 송지원 python dict sum 정리
# - https://hello-bryan.tistory.com/46
score = sum(x[1] for x in res)

for i in range(3):
    score -= res[i][1]
    # 송지원 python list 제거하기 정리
    # - https://velog.io/@code_angler/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%9A%94%EC%86%8C-%EC%A0%9C%EA%B1%B0%ED%95%98%EA%B8%B0
print(score)

countedRes = sorted(res[3:], key= lambda x: x[0]);
# 송지원 python 배열을 문자열로
# - https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=complusblog&logNo=221158629508

y = [str(x[0]) for x in countedRes]
# print(y)
# print(len(y))
print(' '.join(y))
# print(', '.join([x[0] for x in countedRes]))