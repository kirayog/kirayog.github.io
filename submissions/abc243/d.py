n, x = map(int, input().split())
s = input()
newS = []
uCount = 0

for i in range(1, n+1):
    if s[-i] == "U":
        uCount += 1
    elif (s[-i] == "L" or "R") and uCount > 0:
        uCount -= 1
    else:
        newS.append(s[-i])

while uCount > 0:
    newS.append("U")
    uCount -= 1

newS.reverse()

for i in range(len(newS)):
    if newS[i] == "U":
        x = x // 2
    elif newS[i] == "L":
        x = x * 2
    elif newS[i] == "R":
        x = x * 2 + 1

print(x)
