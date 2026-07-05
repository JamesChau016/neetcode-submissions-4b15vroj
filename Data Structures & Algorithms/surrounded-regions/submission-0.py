class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS=len(board)
        COLS=len(board[0])
        
        def dfs(row,col):
            if row<0 or row>=ROWS or col<0 or col>=COLS:
                return
            
            if board[row][col]!='O':
                return
            
            board[row][col]='#'

            dfs(row+1,col)
            dfs(row,col+1)
            dfs(row-1,col)
            dfs(row,col-1)
        
        for r in range(ROWS):
            dfs(r,0)
            dfs(r,COLS-1)
        
        for c in range(COLS):
            dfs(0,c)
            dfs(ROWS-1,c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=='O':
                    board[r][c]='X'
                elif board[r][c]=='#':
                    board[r][c]='O'
            
