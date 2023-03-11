n, a, b = map(int, input().split())
p, q, r, s = map(int, input().split())
ans = [["." for _ in range(s-r+1)] for _ in range(q-p+1)]

for i in range(max(p-a, r-b), min(q-a, s-b)+1):
    ans[a+i-p][b+i-r] = "#"

for i in range(max(p-a, b-s), min(q-a, b-r)+1):
    ans[a+i-p][b-i-r] = "#"

for i in ans:
    print("".join(i))
