n = int(input())
s = input()
ans = []

flag = False
for i in range(n):
    if s[i] == "n":
        flag = True
        ans.append("n")
    elif s[i] == "a" and flag == True:
        flag = False
        ans.append("ya")
    else:
        flag = False
        ans.append(s[i])
        
print("".join(ans))
