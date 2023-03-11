n = int(input())

dic = {}
stArray = []

for i in range(n):
    s, t = input().split()
    t = int(t)
    if s not in dic:
        dic[s] = 1
        stArray.append([s, t, i])

max = -1
ans = -1
for i in range(len(stArray)):
    if max < stArray[i][1]:
        max = stArray[i][1]
        ans = stArray[i][2]+1
        
print(ans)
