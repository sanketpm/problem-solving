from collections import defaultdict

class Solution:
    def dfs(self, )
    def fn(self, edges: list[list[int]], V: int) -> int:
        adj = defaultdict(lambda: [])

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        print(adj)

        vis = [False] * V + 1

        for i in range(1, V+1):
            if not vis[i]:
                dfs(i)        

        return 0


edges = [ [1, 2], [1, 3], [1, 4], [2, 5], [3, 5], [4, 5] ]
print(Solution().dfs(edges, 0))
