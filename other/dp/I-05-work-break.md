## links
[leetcode](https://leetcode.com/problems/word-break/description/)

## Expected Output


## Recursive Approach

```
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        def dfs(s):
            if len(s) == 0:
                return True
            
            for i in range(n):
                if s[:i] in wordDict and dfs(s[i:]):
                    return True
            
            return False
        
        return dfs(s)
```

## Memoization - Top_Down

```
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        dp = {}

        def dfs(s):
            if len(s) == 0:
                return True
            
            if s in dp:
                return dp[s]
            
            for i in range(n + 1):
                if s[:i] in wordDict and dfs(s[i:]):
                    dp[s] = True
                    return True
            
            dp[s] = False
            return False
        
        return dfs(s)
```

## Tabulation - Bottom up

```
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        dp = [False] * (n + 1)

        dp[0] = True

        for i in range(1, n + 1):
            for w in wordDict:
                if i - len(w) >= 0 and dp[i - len(w)] and s[i - len(w): i] == w:
                    dp[i] = True
                
                if dp[i]:
                    break
        
        return dp[n]
```

**Edge Case:**
```
Input:
    word = 'a'
    wordDict = ['a']

Output:
    True

```

**Questions**
1. Why use:
```
if dp[i]:
    break
```
the next work in the wordDict can make `dp[i] = False`, therefore as you encounter dp[i] = True, break the wordDict for-loop

2. Why return dp[n] not dp[0] ?
    - dp[n] represents input string `s`

3. What dp[0] represent?
    - empty string

4. Why is dp[0] = True?
