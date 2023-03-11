n = input()
s = list(input())
leftArray = []
rightArray = []
for i in range(len(s)):
    leftArray.append(i) if s[i] == "R" else rightArray.append(i)
leftArray.append(len(s))
print(*leftArray + rightArray[::-1])
