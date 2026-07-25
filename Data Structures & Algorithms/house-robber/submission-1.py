class Solution:
    def rob(self, nums: List[int]) -> int:
        hashMap={}
        def dp(index):
            if index>=len(nums):
                return 0
            if hashMap.get(index):
                return hashMap.get(index)
            s=max(nums[index]+dp(index+2),dp(index+1))
            hashMap[index]=s
            return s
        
        return dp(0)