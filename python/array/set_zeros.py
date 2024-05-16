class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])

        def setRow(ROW):
            for i in range(col):
                matrix[ROW][i] = -1
            
        def setCol(COL):
            for i in range(row):
                matrix[i][COL] = -1

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    setRow(i)
                    setCol(j)
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0

        return matrix

# res = Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
res = Solution().setZeroes([[-1],[2],[3]])
print(res)