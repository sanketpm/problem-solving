## links
[leetcode](https://leetcode.com/problems/combination-sum-iv)

## Expected Output


## Recursive Approach

```
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def dfs(sum):
            if sum == target:
                return 1
            
            if sum > target:
                return 0
            
            res = 0

            for i in range(n):
                res += dfs(sum + nums[i])
            
            return res
        
        return dfs(0)
```

## Memoization - Top_Down

```
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)

        dp = {}

        def dfs(sum):
            if sum == target:
                return 1
            
            if sum > target:
                return 0
            
            if sum in dp:
                return dp[sum]
            
            res = 0

            for i in range(n):
                res += dfs(sum + nums[i])
            
            dp[sum] = res

            return dp[sum]
        
        return dfs(0)
```

## Tabulation - Bottom up

```
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)

        dp = [0] * (target + 1)

        dp[target] = 1

        for tar in range(target, -1, -1):
            for i in range(n):
                if tar + nums[i] > target:
                    continue
                
                dp[tar] += dp[nums[i] + tar]
            
        return dp[0]
```