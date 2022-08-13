N = int(input())
student = []

for _ in range(N):
    name, score = input().split()
    student.append((name, int(score)))

# print(student)
# sorted(student, key= lambda x: x[1], reverse=True)
# sorted(student, key= lambda x: x[1])
student.sort(key= lambda x: x[1])

print(" ".join(map(lambda x: x[0], student)))