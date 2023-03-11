n, q = list(map(int, input().split()))
a = list(map(int, input().split()))
xk = [list(map(int, input().split())) for _ in range(q)]
d = {}

for i in range(n):
    if a[i] not in d: d[a[i]] = [i]
    else: d[a[i]].append(i)

for i in range(q):
    if xk[i][0] in d and len(d[xk[i][0]]) > xk[i][1]-1:
        print(d[xk[i][0]][xk[i][1]-1] + 1)
    else:
        print(-1)
