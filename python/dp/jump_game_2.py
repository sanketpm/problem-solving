class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        n = len(arr)

        def dfs(i):
            if i < 0 or i >= n:
                return False
            
            if arr[i] == 0:
                return True
            
            plus = dfs(i + arr[i])
            minus = dfs(i - arr[i])

            return plus or minus
        
        return dfs(start)

arr = [4,2,3,0,3,1,2]
start = 5
res = Solution().canReach(arr, start)