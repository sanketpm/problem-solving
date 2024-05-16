class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        cnt = 0

        vis = [False] * n

        def dfs(node):
            vis[node] = True

            for idx, val in enumerate(isConnected[node]):
                if val == 1 and not vis[idx]:
                    dfs(idx)

        for i in range(n):
            if not vis[i]:
                dfs(i)
                cnt += 1
        
        return cnt
    
res = Solution().findCircleNum([[1,0,0],[0,1,0],[0,0,1]])
print(res)