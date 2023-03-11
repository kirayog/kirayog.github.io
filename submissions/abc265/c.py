h, w = map(int, input().split())

array = [["" for _ in range(w)] for _ in range(h)]
tfArray = [[False for _ in range(w)] for _ in range(h)]
current = [0, 0]


for i in range(h):
    array[i] = list(input())
    
while True:
    if tfArray[current[0]][current[1]] == True:
        print(-1)
        exit()
        break
    else:
        tfArray[current[0]][current[1]] = True
        
    if array[current[0]][current[1]] == "U":
        if current[0] != 0:
            current[0] -= 1
        else:
            print(str(current[0]+1) + " " + str(current[1]+1))
            break
    elif array[current[0]][current[1]] == "D":
        if current[0] != h-1:
            current[0] += 1
        else:
            print(str(current[0]+1) + " " + str(current[1]+1))
            break
    elif array[current[0]][current[1]] == "L":
        if current[1] != 0:
            current[1] -= 1
        else:
            print(str(current[0]+1) + " " + str(current[1]+1))
            break
    elif array[current[0]][current[1]] == "R":
        if current[1] != w-1:
            current[1] += 1
        else:
            print(str(current[0]+1) + " " + str(current[1]+1))
            break
