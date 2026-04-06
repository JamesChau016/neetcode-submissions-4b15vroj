class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums=sorted(nums)
        n=len(nums)

        for i in range(n-2):
            if i>0 and nums[i-1]==nums[i]:
                continue
            l=i+1
            r=n-1
            while l<r:
                s=nums[l]+nums[r]
                if s<-nums[i]:
                    l+=1
                elif s>-nums[i]:
                    r-=1
                else:
                    ans.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l-1]==nums[l] and l<n-1:
                        l+=1
                    while nums[r+1]==nums[r] and l<n-1:
                        r-=1
        return ans