'''
        (0)
     /   |  \\
    /    |   \\
   /     |     \\
(1)     (2)     (3)     (5)
  \\
    \\
      \\
       (4)

DFS: [0, 1, 4, 2, 3, 5]
BFS: [0, 1, 2, 3, 4, 5]

note: (5) disconnected node (edge case)
'''

# Given
V = 5
mat = [
    [1, 1, 1, 1, 0, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1]
]

def depthFirstSearch():
    vis = set()
    res = []

    def dfs(node):
        vis.add(node)
        res.append(node)

        for ver in range(V):
            if ver not in vis and mat[node][ver] == 1:
                dfs(ver)
    
    for v in range(V):
        if v not in vis:
            dfs(v)
    
    print(res)

depthFirstSearch()