#djisktra's
import heapq
import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())
INF=sys.maxsize

n,m=mii()
graph=defaultdict(list)
visited=[0]*(n+1)
cost=[INF]*(n+1)
parent=defaultdict(int)

for i in range(m):
    a,b,w=mii()
    graph[a].append((b,w))
source=1
cost[source]=0
heap=[(0,source)]
heapq.heapify(heap)

while heap:
    c,node=heapq.heappop(heap)
    if visited[node]:
        continue
    for next,d in graph[node]:
        if c+d < cost[next]:
            cost[next]=c+d
        heapq.heappush(heap,(cost[next],next))
    visited[node]=True

for i in range(1,n+1):
    print(cost[i],end=' ')
print()