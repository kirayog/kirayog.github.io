n, w = map(int, input().split())

dp = [[0 for _ in range(w+1)] for _ in range(n+1)]

for i in range(1, n+1):
    tmpW, tmpV = map(int, input().split())
    for j in range(1, w+1):
        if j-tmpW >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-tmpW] + tmpV)
        else:
            dp[i][j] = dp[i-1][j]
        
print(dp[-1][-1])
