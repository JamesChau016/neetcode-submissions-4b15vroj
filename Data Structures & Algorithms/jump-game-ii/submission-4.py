class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        count=1
        l=1
        r=nums[0]
        while l+r<len(nums):
            jump=(nums[l],l)
            for i in range(l,r+l):
                if nums[i]+i>=sum(jump):
                    jump=(nums[i],i)
                    l=i+1
            r=jump[0]
            count+=1
        
        return count