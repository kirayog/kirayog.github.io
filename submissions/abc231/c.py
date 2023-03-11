n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

for i in range(q):
    x = int(input())
    st, en = -1, n
    for j in range(n):
        if a[(st+en)//2] < x:
            st = (st+en)//2
        elif a[(st+en)//2] >= x:
            en = (st+en)//2
        if st+1 == en or st == en:
            print(n-st-1)
            break
