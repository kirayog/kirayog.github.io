n, m = map(int, input().split())
s = []
ans = 0

for i in range(n):
    s.append(input())
    
for i in range(n):
    for j in range(n):
        if i != j and i < j:
            flag = False
            for k in range(m):
                if s[i][k] == "x" and s[j][k] == "x":
                    flag = True
            if flag == False:
                ans += 1

print(ans)
