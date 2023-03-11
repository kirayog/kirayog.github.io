n, m, k, s, t, x = map(int, input().split())
MOD = 998244353

array = [[] for _ in range(n)]
dp = [[[0, 0] for _ in range(n)] for _ in range(k+1)] #[k‚ğ‹ô”‰ñ’Ê‚Á‚½, k‚ğŠï”‰ñ’Ê‚Á‚½]
dp[0][s-1][0] = 1

for i in range(m):
    u, v = map(int, input().split())
    array[u-1].append(v-1)
    array[v-1].append(u-1)
    
for i in range(1, k+1):
    for j in range(n):
        for k in range(2):
            for l in range(len(array[j])):
                dp[i][j][k] += dp[i-1][array[j][l]][k]
                dp[i][j][k] %= MOD
    tmp = dp[i][x-1][0]
    dp[i][x-1][0] = dp[i][x-1][1]
    dp[i][x-1][1] = tmp

print(dp[-1][t-1][0])
