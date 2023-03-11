n = int(input())
s = input()

if n == 2:
    if s[0] == s[1]:
        print("Yes")
    else:
        print("No")
    exit()

if s[0] == "B" or s[-1] == "A":
    print("Yes")
else:
    print("No")
