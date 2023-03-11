n = int(input())
a = list(map(int, input().split()))

ans = [0 for _ in range(n)]
a.sort()

count = 0
tmp = -1
ansCount = 0
for i in range(n):
    if tmp == -1:
        tmp = a[n-i-1]
        count+=1
    elif tmp == a[n-i-1]:
        count+=1
    else:
        ans[ansCount] = count
        ansCount+=1
        tmp = a[n-i-1]
        count = 1
        
ans[ansCount] = count

for i in range(n):
    print(ans[i])
