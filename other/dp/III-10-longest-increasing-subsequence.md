## Links
[Leetcode](https://leetcode.com/problems/longest-increasing-subsequence)

## Expected Output
Length of longest increasing subsequence 

## Approach
Pattern:
1. Take & Dont Take - recursively
2. Memoization: This is a prototype Pattern - `index-shifting`

### Brute Force
In traversal, at every index you point you need two things:
- `prevIdx`: previous smaller number's index
- `currIdx`: current element's index

You have two choices for each element:
a. dontTake
b. take

Criteria to `dontTake` or `take`:
1. `dontTake` : 
    - applicable at every index
    - prevIdx remains the same since that will the index of previous-smallest number
2. `take`: applicable at only those index where:
    - arr[prevIdx] < arr[currIdx]: value at currIdx is greater than the value at previous index
    - first element should always be taken, `prevIdx == -1` (first index): 

**code**
```
class Solution {

    private int lis(int idx, int prevIdx, int[] nums, int n) {
        if(idx == n) {
            return 0;
        }

        int dontTake = lis(idx + 1, prevIdx, nums, n);
        int take = 0;

        if(prevIdx == -1 || nums[prevIdx] < nums[idx]) {
            take = 1 + lis(idx + 1, idx, nums, n);
        }

        return Math.max(take, dontTake);
    }
    public int lengthOfLIS(int[] nums) {
        return lis(0, -1, nums, nums.length);    
    }
}
```

### Memoization
> prevIdx value remains the same everywhere except the dp array, when referring to dp array using prevIdx, add `+1` to it. At other places like if(..) else(..) or nums[prevIdx] (accessing value) etc.. its the same

- If arr = [1, 2, 3]\
    `idx` values => (0, 1, 2)\
`prevIdx` values => (-1, 0, 1, 2)
- Since `idx` & `prevIdx` are changing values, we create an array based on their max-values. From the above we can see:
- If farthest `idx` = 3, `prevIdx` will be 4
- If farthest `idx` = 4, `prevIdx` will be 5
- If farthest `idx` = 5  `prevIdx` will be 6
- Therefore, `idx` = `n`, `prevIdx` = `n + 1`
- size of dp array = `dp[n + 1][n + 1]` => `dp[prevIdx][currIdx]` 

```
class Solution {

    private int lis(int idx, int prevIdx, int n, int[] nums, int[][] dp) {
        if(idx == n) {
            return 0;
        }

        if(dp[idx][prevIdx + 1] != -1) {
            return dp[idx][prevIdx + 1];
        }

        int dontTake = lis(idx + 1, prevIdx, n, nums, dp);
        int take = 0;

        if(prevIdx == -1 || nums[prevIdx] < nums[idx]) {
            take = 1 + lis(idx + 1, idx, n, nums, dp);
        }

        return dp[idx][prevIdx + 1] = Math.max(take, dontTake);
    }

    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        int[][] dp = new int[n][n + 1];

        for(int t[] : dp) {
            Arrays.fill(t, -1);
        }

        return lis(0, -1, n, nums, dp);
    }
}
```
### Tabulation


```
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        LIS = [1] * n

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        return max(LIS)
```

## Python

**Recursion:**

```
class Solution:
    def LIS(self, idx: int, prev: int, N: int, nums: List[int]) -> int:
        if idx == N:
            return 0

        dntTake = self.LIS(idx + 1, prev, N, nums)

        take = 0
        if prev == -1 or nums[prev] < nums[idx]:
            take = 1 + self.LIS(idx + 1, idx, N, nums)
        
        return max(take, dntTake)
        
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        return self.LIS(0, -1, n, nums)
```

**Memoization:**

```
class Solution:
    def LIS(self, idx: int, prev: int, N: int, nums: List[int], dp: List[List[int]]) -> int:
        if idx == N:
            return 0

        if dp[idx][prev + 1] != -1:
            return dp[idx][prev + 1]
        
        dntTake = self.LIS(idx + 1, prev, N, nums, dp)

        take = 0
        if prev == -1 or nums[prev] < nums[idx]:
            take = 1 + self.LIS(idx + 1, idx, N, nums, dp)
        
        dp[idx][prev + 1] = max(take, dntTake)
        
        return dp[idx][prev + 1]

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1] * (n + 1) for _ in range(n)]

        return self.LIS(0, -1, n, nums, dp)
```

**DP**
