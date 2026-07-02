from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
        
        INF=pow(2,31)-1
        lenRow=len(grid)
        lenCol=len(grid[0])
        visited=set()
        queue=deque()

        for r in range(lenRow):
            for c in range(lenCol):
                if grid[r][c]==0:
                    queue.append((r,c))
        
        travel=[(1,0),(0,1),(-1,0),(0,-1)]
        while queue:
            row,col=queue.popleft()
            visited.add((row,col))

            for x,y in travel:
                newRow, newCol=row+x,col+y

                if 0 <= newRow < lenRow and 0 <= newCol < lenCol:
                    if (newRow,newCol) in visited:
                        continue
                    if grid[newRow][newCol]==INF:
                        grid[newRow][newCol]=grid[row][col]+1
                        queue.append((newRow,newCol))

