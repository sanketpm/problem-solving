## Links
[Leetcode](https://leetcode.com/problems/jump-game-ii)

## Expected Output
Minimum number of jumps to reach to the end

### Brute Force
**Approach**:
- DFS

**code**:
```
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        def dfs(i):
            if i >= n - 1:
                return 0
            
            min_jump = float('inf')

            for j in range(nums[i], 0, -1):
                jumps_to_end = 1 + dfs(i + j)
                min_jump = min(min_jump, jumps_to_end)
            
            return min_jump
        
        return dfs(0)
```

### Memoization
**Approach**


**code**:
```
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        dp = {}

        def dfs(i):
            if i >= n - 1:
                return 0
            
            if i in dp:
                return dp[i]
            
            min_jump = float('inf')

            for j in range(nums[i], 0, -1):
                jumps_to_end = 1 + dfs(i + j)
                min_jump = min(min_jump, jumps_to_end)
            
            dp[i] = min_jump

            return dp[i]
        
        return dfs(0)
```