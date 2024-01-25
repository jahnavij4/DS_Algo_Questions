class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        mainboard=[["."]*n for _ in range(n)]
        self.res=[]
        def isValid(row,col,board):
            for i in range(n):
                if row>0:
                    if i==col-1 and board[row-1][i]=='Q':
                        return False
                    if i==col+1 and board[row-1][i]=='Q':
                        return False
                    if board[i][col]=='Q':
                        return False
                if row-i>=0 and col-i>=0 and board[row-i][col-i]=='Q':
                    return False
                if row-i>=0 and col+i<n and board[row-i][col+i]=='Q':
                    return False
                    
            return True
            

        def addQueen(row,board):
            if row==n:
                self.res.append(["".join(x) for x in board])
                return
         
            if 'Q' not in board[row]:
                for i in range(n):
                    if isValid(row,i,board):
                        board[row][i]="Q"                        
                        if addQueen(row+1,board):
                            return True
                        else:
                            board[row][i]="."
                return False
            else:
                return addQueen(row+1,board)
        addQueen(0,mainboard)
        return self.res
            
