bug = []
dri = []
for _ in range(3):
    bug.append(int(input()))
for _ in range(2):
    dri.append(int(input()))
print(min(bug) + min(dri) - 50)