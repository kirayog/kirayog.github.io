alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

s = input()
t = input()

for i in range(len(alpha)):
    if s[0] == alpha[i]: tmp1 = i
    if t[0] == alpha[i]: tmp2 = i

diff = tmp2-tmp1

for i in range(1, len(s)):
    for j in range(len(alpha)):
        if s[i] == alpha[j]:
            tmp = (j+diff)%26
    if t[i] != alpha[tmp]:
        print("No")
        exit()

print("Yes")
