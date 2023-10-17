## links
[leetcode](https://leetcode.com/problems/target-sum)

## Expected Output


## Recursive Approach

```
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)

        def dfs(i: int, sum: int) -> int:
            if i == N:
                if sum == target:
                    return 1
                else:
                    return 0
            
            plus = dfs(i + 1, sum + nums[i])
            minus = dfs(i + 1, sum - nums[i])

            return plus + minus
        
        return dfs(0, 0)
```

## Memoization - Top_Down

```
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)

        dp = {}

        def dfs(i: int, sum: int) -> int:
            if i == N:
                if sum == target:
                    return 1
                else:
                    return 0
            
            if (i, sum) in dp:
                return dp[(i, sum)]
            
            dp[(i, sum)] = ( dfs(i + 1, sum + nums[i]) + 
                            dfs(i + 1, sum - nums[i]) )

            return dp[(i, sum)]
        
        return dfs(0, 0)
```

## Tabulation - Bottom up

```

```