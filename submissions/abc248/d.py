n = int(input())
a = list(map(int, input().split()))
q = int(input())

array = [[] for _ in range(2*10**5)]

for i in range(n):
    array[a[i]-1].append(i)

for i in range(q):
    l, r, x = map(int, input().split())
    sta, end = -1, len(array[x-1])
    while end-sta >= 2:
        if array[x-1][(sta+end)//2] >= l-1:
            end = (sta+end)//2
        else:
            sta = (sta+end)//2
    ans = sta
    
    sta, end = -1, len(array[x-1])
    while end-sta >= 2:
        if array[x-1][(sta+end)//2] < r:
            sta = (sta+end)//2
        else:
            end = (sta+end)//2
    ans = end - ans - 1
    
    print(ans)
    
