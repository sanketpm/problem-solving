class Solution:
    def numSquares(self, n: int) -> int:

        maxSquare = int(n / 2)

        def dfs(sum):
            if sum == 0:
                return 0
            
            if sum < 0:
                return n + 1

            minSq = n + 1

            for i in range(1, sum):
                minSq = min(minSq, 1 + dfs(sum - (i ** 2)))
            
            return minSq
        
        return dfs(n)
    
res = Solution().numSquares(12)
print(res)