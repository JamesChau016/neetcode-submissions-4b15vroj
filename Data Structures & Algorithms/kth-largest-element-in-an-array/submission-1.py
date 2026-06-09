import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap=[]
        heapq.heapify(maxHeap)
        for i in nums:
            heapq.heappush(maxHeap, i)
            if len(maxHeap)>k:
                heapq.heappop(maxHeap)
        
        return heapq.heappop(maxHeap)