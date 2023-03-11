n, k = map(int, input().split())
a = list(map(int, input().split()))

ansArray = sorted(a)

for i in range(k):
    tmpArray = []
    for j in range(n//k+1):
        if j*k+i >= n:
            break
        tmpArray.append(a[j*k+i])
    tmpArray.sort()
    for j in range(n//k+1):
        if j*k+i >= n:
            break
        if tmpArray[j] != ansArray[j*k+i]:
            print("No")
            exit()
print("Yes")
