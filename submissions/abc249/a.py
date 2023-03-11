a, b, c, d, e, f, x= map(int, input().split())

ans1, ans2 = 0, 0

ans1 += (x//(a+c))*b*a
if x%(a+c) < a:
    ans1 += (x%(a+c))*b
else:
    ans1 += a*b
    
ans2 += (x//(d+f))*e*d
if x%(d+f) < d:
    ans2 += (x%(d+f))*e
else:
    ans2 += d*e
    
if ans1 > ans2:
    print("Takahashi")
elif ans1 < ans2:
    print("Aoki")
else:
    print("Draw")
