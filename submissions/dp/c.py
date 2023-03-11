n = int(input())
dp = [[0, 0, 0] for _ in range(n+1)]

for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    for j in range(3):
        dp[i][j] = max(dp[i-1][(j-1)%3], dp[i-1][(j+1)%3]) + tmp[j]
        
print(max(dp[-1]))
