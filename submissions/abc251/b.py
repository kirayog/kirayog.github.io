n, w = map(int, input().split())
a = list(map(int, input().split()))

ansList = [0 for _ in range(w+1)]

for i in range(n):
    if a[i] <= w:
        ansList[a[i]] = 1
            
for i in range(n):
    for j in range(n):
        if i != j:
            if a[i]+a[j] <= w:
                ansList[a[i]+a[j]] = 1

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and j != k and k != i:
                if a[i]+a[j]+a[k] <= w:
                    ansList[a[i]+a[j]+a[k]] = 1

print(sum(ansList))
