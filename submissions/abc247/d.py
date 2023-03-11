sta = 0
a = []

q = int(input())

for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        a.append([query[1], query[2]])
    if query[0] == 2:
        ans = 0
        while query[1] > 0:
            if query[1] > a[sta][1]:
                ans += a[sta][0] * a[sta][1]
                query[1] -= a[sta][1]
                a[sta][1] = 0
                sta += 1
            else:
                ans += a[sta][0] * query[1]
                a[sta][1] -= query[1]
                query[1] = 0
        print(ans)
