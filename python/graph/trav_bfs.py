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

import collections

V = 5
mat = [
    [1, 1, 1, 1, 0, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1]
]

def breadthFirstSearch():
    vis = set()
    res = []
    q = collections.deque()

    def bfs(node):
        q.append(node)
        vis.add(node)

        while q:
            node = q.popleft()
            res.append(node)

            for ver in range(V):
                if ver not in vis and mat[node][ver] == 1:
                    vis.add(ver)
                    q.append(ver)
    
    for v in range(V):
        if v not in vis:
            bfs(v)
    
    print(res)
    
breadthFirstSearch()
