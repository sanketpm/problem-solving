class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def isPalindrome(i, j) -> str:
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            
            return s[i+1:j]
        
        res = ''
        for i in range(n):
            oddPalin = isPalindrome(i, i)
            evenPalin = isPalindrome(i, i + 1)

            reslen = len(res)

            if len(oddPalin) > reslen:
                res = oddPalin
            elif len(evenPalin) > reslen:
                res = evenPalin
            
        return res

res = Solution().longestPalindrome("bb")