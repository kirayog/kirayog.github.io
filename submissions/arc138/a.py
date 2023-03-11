n, k = map(int, input().split())
a = list(map(int, input().split()))

array = [[a[i], k-i, -1] for i in range(n)] #[Œ³‚Ì”š, Œ³‚Ì•À‚Ñ‡, ‚¢‚­‚ÂˆÚ“®‚·‚é•K—v‚ª‚ ‚é‚©]
array1 = array[:k]
array2 = array[k:]
array1.sort()
ans = 10**6

current = 0
i = 0
flag = False
while True:
    if array1[current][0] < array2[i][0]:
        array1[current][2] = i
        current += 1
        flag = True
    else:
        i += 1
    if current == k or i == n-k:
        break
        
for i in range(k):
    if array[i][2] != -1:
        ans = min(ans, array[i][1] + array[i][2])

if flag == False:
    print(-1)
else:
    print(ans)
