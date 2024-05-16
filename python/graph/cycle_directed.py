def detectCycleInDirectedGraph(n, edges):
    vis, dfsVis = set(), set()

    adj = [[] for _ in range(n)]

    for u,v in edges:
        adj[u].append(v)

    def dfsCycle(node):
        vis.add(node)
        dfsVis.add(node)

        for nb in adj[node]:
            if nb not in vis:
                if dfsCycle(nb):
                    return True
            elif nb in dfsVis:
                return True
        
        dfsVis.remove(node)
        return False

    for v in range(n):
        if v not in vis:
            if dfsCycle(v):
                return True
    
    return False

edges = [[0,1], [1,3], [3,2], [2, 0]]   # Cycle
edges = [[0, 1], [0, 2], [1, 3], [2, 3]] # No Cycle
n = 4
print(detectCycleInDirectedGraph(n, edges))