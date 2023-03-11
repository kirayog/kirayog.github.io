n = int(input())
s = input().split("C")
newS = []
for i in range(len(s)):
    count = 0
    for j in range(len(s[i])):
        if s[i][j] == "A": count+=2
        if s[i][j] == "B": count+=1
    newS.append("A"*(count//2) + "B"*(count%2))
        
print("C".join(newS))
