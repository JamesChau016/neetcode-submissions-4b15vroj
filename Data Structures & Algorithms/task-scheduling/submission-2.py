import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time=0

        alpha=[0]*26
        for i in tasks:
            alpha[ord(i)%65]+=1
        
        l=[(-alpha[i],chr(i+65)) for i in range(len(alpha)) if alpha[i]!=0]
        heapq.heapify(l)
        
        q=deque()

        while q or l:
            time+=1
            if q and q[0][2]<=time:
                tmp=q.popleft()
                heapq.heappush(l,(-tmp[0],tmp[1]))


            if l:            
                f,c=heapq.heappop(l)
                if -f-1>0:
                    q.append((-f-1,c,time+n+1))
            else:
                time+=(q[0][2]-time-1)


        return time