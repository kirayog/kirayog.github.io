n, m= map(int, input().split())
s = input().split()
t = set(input().split())
for x in s:
    print("Yes" if x in t else "No")
