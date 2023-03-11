n = int(input())
a = list(map(int, input().split()))

a.sort()

ans = []

ans.append(int(str(a[-1]) + str(a[-2]) + str(a[-3])))
ans.append(int(str(a[-1]) + str(a[-3]) + str(a[-2])))
ans.append(int(str(a[-2]) + str(a[-1]) + str(a[-3])))
ans.append(int(str(a[-2]) + str(a[-3]) + str(a[-1])))
ans.append(int(str(a[-3]) + str(a[-1]) + str(a[-2])))
ans.append(int(str(a[-3]) + str(a[-2]) + str(a[-1])))

print(max(ans))
