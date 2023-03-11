n, s = map(int, input().split())
a = list(map(int, input().split()))

dp = [[0 for _ in range(s+1)] for _ in range(n+1)]
dp[0][0] = 1

for i in range(1, n+1):
    for j in range(s+1):
        dp[i][j] += dp[i-1][j]
        if j-a[i-1] >= 0:
            dp[i][j] += dp[i-1][j-a[i-1]]
            
print("Yes" if dp[-1][-1] > 0 else "No")
