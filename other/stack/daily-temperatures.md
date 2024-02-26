## Links
[Leetcode](https://leetcode.com/problems/daily-temperatures/description/)

## Expected Output

### Optimized
**Dry run:**
```
Example 1:
    Input: temperatures = [73,74,75,71,69,72,76,73]
    Output: [1,1,4,2,1,1,0,0]

Example 2:
    Input: temperatures = [30,40,50,60]
    Output: [1,1,1,0]

Example 3:
    Input: temperatures = [30,60,90]
    Output: [1,1,0]

```

**Approach**
1. Find Nearest Greater Right
2. Subtract the NGR_Index with current index => Answer we need (Next day where tempeerature is greater)

**Efficiency**:
- Time: `O(N)`, Where N is .
- Space: `O(N)`, Where N is

**code**:
```
class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stk = collections.deque()
        n = len(temp)
        res = [0] * n
        
        for i in range(n - 1, -1, -1):
            while stk and temp[i] >= temp[stk[-1]]:
                stk.pop()
            
            if not stk:
                res[i] = i
            else:
                res[i] = stk[-1]
            
            stk.append(i)
        
        for i in range(n):
            res[i] = abs(i - res[i])
        
        return res
```