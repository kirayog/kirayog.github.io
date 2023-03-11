n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = [a[i]+b[i] for i in range(n)]

ans = [False for _ in range(n)]

sortA = sorted(a, reverse=True)
sortB = sorted(b, reverse=True)
sortC = sorted(c, reverse=True)

count = 0
for i in range(n):
    if count == x:
        break
    for j in range(n):
        if a[j] == sortA[i] and ans[j] == False:
            count += 1
            ans[j] = True
            break
            
count = 0            
for i in range(n):
    if count == y:
        break
    for j in range(n):
        if b[j] == sortB[i] and ans[j] == False:
            count += 1
            ans[j] = True
            break

count = 0
for i in range(n):
    if count == z:
        break
    for j in range(n):
        if c[j] == sortC[i] and ans[j] == False:
            ans[j] = True
            count += 1
            break

for i in range(n):
    if ans[i] == True:
        print(i+1)
