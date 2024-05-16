class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def dfs(i, j):
            if i == m or j == n:
                return 0
            
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            
            right = grid[i][j] + dfs(i + 1, j)
            down = grid[i][j] + dfs(i, j + 1)

            res = min(right, down)

            return res

        return dfs(0, 0)

grid = [[1,3,1],[1,5,1],[4,2,1]]
print(Solution().minPathSum(grid))