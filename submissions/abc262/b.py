n, m = map(int, input().split())
array = [[0 for _ in range(n)] for _ in range(n)]
ans = 0

for i in range(m):
    u, v = map(int, input().split())
    array[u-1][v-1] = 1
    array[v-1][u-1] = 1
    
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if array[i][j] == 1 and array[j][k] == 1 and array[k][i] == 1:
                ans += 1
                
print(ans)
