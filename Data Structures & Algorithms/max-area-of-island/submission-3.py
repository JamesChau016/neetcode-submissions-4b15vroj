class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(row,col):
            nonlocal area
            if (row<0 or col<0 or row>=len(grid) or col>=len(grid[0])):
                return
            
            if grid[row][col]==0:
                return
            
            area+=1
            grid[row][col]=0
            dfs(row+1,col)
            dfs(row,col+1)
            dfs(row-1,col)
            dfs(row,col-1)
        
        res=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==0:
                    continue
                area=0
                dfs(r,c)
                res=max(res,area)
        
        return res