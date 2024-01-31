## Links
[gfg](https://www.geeksforgeeks.org/problems/stock-span-problem-1587115621/1)

## Expected Output

### Optimized
**Approach**
1. Nearest Greater Left modified
2. Put the indexes of `nearest greater left` into the result array
3. Final result = at each `res[i] = abs(res[i] - i)`

Edge Case: Element which have no greater elements to its left:
```
# all elements to the left + itself
res[i] = i + 1
```

**Efficiency**:
- Time: `O(N)`, Where N is .
- Space: `O(N)`, Where N is

**code**:
```
import collections

class Solution:
    def calculateSpan(self,A,n):
        res = [0] * len(A)
        stk = collections.deque()
        
        for i in range(len(A)):
            while stk and A[i] >= A[stk[-1]]:
                stk.pop()
            
            if not stk:
                res[i] = i
            else:
                res[i] = stk[-1]
            
            stk.append(i)
        
        for i in range(len(A)):
            res[i] = abs(i - res[i])

            # Why? cuz here there is no nearest greater to its left then, `no of elements to left` + `itself` is the answer 
            if res[i] == 0:
                res[i] = i + 1
            
        return res
```

