s = input()

a = [0 for _ in range(4)]
a[1] = s[0]
a[2] = s[1]
a[3] = s[2]

a = map(str, a)
print("".join(a))
