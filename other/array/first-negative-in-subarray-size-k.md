## Links
[GFG](https://www.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1)

## Expected Output

### Optimized

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
    
    while r < N:
        if A[r] < 0:
            q.append(A[r])
        
        if (r - l + 1) == K:
            if q:
                res.append(q[0])
                if A[l] == q[0]:
                    q.popleft()
            else:
                res.append(0)

            l += 1
        
        r += 1
    
    return res
```