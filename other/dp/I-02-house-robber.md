## Links
[Leetcode](https://leetcode.com/problems/house-robber/)

## Expected Output
Maximum Profit by robbing wihout getting caught

> This is a perfect DP Problem to understand how recursion links with Memoization & DP, how we can break down our recusion to form the other two types of optimized solutions

## Recursive Approach
**Bottom Up**
```
class Solution:
    def robHouse(self, idx: int, nums: List[int]) -> int:
        if idx >= len(nums):
            return 0
        
        rob = nums[idx] + self.robHouse(idx + 2, nums)
        dntRob = self.robHouse(idx + 1, nums)

        return max(rob, dntRob)

    def rob(self, nums: List[int]) -> int:
        return self.robHouse(0, nums)
```

**Top Down**
```
class Solution:
    def robHouse(self, N: int, nums: List[int]) -> int:
        if N <= 0:
            return 0
        
        rob = nums[N - 1] + self.robHouse(N - 2, nums)
        dntRob = self.robHouse(N - 1, nums)

        return max(rob, dntRob)

    def rob(self, nums: List[int]) -> int:
        return self.robHouse(len(nums), nums)
```


## Memoization - Top Down
```
class Solution:
    def robHouse(self, N: int, nums: List[int], dp: List[int]) -> int:
        if N <= 0:
            return 0

        if dp[N] != -1:
            return dp[N]

        rob = nums[N - 1] + self.robHouse(N - 2, nums, dp)
        dntRob = self.robHouse(N - 1, nums, dp)

        dp[N] = max(rob, dntRob)
        return dp[N]

    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [-1] * (N + 1)
        return self.robHouse(N, nums, dp)
```

## Tabulation - Bottom Up

```
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * (N + 1)

        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, N + 1):
            dntTake = dp[i - 1]
            take = nums[i - 1] + dp[i - 2]

            dp[i] = max(dntTake, take)
        
        return dp[N]
```