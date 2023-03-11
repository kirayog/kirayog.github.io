n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
x = int(input())

dp = [0 for i in range(x+1)]
dp[0] = 1

for i in range(m):
    dp[b[i]] = -1
    
for i in range(x):
    if dp[i] != 1: continue
    for j in range(n):
        if i+a[j] < x+1 and dp[i+a[j]] == 0:
            dp[i+a[j]] = 1

if dp[-1] == 1:
    print("Yes")
else:
    print("No")
