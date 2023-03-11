s = list(input())
start = 0 #a‚Å‚Í‚È‚¢‚Æ‚±‚ë‚ðŽw‚·
end = len(s)-1

while start < len(s):
    if s[start] == "a": start+=1
    else: break
while 0 <= end:
    if s[end] == "a": end-=1
    else: break
if start > len(s)-1-end:
    print("No")
    exit()

while start < end:
    if s[start] == s[end]:
        start+=1
        end-=1
    else:
        print("No")
        exit()
print("Yes")
