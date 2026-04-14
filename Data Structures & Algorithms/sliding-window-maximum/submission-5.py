from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]

        dq=deque([0])

        for i in range(1,k):
            
            while len(dq)>0 and nums[dq[-1]]<nums[i]:
                dq.pop()
            dq.append(i)

        
        ans.append(nums[dq[0]])

        l=1
        for i in range(k,len(nums)):
            if l>dq[0]:
                dq.popleft()
            while len(dq)>0 and nums[dq[-1]]<nums[i]:
                dq.pop()

            dq.append(i)
            
            ans.append(nums[dq[0]])
            l+=1

        return ans