## Links
[Leetcode](https://leetcode.com/problems/valid-palindrome)

## Expected Output

### Brute Force
**Approach**:
- Two pointer

**Time Complexity:** 
- `O(N)`

**Auxiliary Space:**
- `O(1)`

**code**:
```
class Solution:
    def isAlphaNum(self, ch):
        return (
            ord(ch) in range(ord('a'), ord('z') + 1) or 
            ord(ch) in range(ord('A'), ord('Z') + 1) or
            ord(ch) in range(ord('0'), ord('9') + 1)
        )
        
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            while i < j and not self.isAlphaNum(s[i]):
                i += 1
            while i < j and not self.isAlphaNum(s[j]):
                j -= 1
            
            if not s[i].lower() == s[j].lower():
                return False

            i += 1
            j -= 1
        
        return True
```