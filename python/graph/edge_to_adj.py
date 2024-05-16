from collections import defaultdict

class Solution:
    def getAdjList(self, edges: list[list[int]], V: int) -> dict[int: list[int]]:
        adj = defaultdict(lambda: [])

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        return adj

edges = [ [1, 2], [1, 3], [1, 4], [2, 5], [3, 5], [4, 5] ]
print(Solution().getAdjList(edges, 0))
