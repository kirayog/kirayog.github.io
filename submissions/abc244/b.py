n = int(input())
t = input()

dire = [[1, 0], [0, -1], [-1, 0], [0, 1]]
currentDire = 0
currentPos = [0, 0]

for i in range(n):
    if t[i] == "S":
        currentPos[0] += dire[currentDire][0]
        currentPos[1] += dire[currentDire][1]
    else:
        currentDire = (currentDire+1)%4
        
print(*currentPos)
