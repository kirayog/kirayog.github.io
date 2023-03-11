h, w = map(int, input().split())
li = [input().split() for _ in range(h)]
for i in range(w):
    ansList = [li[j][i] for j in range(h)]
    print(*ansList)
