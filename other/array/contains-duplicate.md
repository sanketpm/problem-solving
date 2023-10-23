## Links
[Leetcode](https://leetcode.com/problems/contains-duplicate/)

## Expected Output

### Brute Force

**Time Complexity:** 
    - `O(N^2)`, Where N is length or array
**Auxiliary Space:** 
    - `O(1)`

**code**:
```
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        
        return False
```

### Optimized
**Approach**

**Time Complexity:** 
    - `O(N)`, Where N is length of array
**Auxiliary Space:** 
    - `O(N)`, Where N is the size of HashSet

**code**:
```
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        dup = set()

        for i in range(n):
            if nums[i] in dup:
                return True
            
            dup.add(nums[i])
            
        return False
```