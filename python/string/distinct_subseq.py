class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        def dfs(i, j):
            if i == m and j == n:
                return 1

            if i == m:
                return 0

            if s[i] == t[j]:
                take = dfs(i + 1, j + 1)
                dntTake = dfs(i + 1, j)
                return take + dntTake
            else:
                return dfs(i + 1, j)

        return dfs(0, 0)

res = Solution().numDistinct("babgbag", "bag")
print(res)