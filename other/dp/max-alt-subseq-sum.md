## links
[leetcode](https://leetcode.com/problems/maximum-alternating-subsequence-sum)

## Expected Output


## Recursive Approach

```
class Solution:

    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)

        def dfs(i, op):
            if i == n:
                return 0

            take = (nums[i] * op) + dfs(i + 1, op * -1)
            skip = dfs(i + 1, op)

            return max(take, skip)
        return dfs(0, 1)
```

## Memoization - Top_Down

```
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)

        dp = {}

        def dfs(i, op):
            if i == n:
                return 0

            if (i, op) in dp:
                return dp[(i, op)]

            take = (nums[i] * op) + dfs(i + 1, op * -1)
            skip = dfs(i + 1, op)

            dp[(i, op)] = max(take, skip)
            return dp[(i, op)]

        return dfs(0, 1)
```

## Tabulation - Bottom up

```
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)

        prev_plus = 0
        prev_minus = 0

        for i in range(n):
            curr_plus = max(prev_minus + nums[i], prev_plus)
            curr_minus = max(prev_plus - nums[i], prev_minus)

            prev_plus = curr_plus
            prev_minus = curr_minus
        
        return prev_plus
```