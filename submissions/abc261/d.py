n, m = map(int, input().split())
x = list(map(int, input().split()))

dic = {}
dp = [[-1 for _ in range(n+1)] for _ in range(n)]
for i in range(m):
    c, y = map(int, input().split())
    dic[c] = y
    
dp[0][0] = 0
dp[0][1] = x[0]
if 1 in dic:
    dp[0][1] += dic[1]

for i in range(n-1):
    for j in range(n):
        if dp[i][j] != -1:
            dp[i+1][0] = max(dp[i+1][0], dp[i][j])
            dp[i+1][j+1] = dp[i][j] + x[i+1]
            if j+1 in dic:
                dp[i+1][j+1] += dic[j+1]
                
print(max(dp[-1]))
