def f(i, total):
    if i == len(a):
        if total == x: return 1
        else: return 0
    count = 0
    for j in range(len(a[i])):
        count += f(i+1, total*a[i][j])
    return count

n, x = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
    a[i].pop(0)

print(f(0, 1))
