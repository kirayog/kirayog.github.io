n, m = map(int, input().split())
a = []

count = 0

for i in range(m):
    c = int(input())
    a.append(list(map(int, input().split())))
    
for i in range(2**m):
    ck = [False for _ in range(n)]
    for j in range(m):
        if (i >> j) & 1:
            for k in range(len(a[j])):
                ck[a[j][k]-1] = True
    if False not in ck:
        count += 1
        
print(count)
