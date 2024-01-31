## Links
[GFG](https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1)

## Expected Output

```
nums = [1, 3, 2, 4]

nums = [ 6 8 0 1 3 ]

```


### Optimized
**Approach**

**Time Complexity:** 
    - `O(N)`
**Auxiliary Space:** 
    - `O(N)`

**code**:
```
from collections import deque

class Solution:
    def nextLargerElement(self,arr,n):
        res = [-1] * len(arr)
        stk = deque()
        
        for i in range(len(arr) - 1, -1, -1):
            while stk and arr[i] >= stk[-1]:
                stk.pop()
        
            if not stk:
                res[i] = -1
            else:
                res[i] = stk[-1]
            
            stk.append(arr[i])
        
        return res
```