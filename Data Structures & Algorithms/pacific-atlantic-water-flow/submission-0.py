class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS=len(heights)
        COLS=len(heights[0])

        def dfs(ocean,prev,row,col):
            if row<0 or row>=ROWS or col<0 or col>=COLS:
                return
            if (row,col) in ocean:
                return
            if prev>heights[row][col]:
                return
            
            ocean.add((row,col))
            node=heights[row][col]
            dfs(ocean,node,row+1,col)
            dfs(ocean,node,row,col+1)
            dfs(ocean,node,row-1,col)
            dfs(ocean,node,row,col-1)
        
        pacific=set()
        atlantic=set()
    
        for r in range(ROWS):
            dfs(pacific,0,r,0)
            dfs(atlantic,0,r,COLS-1)
        
        for c in range(COLS):
            dfs(pacific,0,0,c)
            dfs(atlantic,0,ROWS-1,c)

        res=list(pacific & atlantic)
        for i in range(len(res)):
            res[i]=list(res[i])

        return res
