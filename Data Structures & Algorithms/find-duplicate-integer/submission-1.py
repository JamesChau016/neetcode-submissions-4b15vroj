class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        
        for i in range(n):
            nums[abs(nums[i])-1]*=-1
            if nums[abs(nums[i])-1]>0:
                return abs(nums[i])