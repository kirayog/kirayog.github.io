import heapq

n, k = map(int, input().split())
p = list(map(int, input().split()))
tmpP = p[:k]
print(min(tmpP))
heapq.heapify(tmpP)

for i in range(k,n):
    tmp = heapq.heappop(tmpP)
    tmp = max(tmp, p[i])
    heapq.heappush(tmpP, tmp)
    tmp = heapq.heappop(tmpP)
    print(tmp)
    heapq.heappush(tmpP, tmp)
