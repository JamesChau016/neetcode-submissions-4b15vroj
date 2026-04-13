class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        win=[nums[i] for i in range(k)]
        
        m=max(win)
        ans.append(m)
        
        l=1
        for i in range(k,len(nums)):
            removed=win.pop(l-1)
            win.append(nums[i])
            if removed==m:
                m=max(win)
            elif nums[i]>m:
                m=nums[i]
            ans.append(m)

        return ans