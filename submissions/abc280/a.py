h, w = map(int, input().split())
s = []

ans = 0

for i in range(h):
    s.append(input())
    
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            ans += 1
print(ans)
