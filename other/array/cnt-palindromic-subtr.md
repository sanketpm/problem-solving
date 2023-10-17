## Links
[Leetcode](https://leetcode.com/problems/palindromic-substrings/)

## Expected Output
No of palindromic substrings

## Approach
1. Left & right step wise comparison

### Brute Force
**Approach**:
1. Generate all substrings
2. count the no of palindromes - checking each substring

**code**
```
```

### Optimized
**Approach**
1. At each index - traverse left & right
```
// To check at odd indexes 
l, r = i, i

// To check at even indexes
l, r = i, i + 1
```


**code**
```
class Solution:
    def cntPalindrome(self, s: str, l: int, r: int, n: int) -> int:
        count = 0
        while l >= 0 and r < n and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        
        return count

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        for i in range(n):
            count += self.cntPalindrome(s, i, i, n)
            count += self.cntPalindrome(s, i, i + 1, n)
        
        return count
```
