class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)

        def dfs(s):
            if len(s) == 0:
                return True
            
            for i in range(n + 1):
                if s[:i] in wordDict and dfs(s[i:]):
                    return True
            
            return False
        
        return dfs(s)
    
res = Solution().wordBreak("a", ["a"])