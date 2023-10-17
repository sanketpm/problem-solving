## Links
[Leetcode](https://leetcode.com/problems/number-of-provinces/description/)

## Expected Output
No of disconnected components in a graph

## Approach
1. Modified BFS/DFS Traversal

**Approach**
```
class Solution {

    private void dfs(int node, int[][] isConnected, boolean[] visited) {
        visited[node] = true;

        for(int i = 0; i < isConnected[node].length; i++) {
            if( isConnected[node][i] == 1 && !visited[i] ) {
                dfs(i, isConnected, visited);
            }
        }
    }

    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        boolean[] visited = new boolean[n];
        int noOfProvinces = 0;

        for(int i = 0; i < n; i++) {
            if( !visited[i] ) {
                ++noOfProvinces;
                dfs(i, isConnected, visited);
            }
        }

        return noOfProvinces;
    }
}
```

**Python**
```
class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        cnt = 0

        vis = [False] * n

        def dfs(node):
            vis[node] = True

            for idx, val in enumerate(isConnected[node]):
                if val == 1 and not vis[idx]:
                    dfs(idx)

        for i in range(n):
            if not vis[i]:
                dfs(i)
                cnt += 1
        
        return cnt
    
res = Solution().findCircleNum([[1,0,0],[0,1,0],[0,0,1]])
print(res)
```