## Links
[Leetcode](https://leetcode.com/problems/largest-rectangle-in-histogram/description/)

## Expected Output

### Brute Force
**Dry Run:** 
```
heights = [6, 2, 5, 4, 5, 2, 6]
output: 12
```

### Optimized
**Approach**

**Efficiency**:
- Time: `O(N)`, Where N is .
- Space: `O(N)`, Where N is

**code**:
```
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        nsl = [0] * n
        nsr = [0] * n
        max_area = 0

        stk = collections.deque()

        for i in range(n):
            while stk and heights[stk[-1]] >= heights[i]:
                stk.pop() 
            
            if not stk:
                nsl[i] = -1
            else:
                nsl[i] = stk[-1]   
            
            stk.append(i)

        stk.clear()

        for i in range(n - 1, -1, -1):
            while stk and heights[stk[-1]] >= heights[i]:
                stk.pop() 
            
            if not stk:
                nsr[i] = n
            else:
                nsr[i] = stk[-1]   
            
            stk.append(i)

        for i in range(n):
            max_area = max(max_area, (abs(nsl[i] - nsr[i]) - 1) * heights[i])
        
        return max_area
```
