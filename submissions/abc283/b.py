n = int(input())
a = list(map(int, input().split()))
q = int(input())

for i in range(q):
    tmp = list(map(int, input().split()))
    if tmp[0] == 1:
        a[tmp[1]-1] = tmp[2]
    else:
        print(a[tmp[1]-1])
