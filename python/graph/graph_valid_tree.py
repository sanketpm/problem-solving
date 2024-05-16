class Solution:
    def validTree(n, edges):
        adj = {}

        for i in range(n):
            adj[i] = []
        
        for edge in edges:
            adj[edge[0]].append(edge[1])

        vis = [False] * n
        dfsVis = [False] * n
        
        def cycleDetect(node):
            vis[node] = True
            dfsVis[node] = True

            for nb in adj[node]:
                if not vis[nb]:
                    if cycleDetect(nb):
                        return True
                if dfsVis[nb]:
                    return True

            dfsVis = False
            return False
        
        res = cycleDetect(0)
        return res



n = 5
edges = [ [0, 1], [0, 2], [0, 3], [1, 4] ]
res = Solution.validTree(n, edges)

print(res)