class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        if m*n==1: return grid[0][0]
        
        table=[[0]*(n) for _ in range(m)]
        table[0][0]=grid[0][0]

        # 0th column values updated from down movement
        for i in range(m):
            table[i][0]=table[i-1][0]+grid[i][0]

        #0th row updated from right side movement
        for i in range(n):
            table[0][i]=table[0][i-1]+grid[0][i]

        # remaining columns updated with minimum value at each cell from its previous up and left side cell value
        for r in range(1,m):
            for c in range(1,n):
                table[r][c]=grid[r][c]+min(table[r-1][c],table[r][c-1])

        return table[m-1][n-1]
