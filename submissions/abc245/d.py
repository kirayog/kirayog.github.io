n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

b = [0 for _ in range(m+1)]
count = 0
for i in range(n+1):
    if a[i] == 0:
        count += 1
    else:
        break

for i in range(m+1):
    b[i] = c[i+count]//a[count]
    for j in range(count, n+1):
        c[j+i] -= a[j]*b[i]

print(*b)
