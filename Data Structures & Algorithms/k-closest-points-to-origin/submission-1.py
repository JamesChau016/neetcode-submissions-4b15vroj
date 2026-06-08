import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points:
            return []

        ans=[]
        heapq.heapify(ans)

        for i in points:
            d=i[0]**2+i[1]**2
            heapq.heappush(ans,(-d, i))
            if len(ans)>k:
                heapq.heappop(ans)
        
        ans=list(ans)
        ans=[i[1] for i in ans]
        return ans