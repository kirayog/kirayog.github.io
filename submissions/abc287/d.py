s = input()
t = input()

lenS = len(s)
lenT = len(t)
tfList = [False for _ in range(lenT)]
deff = 0

for i in range(lenT):
    if s[lenS-lenT+i] == t[i] or \
    s[lenS-lenT+i] == "?" or \
    t[i] == "?":
        tfList[i] = True
    else:
        tfList[i] = False
        deff += 1
        
if deff == 0:
    print("Yes")
else:
    print("No")

for i in range(lenT):
    if tfList[i] == False:
        tfList[i] = True
        deff -= 1
    if s[i] == t[i] or \
    s[i] == "?" or \
    t[i] == "?":
        tfList[i] = True
    else:
        tfList[i] = False
        deff += 1
    if deff == 0:
        print("Yes")
    else:
        print("No")
