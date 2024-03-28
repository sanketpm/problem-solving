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

## Greedy O(n)
```
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        max_reach, stop = 0, 0
        jumps = 0

        for i in range(n - 1):
            max_reach = max(max_reach, i + nums[i])

            if i == stop:
                stop = max_reach
                max_reach = 0
                jumps += 1
                
        return jumps
```