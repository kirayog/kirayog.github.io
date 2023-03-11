array = [0 for i in range(10)]
xList = []
yList = []

for i in range(10):
    x = input()
    array[i] = list(x)
    
for i in range(10):
    for j in range(10):
        if array[i][j] == "#":
            xList.append(i+1)
            yList.append(j+1)
            
str1 = ""
str2 = ""

str1 += str(min(xList))
str1 += " "
str1 += str(max(xList))
str2 += str(min(yList))
str2 += " "
str2 += str(max(yList))
print(str1)
print(str2)
