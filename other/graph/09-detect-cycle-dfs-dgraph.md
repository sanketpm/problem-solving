## Links
[coding_ninjas](https://www.codingninjas.com/codestudio/problems/1062626)

## Expected Output
True: Cycle exist in graph
False: Cycle doesnt not exist in graph

## Approach
1. Modified DFS
2. Have a dfsVisited[] which traces the dfs_path (concept: Backtracking)
3. You reach back the same path then cycle is detected

**Core concept**
You get a cycle in DFS iff you reach back to same node who started this dfs_path

**dry run**
![image](../../images/topological-sort.png)

**Approach**
```
public class Solution {

  private static boolean dfsCycle(int currNode, boolean[] visited, 
            boolean[] dfsVisited, ArrayList<ArrayList<Integer>> adj) {

    visited[currNode] = true;
    dfsVisited[currNode] = true;

    for(int neighbour: adj.get(currNode)) {
      if( !visited[neighbour] ) {
        boolean cycleFound = dfsCycle(neighbour, visited, dfsVisited, adj);
        if( cycleFound ) {
          return true;
        }
      } else if( dfsVisited[neighbour] ){
          return true;
      }
    }

    dfsVisited[currNode] = false;
    return false;
  }
  public static boolean detectCycleInDirectedGraph(int n, ArrayList < ArrayList < Integer >> edges) {
    ArrayList < ArrayList < Integer >> adj = new ArrayList < ArrayList < Integer >>();

    for(int i = 0; i <= n; i++) {
      adj.add(new ArrayList<>());
    }

    for(int i = 0; i < edges.size(); i++) {
      int u = edges.get(i).get(0);
      int v = edges.get(i).get(1);

      adj.get(u).add(v);
    }

    boolean[] visited = new boolean[n + 1];
    boolean[] dfsVisited = new boolean[n + 1];

    for(int i = 0; i <= n; i++) {
      if( !visited[i] ) {
        boolean cycleFound = dfsCycle(i, visited, dfsVisited, adj);
        if( cycleFound ) {
          return true;
        }
      }
    }

    return false;
  }
}
```