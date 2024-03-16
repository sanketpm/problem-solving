## Links
[GFG](https://practice.geeksforgeeks.org/problems/topological-sort/1)

## Expected Output
List of Topologically sorted nodes

## Topological Sort
For every node (u, v), u appears in any traversal before v
- We can topological sort of any DAGs (Directed Acyclic Graph)

**dry run**
![image](../../images/topological-sort.png)
![image](../../images/topological-sort-1.png)

```
Output:

5 4 2 3 1 0
```

## Approach
1. DFS Traversal
2. Use a stack 
   1. when you reach a node where you cannot dfs to any other node -> push it into stack
3. Once you return to the main function: pop() stack elements & record them into a list, this list contains the topologically sorted nodes

**Approach**
```
class Solution
{
    static void toposort(int currNode, boolean[] visited, LinkedList<Integer> stk, ArrayList<ArrayList<Integer>> adj ) {
        visited[currNode] = true;
        
        for(int neighbour : adj.get(currNode)) {
            if( !visited[neighbour] ) {
                toposort(neighbour, visited, stk, adj);
            }
        }
        
        stk.push(currNode);
    }

    static int[] topoSort(int n, ArrayList<ArrayList<Integer>> adj) {
        boolean[] visited = new boolean[n];
        LinkedList<Integer> stk = new LinkedList<>();
        
        for(int i = 0; i < n; i++) {
            if(!visited[i]) {
                toposort(i, visited, stk, adj);
            }
        }
        
        int[] res = new int[stk.size()];
        int i = 0;
        while( !stk.isEmpty() ) {
            res[i++] = stk.pop();
        }
        
        return res;
    }
}
```

## Python

```
import collections

class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    vis = set()
	    q = collections.deque()
	    
	    def bfs(ver):
    	    q.append([ver, -1])
    	    vis.add(ver)
    	    
    	    while q:
    	        node, src = q.popleft()
    	        
    	        for nb in adj[node]:
    	            if nb not in vis:
    	                q.append([nb, node])
    	                vis.add(nb)
    	            elif nb != src:
    	                return True
	   
            return False
        
        
        for v in range(V):
            if v not in vis and bfs(v):
                return True
        
        return False
```

## Debugging

1. Failed to consider that input can be a disconnected graph (forgot the for-loop check for all vertices)
2. 