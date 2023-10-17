## Links
[Leetcode](https://leetcode.com/problems/jump-game-iii/description/)

## Expected Output
Can we reach an  with value 0
 yes -> 'True'
 no  -> 'False'

## Dry Run

**Example 1:**
```
Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true

Explanation: 

    All possible ways to reach at  3 with value 0 are: 
        way 1 = 5 ->  4 ->  1 ->  3 
        way 1 = 5 ->  6 ->  4 ->  1 ->  3 
```

**Example 2:**
```
Input: arr = [3,0,2,1,2], start = 2
Output: false

Explanation: 
    There is no way to reach at index 1 with value 0.

```

### Brute Force
**Approach**:
- DFS
- code is self descriptory

**CODE FAILS: Maximum Recursive Depth exceeded**
Why?
- Circular Recursive Call
- Dry run example 1 - you'll get where the circular dependency arises

**code**:
```
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)

        dp = {}

        def dfs(i):
            if i < 0 or i >= n:
                return False
            
            if arr[i] == 0:
                return True
            
            plus = dfs(i + arr[i])

            minus = dfs(i - arr[i])

            return plus or minus
        
        return dfs(start)
```

### Memoization
**Approach**
- Due to `Circular Recursive` call the Brute-force was failing
- DP'fying the `plus` and `minus` calls at each recursive call will avoid the circular recursive call

**code**:
```
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)

        dp = {}

        def dfs(i, op):
            if i < 0 or i >= n:
                return False
            
            if arr[i] == 0:
                return True
            
            if (i, op) in dp:
                return dp[(i, op)]
            
            plus = dfs(i + arr[i], '+')
            dp[(i, '+')] = plus

            minus = dfs(i - arr[i], '-')
            dp[(i, '-')] = minus

            return plus or minus
        
        return dfs(start, '')
```

**Questions**