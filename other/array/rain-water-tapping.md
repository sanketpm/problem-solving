## Links
[Leetcode](https://leetcode.com/problems/trapping-rain-water/description/)

## Expected Output

## Brute Force
- For each cell find Left_max & Right_Max record them in seperate arrays of same size
- `Area = min(Left_Max, Right_Max) - height[i]`

```
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left = [0] * n
        right = [0] * n
        res = [0] * n

        max_cap = 0

        for i in range(n):
            left[i] = max(max_cap, height[i])
            max_cap = max(height[i], max_cap)

        max_cap = 0

        for i in range(n - 1, -1, -1):
            right[i] = max(max_cap, height[i])
            max_cap = max(height[i], max_cap)
        
        for i in range(n):
            res[i] = min(left[i], right[i]) - height[i]
        
        return sum(res)
```

## Optimized
- Two Pointer

**Dry run:**
```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Input: height = [4,2,0,3,2,5]
Output: 9
```

- Time: O(N)
- Space: O(1)

```
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)
        lmax, rmax = height[0], height[-1]
        res = 0

        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                res += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                res += rmax - height[r]
        
        return res
```
