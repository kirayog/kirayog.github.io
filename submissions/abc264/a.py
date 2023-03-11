l, r = map(int, input().split())

str = "atcoder"
ans = ""

for i in range(l-1, r):
    ans += str[i]
    
print(ans)
