from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        lenRow=len(grid)
        lenCol=len(grid[0])
        queue=deque()
        visited=set()
        fresh=0

        for r in range(lenRow):
            for c in range(lenCol):
                if grid[r][c]==2:
                    queue.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1
        
        if fresh==0:
            return 0
        
        travel=[(1,0),(0,1),(-1,0),(0,-1)]
        res=0
        while queue and fresh>0:
            size=len(queue)
            for i in range(size):
                row,col=queue.popleft()
                for x,y in travel:
                    newRow,newCol=row+x,col+y
                    
                    if 0<=newRow<lenRow and 0<=newCol<lenCol:
                        if (newRow,newCol) not in visited:
                            if grid[newRow][newCol]==1:
                                grid[newRow][newCol]=2
                                queue.append((newRow,newCol))
                                visited.add((newRow,newCol))
                                fresh-=1
            res+=1
            
        
        for r in range(lenRow):
            for c in range(lenCol):
                if grid[r][c]==1:
                    return -1
        
        return res
        
        
