n = int(input())
p = list(map(int, input().split()))

a = []
tmp = p[n-1]

for i in range(n):
    if p[n-1-i] > tmp:
        j = 0
        while True:
            j += 1
            if p[n-1-i]-j in a:
                a[a.index(p[n-1-i]-j)] = p[n-1-i]
                a.insert(0, p[n-1-i]-j)
                cnt = 0
                for k in range(n-len(a), n):
                    p[k] = a[cnt]
                    cnt += 1
                print(*p)
                exit()
    else:
        a.append(p[n-1-i])
        tmp = p[n-1-i]
