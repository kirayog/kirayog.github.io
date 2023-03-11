n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
s = input()
di = {} #キーにy座標、値に[min(R), max(L)]

for i in range(n):
    if li[i][1] not in di.keys():
        if s[i] == "R": di[li[i][1]] = [li[i][0], -1]
        else: di[li[i][1]] = [-1, li[i][0]]
    else:
        if s[i] == "R":
            if di[li[i][1]][0] == -1: di[li[i][1]][0] = li[i][0]
            else: di[li[i][1]][0] = min(di[li[i][1]][0], li[i][0])
        if s[i] == "L":
            if di[li[i][1]][1] == -1: di[li[i][1]][1] = li[i][0]
            else: di[li[i][1]][1] = max(di[li[i][1]][1], li[i][0])
              
for values in di.values():
    if values[0] != -1 and values[1] != -1:
        if values[0] < values[1]:
            print("Yes")
            exit()
print("No")
