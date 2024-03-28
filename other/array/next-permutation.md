## Links
[Leetcode](https://leetcode.com/problems/next-permutation/description/)

## Expected Output

**Dry run**
```
nums = [1 2 4 1]
: [1, 4, 2, 1] ==> [1, 4, 1, 2]

nums = [1 2 4 3] -> [1, 2, 4, 3] 

nums = [1 3 4 2] -> [1, 4,| 3, 2] -> [1, 4, 2, 3]

nums = [4 3 2 1] -> [1 2 3 4]

nums = [1 2 3 4]

nums = [1 2 3 2 3]
```

**Edge Cases:**
```
nums = [4, 2]
op: [2, 4]

nums = [1]
op: 1
```

### Optimized
**Approach**

**Efficiency**:
- Time: `O(N)`, Where N is .
```
nums = [4 2 1 1 1] => shows the worst case complexity
```
- Space: `O(1)`

**code**:
```
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        brkpt = -1

        for i in range(n - 2, -1, -1):
            if nums[i] >= nums[i + 1]:
                continue

            brkpt = i

            for j in range(n - 1, i, -1):
                if nums[brkpt] < nums[j]:
                    nums[brkpt], nums[j] = nums[j], nums[brkpt]
                    break
            break
        nums[(brkpt + 1):] = reversed(nums[(brkpt + 1):])
```