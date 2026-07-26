class Solution:
    def rob(self, nums: List[int]) -> int:
        visited={}
        nums1=nums[:-1]
        nums2=nums[1:]
        def dp(i,arr,n):
            if i>=len(arr):
                return 0
            
            if visited.get((i,n),None):
                return visited.get((i,n))
            
            s=max(arr[i]+dp(i+2,arr,n),dp(i+1,arr,n))
            visited[(i,n)]=s
            return s

        
        return max(dp(0,nums1,0),dp(0,nums2,1)) if len(nums)>1 else dp(0,nums,0)