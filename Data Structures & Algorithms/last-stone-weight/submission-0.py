import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones=[-i for i in stones]
        heapq.heapify(stones)

        n=len(stones)
        while n>1:
            x=heapq.heappop(stones)
            y=heapq.heappop(stones)
            s=-abs(x-y)
            if s!=0:
                heapq.heappush(stones, s)
            n=len(stones)
        
        return 0 if n==0 else -stones[0]