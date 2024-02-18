class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n= len(obstacleGrid),len(obstacleGrid[0])
        table=[[0]*(n) for _ in range(m)]
        table[0][0]=1 if obstacleGrid[0][0]!=1 else 0
        for i in range(1,m):
            if obstacleGrid[i][0]!=1 and table[i-1][0]!=0:
                table[i][0]=1

        for j in range(1,n):
            if obstacleGrid[0][j]!=1 and table[0][j-1]!=0:
                table[0][j]=1
        
        for r in range(1,m):
            for c in range(1,n):
                if obstacleGrid[r][c]!=1:
                    table[r][c]=table[r-1][c]+table[r][c-1]
        
        return table[m-1][n-1] if obstacleGrid[m-1][n-1]!=1 else 0
