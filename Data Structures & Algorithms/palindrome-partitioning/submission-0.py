class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]

        def backtrack(l,index):
            if index==len(s):
                res.append(l[:])
                return
            
            for end in range(index+1,len(s)+1):
                sub=s[index:end]
                if sub==sub[::-1]:
                    l.append(sub)
                    backtrack(l,end)
                    l.pop()
                

        l=[]
        index=0
        backtrack(l,index)
        return res