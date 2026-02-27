import sys
import bisect
from collections import deque
from collections import defaultdict
import heapq

input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())
li= lambda: list(input())
INF = sys.maxsize

def solve():
    n,ax,ay,bx,by=mii()
    x=lii()
    y=lii()
    d=defaultdict(list)
    keys=[0]*(200000+1)
    heapq.heappush(d[ax],ay)
    heapq.heappush(d[bx],by)
    for i in range(n):
        heapq.heappush(d[x[i]],y[i])
        keys[x[i]]=1
    x=ax
    y=ay
    print(d[x])
    distl=2*heapq.nlargest(d[x])-y-heapq.nsmallest(d[x])
    y=heapq.nsmallest(d[x])
    i=0
    while x!=bx and y!=by:
        if keys[x]:
            s=heapq.nsmallest(d[x])
            l=heapq.nlargest(d[x])
            if i%2==0:
                if s>=y: distl+=l-y
                else: distl+=2*abs(y-s)+abs(l-y)
                y=s
            else:
                if l<=y: distl+=y-s
                else: distl+=2*abs(l-y)+abs(y-s)
                y=l
            i+=1
        x+=1
    distr=2*abs(y-heapq.nsmallest(d[x]))+abs(heapq.nlargest(d[x]))
    y=heapq.nlargest(d[x])
    i=0
    while x!=bx and y!=by:
        if keys[x]:
            s=heapq.nsmallest(d[x])
            l=heapq.nlargest(d[x])
            if i%2==1:
                if s>=y: distr+=l-y
                else: distr+=2*abs(y-s)+abs(l-y)
                y=s
            else:
                if l<=y: distr+=y-s
                else: distr+=2*abs(l-y)+abs(y-s)
                y=l
            i+=1
        x+=1
    print(min(distl,distr))
    return

for _ in range(int(input())):
    solve()