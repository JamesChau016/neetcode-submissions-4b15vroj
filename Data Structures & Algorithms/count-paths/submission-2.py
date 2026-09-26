class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==n==1:
            return 1
        memo={}

        def travel(r,c):
            nonlocal memo
            if (r==m-1 and c==n-1):
                return 1
            
            if (r==m or r<0) or (c==n or c<0):
                return 0
            
            if memo.get((r,c)):
                return memo.get((r,c))
            
            total= travel(r+1,c) + travel(r,c+1)
            memo[(r,c)]=total
            return total
        
        travel(0,0)

        return memo[(0,0)]