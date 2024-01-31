## Links
[Leetcode](https://leetcode.com/problems/longest-consecutive-sequence/description/)

## Expected Output

### Brute Force
- code self explanatory
**Approach**

**Efficiency**:
- Time: `O(N * N)`, Where N is .
- Space: `O(N)`, Where N is

**code**:
```
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        res = 0

        for val in seq:
            cnt = 0

            while val in seq:
                cnt += 1
                val += 1

            res = max(res, cnt)
            
        return res
```

### Optimized
**Approach**

**Efficiency**:
- Time: `O(N * M)`, Whe    
- Space: `O(N)`, Where N is

**code**:
```
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        res = 0

        for num in nums:
            pre = num - 1

            if pre in seq:
                continue
            
            pre = num
            cnt = 0

            while pre in seq:
                cnt += 1
                pre += 1
            
            res = max(res, cnt)
            
        return res
```