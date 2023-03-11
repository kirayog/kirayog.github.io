n = int(input())
a = [["" for _ in range(n)] for _ in range(n)]

for i in range(n):
    a[i] = list(input())

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        elif a[i][j] == "W" and a[j][i] == "L":
            continue
        elif a[i][j] == "L" and a[j][i] == "W":
            continue
        elif a[i][j] == "D" and a[j][i] == "D":
            continue
        print("incorrect")
        exit()
        
print("correct")
