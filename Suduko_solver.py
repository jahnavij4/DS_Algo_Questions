class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n=9

        def isValid(row,col,ch):
            # row,col
            for i in range(9):
                if board[row][i]==ch:
                    return False
                if board[i][col]==ch:
                    return False
                if board[3*(row//3)+i//3][3*(col//3)+i%3]==ch:
                    return False
            return True
        

        def suduko(row,col):
            if row==n:
                return True
            if col==n:
                return suduko(row+1,0)
            
            if board[row][col]==".":
                for i in range(1,10):
                    if isValid(row,col,str(i)):
                        board[row][col]=str(i)
                        if suduko(row,col+1):
                            return True
                        else:
                            board[row][col]="."
                return False
            else:
                return suduko(row,col+1)
        suduko(0,0)



        
