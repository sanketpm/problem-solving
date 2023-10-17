
## Links
[GFG](https://practice.geeksforgeeks.org/problems/topological-sort/1)

## Expected Output
Topologically sorted list of nodes

## Approach - Kahn Algorithm
1. Modified BFS
2. Indegree[] which tracks incoming-edges to a node
3. Put All nodes in queue whose incoming edges is 0
4. Poll() the queue (record this polling order - it's the result) (viz.., node + edges are erased => incoming nodes will also be gone)
   1. Update the indegree edges
   2. If updated indegree edge for a neighbour node becomes zero - put it into queue

**dry run**
![image](../../images/topological-sort.png)

**Approach**
```
class Solution
{
    static int[] topoSort(int V, ArrayList<ArrayList<Integer>> adj) 
    {
        Queue<Integer> q = new LinkedList<>();
        int[] indegree = new int[V];
        int[] res = new int[V];

        for(int i = 0; i < V; i++) {
            for(int neighbour : adj.get(i)) {
                indegree[neighbour] += 1;
            }
        }
        
        for(int i = 0; i < V; i++) {
            if( indegree[i] == 0 ) {
                q.add(i);
            }
        }
        
        int i = 0;
        while( !q.isEmpty() ) {
            int currNode = q.poll();
            res[i++] = currNode;
            
            for(int nb : adj.get(currNode)) {
                indegree[nb] -=1;
                
                if( indegree[nb] == 0) {
                    q.add(nb);
                }
            }
            
        }
        return res;     
    }
}
```


_coding-ninjas_
```
public class Solution 
{
    public static ArrayList<Integer> topologicalSort(ArrayList<ArrayList<Integer>> edges, int v, int e) 
    {
        // 1. Create Adjacency List
        ArrayList<ArrayList<Integer>> adj = new ArrayList<ArrayList<Integer>>();

        for(int i = 0; i < v; i++) {
            adj.add(new ArrayList<>());
        }

        for(ArrayList<Integer> li : edges ) {
            int _u = li.get(0);
            int _v = li.get(1);

            adj.get(_u).add(_v);
        }

        // Populate indegree[]
        int[] indegree = new int[v];

        for(ArrayList<Integer> li : adj) {
            for(int nb : li) {
                indegree[nb] += 1;
            }
        }
        
        ArrayList<Integer> res = new ArrayList<>();
        Queue<Integer> q = new LinkedList<>();

        for(int i = 0; i < v; i++) {
            if(indegree[i] == 0) {
                q.add(i);
            }
        }

        while( !q.isEmpty() ) {
            int currNode = q.poll();
            res.add(currNode);

            for(int nb : adj.get(currNode) ) {
                indegree[nb] -= 1;
                
                if( indegree[nb] == 0 ) {
                    q.add(nb);
                }
            }
        }

        return res;
    }
}
```