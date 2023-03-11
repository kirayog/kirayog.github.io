n, m = map(int, input().split())
a = list(map(int, input().split()))

dp = [[0 for _ in range(m+1)] for _ in range(n)]
check = [[False for _ in range(m+1)] for _ in range(n)]#dpの値が一度でも更新されたらTrueにする

dp[0][1] = a[0]
check[0][1] = True

for i in range(n-1):
    for j in range(m+1):
        if i < j-1:
            continue
        if j != m:
            if check[i+1][j+1] == False:
                dp[i+1][j+1] = dp[i][j]+a[i+1]*(j+1)
                check[i+1][j+1] = True
            else:
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+a[i+1]*(j+1))
                
        if check[i+1][j] == False:
            dp[i+1][j] = dp[i][j]
            check[i+1][j] = True
        else:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])

print(dp[-1][-1])
