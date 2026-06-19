class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited=set()
        def backtrack(index,row,col):
            if index==len(word):
                return True
            
            if (row==len(board) 
                or row==-1 
                or col==len(board[0]) 
                or col==-1 
                or board[row][col]!=word[index]
                or (row,col) in visited):
                return False



            visited.add((row,col))
            res=(backtrack(index+1,row+1,col) or 
                backtrack(index+1,row,col+1) or
                backtrack(index+1,row-1,col) or
                backtrack(index+1,row,col-1))
            
            visited.remove((row,col))

            return res

        index=0 
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]!=word[0]:
                    continue
                
                if backtrack(index,r,c):
                    return True

    
        return False   

            