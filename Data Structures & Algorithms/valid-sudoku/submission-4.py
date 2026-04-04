class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            col={}
            row={}
            squ={}
            for j in range(9):
                if board[i][j]!='.':
                    if row.get(board[i][j]) is None:
                        row[board[i][j]]=1
                    else:
                        return False
                if board[j][i]!='.':
                    if col.get(board[j][i]) is None:
                        col[board[j][i]]=1
                    else:
                        return False
                s1=(i%3)*3+j//3
                s2=j%3+(i//3)*3
                if board[s1][s2]!='.':
                    if squ.get(board[s1][s2]) is None:
                        squ[board[s1][s2]]=1
                    else:
                        return False

        return True