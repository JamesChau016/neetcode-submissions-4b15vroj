class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pre=[1]*n
        suf=[1]*n
        preS=1
        for i in range(1,n):
            preS*=nums[i-1]
            pre[i]=preS
        
        sufS=1
        for i in range(n-2,-1,-1):
            sufS*=nums[i+1]
            suf[i]=sufS

        return [pre[i]*suf[i] for i in range(n)]
