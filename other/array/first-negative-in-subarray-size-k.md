## Links
[GFG](https://www.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1)

## Expected Output

### Optimized
**Dry run**
```
A[] = [-8, 2, 3, -6, 10], K = 2
```

**Approach**
- Sliding window

**Efficiency**:
- Time: `O(N)`, 
- Space: `O(k)`, size of q, when all integers are negative

**code**:
```
import collections

def printFirstNegativeInteger( A, N, K):
    l, r = 0, 0
    res = []
    q = collections.deque()
    
    for r in range(len(A)):
        if A[r] < 0:
            q.append(A[r])
        
        if (r - l + 1) == K:
            res.append(q[0] if q else 0)

            if q and A[l] == q[0]:
                q.popleft()
            l += 1
        
    return res
```