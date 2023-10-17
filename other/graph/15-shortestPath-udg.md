## Links
[coding_ninjas](https://www.codingninjas.com/codestudio/problems/shortest-path-in-an-unweighted-graph_981297)

## Expected Output
Shortest path list from start node to end node

## Approach
1. Have a `parent[]` - to track parent nodes
2. Have a `visited[]` - to track visited nodes
3. Do a simple BFS

> Idea: Shortest Path will be first one to reach the target node
> Using target & source node with parent[] we can easily get the path

**Approach**
```
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.Queue;

public class Solution {

	public static LinkedList<Integer> shortestPath(int[][] edges, int n, int m, int s, int t) {
		ArrayList<ArrayList<Integer>> adj = new ArrayList<ArrayList<Integer>>();
		
		for(int i = 0; i <= n; i++) {
			adj.add(new ArrayList<>());
		}

		for(int[] edge : edges) {
			int u = edge[0];
			int v = edge[1];

			adj.get(u).add(v);
			adj.get(v).add(u);
		}

		boolean[] visited = new boolean[n + 1];
		int[] parent = new int[n + 1];
		Queue<Integer> q = new LinkedList<>();
		
		visited[s] = true;
		parent[s] = -1;
		q.add(s);
		

		while( !q.isEmpty() ) {
			int node = q.poll();

			for(int nb : adj.get(node)) {
				if( !visited[nb] ) {
					visited[nb] = true;
					parent[nb] = node;
					q.add(nb);
				}
			}
		}

		LinkedList<Integer> ans=new LinkedList<>();
		while(t != s) {
			ans.add(t);  
			t = parent[t];   
		}  
		ans.add(s);

		Collections.reverse(ans);  
		return ans;
	}
}
```