class Solution:
    def isPalindrome(self, s, i, j):
        j = j - 1

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True

    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n == 1:
            return s

        res = [0, ""]

        for i in range(n):
            for j in range(i+1, n):
                if self.isPalindrome(s, i, j) and ((j - i + 1) > res[0]):
                    res = [j -i + 1, s[i:j]]
        
        return res[1]

print(Solution().longestPalindrome("a"))