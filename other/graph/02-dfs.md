## Links
[GFG](https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1)

## Expected Output

## Approach

>NOTE: Visualize: using Recursion Tree + visited array

**Approach - Adjacency List**
```
class Solution {
    // Function to return a list containing the DFS traversal of the graph.
    
    private void dfs(int V, int node, ArrayList<ArrayList<Integer>> adj, ArrayList<Integer> res, boolean[] visited) {
        visited[node] = true;
        res.add(node);
        
        for(int neighbour : adj.get(node) ) {
            if( !visited[neighbour] ) {
                dfs(V, neighbour, adj, res, visited);
            }
        }
    }
    
    public ArrayList<Integer> dfsOfGraph(int V, ArrayList<ArrayList<Integer>> adj) {
        boolean[] visited = new boolean[V];
        ArrayList<Integer> res = new ArrayList<>();
        
        dfs(V, 0, adj, res, visited);
        
        return res;
    }
}
```

**Adjacency Matrix**
```
    // node = 0;

    void dfs(int node, int[][] matrix, boolean[] visited) {
        visited[node] = true;
        
        for (int i = 0; i < matrix[node].length; i++) {

            // Are nodes connected && Is the neighbour node visited
            
            if (matrix[node][i] == 1 && !visited[i]) {
                dfs(i, matrix, visited);
            }
        
        }
    }

```

### Python
**Adjacency List**
```
class Solution:
    def dfsOfGraph(self, V, adj):
        visited = [False] * V
        res = []

        def dfs(node):
            visited[node] = True
            res.append(node)
            
            for nb in adj[node]:
                if not visited[nb]:
                    dfs(nb)
        
        dfs(0)
        
        return res
```

**Adjacency Matrix**
```
def dfs(node, matrix, vis):
    vis.add(node)

    # are `nodes connected` and Is the `neighbour node` visted
    for i in range(len(matrix[node])):
        if matrix[node][i] == 1 and i not in vis:
            dfs(i, matrix, vis)

```