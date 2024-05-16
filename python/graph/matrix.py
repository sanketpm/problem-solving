import collections

mat = [
    [1, 1, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 1, 1, 1, 1],
]

def bfs():
    V = len(mat)
    res, vis = [], set()
    q = collections.deque()

    q.append(0)
    vis.add(0)

    while q:
        node = q.popleft()
        res.append(node)

        for ver in range(V):
            if mat[node][ver] == 1 and ver not in vis:
                vis.add(ver)
                q.append(ver)
    return res

print(bfs())


def depth_first_search():
    V = len(mat)
    res, vis = [], set()

    def dfs(node):
        vis.add(node)
        res.append(node)

        for ver in range(V):
            if mat[node][ver] == 1 and ver not in vis:
                dfs(ver)
    
    dfs(0)
    return res

print(depth_first_search())

