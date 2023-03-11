n = int(input())
m = input()

flag = False
ans = ["" for _ in range(n)]

for i in range(n):
    if m[i] == "\"":
        flag = not flag
        ans[i] = m[i]
    elif m[i] == "," and flag == False:
        ans[i] = "."
    else:
        ans[i] = m[i]
        
print("".join(ans))
