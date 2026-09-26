class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        att_row=set()
        att_pos_dia=set()
        att_neg_dia=set()
        
        res=[]

        def backtrack(board,col):
            if col==n:
                res.append(board[:])
                return
                
            for row in range(n):
                if (row in att_row or
                    (row+col) in att_pos_dia or
                    (row-col) in att_neg_dia):
                    continue
            
                r=list(board[row])
                r[col]='Q'
                board[row]=''.join(r)
                att_row.add(row)
                att_pos_dia.add(row+col)
                att_neg_dia.add(row-col)

                backtrack(board,col+1)
                board[row]='.'*n
                att_row.remove(row)
                att_pos_dia.remove(row+col)
                att_neg_dia.remove(row-col)
            else:
                return

        board=['.'*n for i in range(n)]
        col=0
        backtrack(board,col)
        return res
