n, k = map(int, input().split())
s = input()

count = 0
ans = ""

for i in range(n):
    if s[i] == "o" and count < k:
        count += 1
        ans += s[i]
    else:
        ans += "x"
        
print(ans)
