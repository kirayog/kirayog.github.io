s = list(input().split())
t = list(input().split())

if (s[0] == t[0] and s[1] != t[1]) or (s[1] == t[1] and s[2] != t[2]) or(s[2] == t[2] and s[1] != t[1]):
    print("No")
else:
    print("Yes")
