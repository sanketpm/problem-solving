## Links
[Leetcode](https://leetcode.com/problems/regular-expression-matching)

## Expected Output
True: Valid Regex (Regex can represent the given string `s`)
False: Invalid Regex (Regex cannot represent the given string `s`)

**Algorithm:**
Decision Tree depends on curr_char_match & pattern-string-next-char

1. pattern-string, If next char is `*`, you have 2 choices:
    a.     take_star = curr_char_match && dfs(i + 1, j) // we consider current char match & increment it by by        
    b. dnt_take_star = dfs(i, j + 1) // no need of curr_char_match since, we're changing the index of pattern string

2. Current char Match
```
curr_char_match = i < m and (s[i] == p[j] or p[j] == '.')
```

**Recursive**
```
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        def dfs(i, j):
            if i == m and j == n:
                return True
            
            if j >= n:
                return False
            
            first_match = i < m and (s[i] == p[j] or p[j] == '.')

            next_match = False

            if j + 1 < n and p[j + 1] == '*':
                takeStar =  first_match and dfs(i + 1, j)
                dntTakeStar = dfs(i, j + 2) 

                next_match = takeStar or dntTakeStar
            else:
                next_match = first_match and dfs(i + 1, j + 1)
            
            return next_match
        
        return dfs(0, 0)
```

**Memoization - Top Down**
```
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        dp = {}

        def dfs(i, j):
            if i == m and j == n:
                return True
            
            if j >= n:
                return False
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            first_match = i < m and (s[i] == p[j] or p[j] == '.')

            next_match = False

            if j + 1 < n and p[j + 1] == '*':
                takeStar = dfs(i, j + 2) 
                dntTakeStar =  first_match and dfs(i + 1, j)
                next_match = takeStar or dntTakeStar
            else:
                next_match = first_match and dfs(i + 1, j + 1)
            
            dp[(i, j)] = next_match

            return dp[(i, j)]
        
        return dfs(0, 0)
```