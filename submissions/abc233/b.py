l, r = map(int, input().split())
s = input()
ls = s[:l-1]
rs = s[r:]
tmp = s[l-1:r]
tmp = tmp[::-1]
    
print(str(ls) + str(tmp) + str(rs))
