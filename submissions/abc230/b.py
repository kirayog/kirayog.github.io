s = input()
xCount = 0

for i in range(len(s)):
    if s[i] == "x":
        xCount += 1
        if xCount > 2:
            print("No")
            exit()
    else:
      break

for i in range(len(s)-xCount):
    if i%3 == 0:
        if s[i+xCount] == "x":
            print("No")
            exit()
    else:
        if s[i+xCount] == "o":
            print("No")
            exit()
            
print("Yes")
