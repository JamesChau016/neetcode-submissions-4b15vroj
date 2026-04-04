class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[1]*n
        for i in range(n-1):
            s=1
            for j in range(i+1,n):
                s*=nums[j]
            ans[i]=s
        
        for i in range(n-1,0,-1):
            for j in range(i-1, -1, -1):
                ans[i]*=nums[j]
        return ans
