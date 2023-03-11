s = input()
dic = {}

if s.isupper() == True or s.islower() == True:
    print("No")
    exit()

for i in range(len(s)):
    if s[i] not in dic:
        dic[s[i]] = 1
    else:
        print("No")
        exit()
        
print("Yes")
