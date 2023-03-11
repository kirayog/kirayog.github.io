n = int(input())

dp = [[0 for _ in range(5)] for _ in range(10**6)]
dp[0] = [1 for _ in range(5)]
mod = 998244353

for i in range(1, n):
    for j in range(5):
        if j == 0:
            dp[i][j] = (dp[i-1][j] + dp[i-1][j+1]) % mod
        elif j == 4:
            dp[i][j] = (dp[i-1][j-1]*2 + dp[i-1][j]) % mod
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]) % mod

ans = ((dp[n-1][0] + dp[n-1][1] + dp[n-1][2] + dp[n-1][3])*2 + dp[n-1][4]) % mod
print(ans)
