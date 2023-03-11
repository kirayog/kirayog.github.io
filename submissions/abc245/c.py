n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

flag = [[False, False] for _ in range(n)]
flag[0] = [True, True]

for i in range(1, n):
    if flag[i-1][0] == True:
        if abs(a[i-1]-a[i]) <= k:
            flag[i][0] = True
        if abs(a[i-1]-b[i]) <= k:
            flag[i][1] = True
    if flag[i-1][1] == True:
        if abs(b[i-1]-a[i]) <= k:
            flag[i][0] = True
        if abs(b[i-1]-b[i]) <= k:
            flag[i][1] = True

if flag[-1][0] == True or flag[-1][1] == True:
    print("Yes")
else:
    print("No")
