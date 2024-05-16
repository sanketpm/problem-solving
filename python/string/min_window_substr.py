from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        tmap = Counter(t)
        smap = {}

        have, need = 0, len(t)

        minLen = float('inf')
        substr = [-1, -1]

        l, r = 0, 0

        while r < len(s):
            if s[r] in tmap:
                smap[s[r]] = 1 + smap.get(s[r], 0)

                if smap[s[r]] == tmap[s[r]]:
                    have += 1
            
            while need == have:
                winLen = r - l + 1

                if winLen < minLen:
                    minLen = winLen
                    substr = [l, r + 1]
                
                if s[l] in tmap:
                    smap[s[l]] -= 1

                    if smap[s[l]] < tmap[s[l]]:
                        have -= 1
                
                l += 1
            r += 1
        
        if minLen == float('inf'):
            return ""
        
        return s[substr[0]:substr[1]]

res = Solution().minWindow("aa", "aa")
print(res)