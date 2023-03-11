from collections import deque

n = int(input())
a = deque(list(map(int, input().split())))
ans = []
total = 0

for i in range(n):
    total += 1
    tmp = a.popleft()
    if len(ans) > 0 and ans[-1][0] == tmp:
        ans[-1][1] += 1
        if ans[-1][0] == ans[-1][1]:
            total -= ans[-1][1]
            ans.pop()
    else:
        ans.append([tmp, 1])
    print(total)
