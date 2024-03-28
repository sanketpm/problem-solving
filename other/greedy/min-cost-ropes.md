## Links
[GFG](https://www.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1)

## Expected Output

```
Input:
    N = 4
    arr[] = {4, 3, 2, 6}
Output: 
    29

Explanation:
Joining two ropes of least length:
    2, 3 = 5    [2, 3, 4, 6]
    4, 5 = 9    [4, 5, 6]
    6, 9 = 15   [6, 9]

    all ropes joined [15]
```

### Approach
1. Join two ropes of min_length, do this while the `no_of_ropes > 1`
2. Min heap to efficiently get min_length ropes

**Efficiency**:
- Time:
  - creating + heapifying = O(N)
  - while loop: iterated `n - 1` times + adding new elements into heap `logN` = O(NlogN) 
  - Total = O(N) + O(NlogN)
  - `O(NlogN)`

- Space:
  - min_heap : O(N)
  - `O(N)`

**code**:
```
import heapq

class Solution:
    def minCost(self,arr,n) :
        min_heap = [ arr[i] for i in range(n) ]
        heapq.heapify(min_heap)
        
        min_cost = 0
        while len(min_heap) > 1:
            r1 = heapq.heappop(min_heap)
            r2 = heapq.heappop(min_heap)
            
            min_cost += (r1 + r2)
            
            heapq.heappush(min_heap, r1 + r2)
        
        return min_cost
```