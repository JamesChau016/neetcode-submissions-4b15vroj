class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        
        def backtrack(l):
            if len(l)==len(nums):
                res.append(l[:])
                return 

            for i in nums:
                if i in l:
                    continue
                l.append(i)
                backtrack(l)
                l.pop()
        
        l=[]
        backtrack(l)
        return res