## Links
[GFG](https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1)

## Expected Output
True: Cycle detected
False: Cycle Not detected

## Approach
1. Modified Disconnected Component 
2. DFS Traversal 
3. Neighbour-Parent condition check

nb: Neighbout

If a nb is visited, then it must be source(parent) node.
- if visited nb not the source/parent node => Cycle is detected

![image](../../images/detect-cycle-bfs-dryrun.png)
**Dry Run:**
1. Tri
2. Quad
3. Disconnected Graph

**Edge Case:**
1. Disconnected Component
 
**NOTE:**
A neighbour-node is visted IFF: That Neighbour-node is the source of my current node
```
if ( !visited[nb] ) {
  // 1. Mark as visited
  // 2. Record the parent of neighbour-node
  // 3. Insert into Queue
} else if( !(parent[currentNode] == nb) ) {
  // Cycle Detected
}
```

**Approach**
```
class Solution {
    
    private boolean detectCycle(int V, int src, boolean[] visited, ArrayList<ArrayList<Integer>> adj) {
        int[] source = new int[V];
        Queue<Integer> q = new LinkedList<>();
        
        visited[src] = true;
        source[src] = -1;
        q.add(src);
        
        while( !q.isEmpty() ) {
            int node = q.poll();
            
            for(int nb : adj.get(node) ) {
                if( !visited[nb] ) {
                    visited[nb] = true;
                    source[nb] = node;
                    q.add(nb);
                } else if( source[node] != nb ){
                    return true;
                }
            }
        }
        return false;
    }
    
    public boolean isCycle(int V, ArrayList<ArrayList<Integer>> adj) {
        boolean[] visited = new boolean[V];
        
        for(int i = 0; i < V; i++) {
            if( !visited[i]  && detectCycle(V, i, visited, adj) ) {
                return true;
            }
        }
        
        return false;
    }
}
```