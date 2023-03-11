N, X = map(int, input().split())
dp = [[0 for _ in range(X+1)] for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    a, b = map(int, input().split())
    for j in range(X+1):
        if dp[i-1][j] == 1:
            if X >= j+a: dp[i][j+a] = 1
            if X >= j+b: dp[i][j+b] = 1

print("Yes" if dp[-1][-1] == 1 else "No")
