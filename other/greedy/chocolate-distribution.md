## Links
[GFG](https://www.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1)

## Expected Output

```
N = 8, M = 5
A = {3, 4, 1, 9, 56, 7, 9, 12}
Output: 6
Explanation: 
    The minimum difference between maximum chocolates and minimum chocolates is 9 - 3 = 6 by choosing following M packets :{3, 4, 9, 7, 9}.
```

### Approach


**Efficiency**:
- Time:

- Space:

**code**:
```
class Solution:
    def findMinDiff(self, A,N,M):
        A.sort()
        
        i, j = 0, M - 1
        res = float('inf')
        
        while j < N:
            res = min(res, A[j] - A[i])
            i += 1
            j += 1
        
        return res
```