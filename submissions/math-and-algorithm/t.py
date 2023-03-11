n = int(input())
a = list(map(int, input().split()))
dp = [[[0, 0, 0, 0, 0, 0] for _ in range(1000+1)] for _ in range(n+1)]
dp[0][0][0] = 1

for i in range(1, n+1):
    for j in range(1000+1):
        for k in range(6):
            if j-a[i-1] < 0 or k < 1:
                dp[i][j][k] = dp[i-1][j][k]
            else:
                dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-a[i-1]][k-1]

print(dp[-1][-1][-1])
