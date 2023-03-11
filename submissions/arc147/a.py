from collections import deque

n = int(input())
a = list(map(int, input().split()))

a.sort()
a = deque(a)
ans = 0

while True:
    tmp = a[n-1]%a[0]
    a.pop()
    if tmp == 0:
        n -= 1
    else:
        a.appendleft(tmp)
    ans += 1
    if n == 1:
        break

print(ans)
