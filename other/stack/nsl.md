## Links
[gfg](https://www.geeksforgeeks.org/problems/smallest-number-on-left3403/1?)

## Expected Output

### Brute Force

**Approach**

**Efficiency**:
- Time: `O(N)`, Where N is .
- Space: `O(N)`, Where N is

**code**:
```
import collections

class Solution:
    def leftSmaller(self, n, A):
        stk = collections.deque()
        res = [0] * len(A)
        
        for i in range(len(A)):
            while stk and A[i] <= stk[-1]:
                stk.pop()
            
            if not stk:
                res[i] = -1
            else:
                res[i] = stk[-1]
            
            stk.append(A[i])
        
        return res
```