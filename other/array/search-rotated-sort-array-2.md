## Links
[Leetcode](https://leetcode.com/problems/search-in-rotated-sorted-array/)

## Expected Output
Target element's index

## Brute Force
Linear Search
T = O(N)

## Optimised
Modified Binary Search

**Code**
```
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            while l < r and nums[l] == nums[l + 1]:
                l += 1
            
            while l < r and nums[r] == nums[r - 1]:
                r -= 1

            mid = (l + r) // 2

            if nums[mid] == target:
                return True
            
            elif nums[l] <= nums[mid]:
                if nums[l] <= target and target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
```

**Extensions**
- code:
```
while l < r and nums[l] == nums[l + 1]:
    l += 1

while l < r and nums[r] == nums[r - 1]:
    r -= 1
```
| What is does? Skips the duplicates elements for each iterations


**Needs imporvement**
1. Debugging
2. Expalaning capacity