class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        def backtrack(l,index):
            if index==len(nums):
                res.append(l[:])
                return
            
            l.append(nums[index])
            backtrack(l,index+1)
            l.pop()
            while index+1<len(nums) and nums[index]==nums[index+1]:
                index+=1
            
            backtrack(l,index+1)
        
        l=[]
        index=0
        backtrack(l,index)
        return res