n = int(input())
s = []

for i in range(n):
    s.append(input())
    
for i in range(n):
    for j in range(n-5):
        countW = 0
        countH = 0
        for k in range(6):
            if s[i][j+k] == "#": countW += 1
            if s[j+k][i] == "#": countH += 1
        if countW >= 4 or countH >= 4:
            print("Yes")
            exit()
            
for i in range(n-5):
    for j in range(n-5):
        countR = 0
        countL = 0
        for k in range(6):
            if s[i+k][j+k] == "#": countR += 1
            if s[i+(5-k)][j+k] == "#": countL += 1
        if countR >= 4 or countL >= 4:
            print("Yes")
            exit()
            
print("No")
