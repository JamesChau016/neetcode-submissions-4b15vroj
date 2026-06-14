class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]

        def backtrack(l, index,s):
            nonlocal res

            if s==target:
                
                res.append(l[:])
                return

            if index==len(nums):
                return
            
            l.append(nums[index])
            s+=nums[index]
            if s<=target:
                backtrack(l,index,s)
            
            l.pop()
            s-=nums[index]
            backtrack(l,index+1,s)
        
        s=0
        index=0
        l=[]
        backtrack(l,index,s)
        return res
