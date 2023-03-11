n, k = map(int, input().split())
a = list(map(int, input().split()))
dic = {0:1}
ans, total = 0, 0

for i in range(n):
    total += a[i]
    if total-k in dic:
        ans += dic[total-k]
    if total in dic:
        dic[total] += 1
    else:
        dic[total] = 1
            
print(ans)
