## Links
[GFG](https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1)

## Expected Output

```
Input: n = 6 
    arr[] = {0900, 0940, 0950, 1100, 1500, 1800}
    dep[] = {0910, 1200, 1120, 1130, 1900, 2000}

Output: 3

Explanation: 
    Minimum 3 platforms are required to  safely arrive and depart all trains.
```

### Greedy

**Efficiency**:
- Time: `O(Nlogn)`, Where N is .
- Space: `O(N)`, Where N is

**code**:
```
#Function to find the minimum number of platforms required at the
#railway station such that no train waits.

class Solution:    
    def minimumPlatform(self,n,arr,dep):
        arr.sort()
        dep.sort()
        
        count, res = 0, 0
        i, j = 0, 0
        
        while i < n:
            if arr[i] <= dep[j]:
                count += 1
                res = max(res, count)
                i += 1
            else:
                count -= 1
                j += 1
        return res
```