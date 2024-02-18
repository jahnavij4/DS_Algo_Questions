class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m=len(triangle)
        table=[[0]*(m+1) for _ in range(m+1)]

        
        for i in range(m-1,-1,-1):
            for j in range(len(triangle[i])):
                table[i][j]=triangle[i][j]+min(table[i+1][j],table[i+1][j+1])
                
        return table[0][0]
