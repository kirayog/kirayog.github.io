s = input()

array = [[6], [3], [1, 7], [0, 4], [2, 8], [5], [9]]

if s[0] == "1":
    print("No")
    exit()
    
for i in range(1, len(array)-1):
    flag = False
    for j in range(len(array[i])):
        if s[array[i][j]] == "1":
            flag = True
    if flag == False:
        left = False
        right = False
        for j in range(0, i):
            for k in range(len(array[j])):
                if s[array[j][k]] == "1":
                    left = True
        for j in range(i+1, len(array)):
            for k in range(len(array[j])):
                if s[array[j][k]] == "1":
                    right = True
        if left == True and right == True:
            print("Yes")
            exit()
            
print("No")
