n = int(input())
array = [["", ""] for _ in range(n)]

for i in range(n):
    array[i][0], array[i][1] = input().split()
    
for i in range(n):
    s, t = True, True
    for j in range(n):
        if i == j: continue
        if array[i][0] == array[j][0] or array[i][0] == array[j][1]:
            s = False
        if array[i][1] == array[j][1] or array[i][1] == array[j][0]:
            t = False
    if s == False and t == False:
        print("No")
        exit()
print("Yes")
