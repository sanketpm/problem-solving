## Links
[Leetcode](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/)

## Expected Output

### Optimized
**Dry run**

```
nums = [1,5,4,2,9,9,9], k = 3

nums = [2, 2, 2], k = 3

nums = [1,1,1,7,8,9], k = 3
```

**Efficiency**:
- Time: `O(N * log(k))`, Where N is k removal operations from set
- Space: `O(N)`, case: all elements are unique & size of k is N

**code**:
```
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        uniq = set()
        l, r = 0, 0
        sum, res = 0, 0

        while r < len(nums):
            while nums[r] in uniq:
                uniq.remove(nums[l])
                sum -= nums[l]
                l += 1

            uniq.add(nums[r])
            sum += nums[r]

            if (r - l + 1) == k and len(uniq) == k:
                res = max(res, sum)
                
                sum -= nums[l]
                uniq.remove(nums[l])
                l += 1
            
            r += 1
        
        return res
```