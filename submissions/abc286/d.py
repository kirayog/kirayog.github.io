n, x = map(int, input().split())
abList = [[-1, -1] for _ in range(n)]

dp = [[False for _ in range(x+1)] for _ in range(n+1)]
#x‚ª0-10000‰~
#n‚ª0-2ŒÂŽg—p

for i in range(n):
    a, b = map(int, input().split())
    abList[i][0] = a
    abList[i][1] = b
    
dp[0][0] = True

for i in range(1, n+1):
    for j in range(x+1):
        if dp[i-1][j] == True:
            for k in range(abList[i-1][1]+1):
                if j+abList[i-1][0]*k <= x:
                    dp[i][j+abList[i-1][0]*k] = True
                
if dp[-1][-1] == True:
    print("Yes")
else:
    print("No")
