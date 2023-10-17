## Links
[Leetcode](https://leetcode.com/problems/word-break/description/)

## Expected Output
True: If the given word (split or non-split) exist in the wordDict

## Recursive Approach


```
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        def check(s):
            if len(s) == 0:
                return True
            
            for i in range(n + 1):
                if s[:i] in wordDict and check(s[i:]):
                    return True

            return False
        
        res = check(s)
        return res
```

## Tabulation - Bottom Up

```
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i: i + len(w)]==w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]        
```