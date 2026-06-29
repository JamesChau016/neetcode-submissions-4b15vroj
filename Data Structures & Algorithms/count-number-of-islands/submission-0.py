class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res=0

        def dfs(row,col):
            if ((row>=len(grid) or row<0)
                or (col>=len(grid[0]) or col<0)):
                return
            
            if grid[row][col]=='0':
                return
            
            grid[row][col]='0'
            dfs(row+1,col)
            dfs(row,col+1)
            dfs(row-1,col)
            dfs(row,col-1)


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=='0':
                    continue
                dfs(r,c)
                res+=1
        
        return res