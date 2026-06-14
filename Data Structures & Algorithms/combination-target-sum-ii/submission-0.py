class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()

        def backtrack(l,index,s):
            if s==target:
                res.append(l[:])
                return
            
            if index==len(candidates):
                return
            
            l.append(candidates[index])
            s+=candidates[index]
            if s<=target:
                backtrack(l,index+1,s)
            
            l.pop()
            s-=candidates[index]

            while index+1<len(candidates) and candidates[index]==candidates[index+1]:
                index+=1
            backtrack(l,index+1,s)
        
        index=0
        s=0
        l=[]
        backtrack(l,index,s)
        return res
        
