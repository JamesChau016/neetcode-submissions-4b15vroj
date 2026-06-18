class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]

        def backtrack(l,open,close):
            if len(l)==2*n:
                res.append(''.join(l[:]))
                return
            
            if open<n:
                l.append("(")
                backtrack(l,open+1,close)
                l.pop()


            if open>close:    
                l.append(")")
                backtrack(l,open,close+1)
                l.pop()
        
        l=[]
        open=0
        close=0
        backtrack(l,open,close)
        return res