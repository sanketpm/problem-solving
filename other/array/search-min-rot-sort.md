## Links
[Leetcode](https://leetcode.com/problems/search-in-rotated-sorted-array-ii)

## Expected Output
Min element in the array

## Approach
Array is rotated => Two Ascending order arrays `min` element is the `start` of 2nd array

### Brute Force
Linear Search for min element in your arrray

**Dry Run:**
```
[3, 4, 5, 1, 2]

[3, 1, 2]
```

### Optimized
**Approach**
```
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2
            res = min(res, nums[m])

            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        
        return res
```