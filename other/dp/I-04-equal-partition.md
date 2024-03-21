## links
[leetcode](https://leetcode.com/problems/partition-equal-subset-sum)

## Describe the Problem
```
Given:
nums = [1, 5, 11, 5]

Q: 
Partition the array into two subsets such that the sum of the elements in both subsets is equal.

e.g.:
nums = [1, 5, 11, 5]

subset1 = [1, 5, 5]
subset2 = [11]

Result = True

The given array can be split/partioned into two subsets of equal sum

e.g.:
nums = [1, 5, 5]
- There exist no two subsets for the input where thier sum is equal
```

**NOTE:**
- This problem depends entirely on [Subset_Sum](./I-02-subset-sum.md) problem.

**Observation**
- The total sum of array for a partionable array will always be even
- Array with Odd Total sum can never be partioned into two equal subsets

**Algorithm:**
1. Find total `sum`
2. If `sum` is odd -> return `False`
3. If `sum` is even -> subsetSum(nums, sum / 2)

- we send `sum/2` to subsetSum function to reduce the computation, send `sum` too will work.

## Tabulation - bottom up

```
class Solution:
    def subsetSum(self, N: int, sum: int, nums: List[int]) -> int:
        dp = [ [False] * (sum + 1) for _ in range(N + 1) ]

        for i in range(N + 1):
            dp[i][0] = True
        
        for i in range(1, N + 1):
            for j in range(1, sum + 1):
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[N][sum]

    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        sum = 0

        for i in range(N):
            sum += nums[i]
        
        if sum % 2 != 0:
            return False
        
        return self.subsetSum(N, int(sum / 2), nums)
```

**Questions**
1. why `sum/2` is the `target`
-> The two partioned subsets must contain sum of `sum/2` only then they can form `sum`