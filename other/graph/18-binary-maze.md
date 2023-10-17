## Links
[GFG](https://practice.geeksforgeeks.org/problems/shortest-path-in-a-binary-maze-1655453161/1)

## Expected Output
Shortest Path : in integers

## Approach
1. Modified Djikstra 
   1. Use Queue instead of Priority Queue
   2. `dist[][]` is used to track the distance from source to each cell once the destination is reached distance in that cell updated & returned.

**Approach**
```
class Solution {
    
    class Tuple {
        int dist;
        int row;
        int col;
        
        Tuple(int _dist, int _row, int _col) {
            dist = _dist;
            row = _row;
            col = _col;
        }
    }
    
    boolean isValidCell(int row, int col, int n, int m, int[][] grid) {
        return row >= 0 && row < n && col >= 0 && col < m && grid[row][col] == 1;
    }

    int shortestPath(int[][] grid, int[] src, int[] tar) {
        
        if(src[0] == tar[0] && src[1] == tar[1]) {
            return 0;
        }
        
        int n = grid.length;
        int m = grid[0].length;
        
        
        int[][] dist = new int[n][m];
        
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                dist[i][j] = Integer.MAX_VALUE;
            }
        }
        
        Queue<Tuple> q = new LinkedList<>();
        dist[src[0]][src[1]] = 0;

        q.add(new Tuple(0, src[0], src[1]));
        
        int[] drow = {0 , -1, 0, +1};
        int[] dcol = {1, 0, -1, 0};
        
        while( !q.isEmpty() ) {
            Tuple cell = q.poll();
            
             for(int i = 0; i < 4; i++) {
                 int _row = cell.row + drow[i];
                 int _col = cell.col + dcol[i];
                 
                 int newDist = cell.dist + 1;
                 
                 if(isValidCell(_row, _col, n, m, grid) && (newDist < dist[_row][_col]) ) {
                    dist[_row][_col] = newDist;
                    if( _row == tar[0] && _col == tar[1]) {
                        return newDist;
                    }
                    q.add(new Tuple(newDist, _row, _col));
                 }
    
             }
        }
        
        return -1;
    }
}
```

**Code**
1. Update cell's new distance (line 70)
2. `row >= 0 && row < n && col >= 0 && col < m && grid[row][col] == 1`
    - row >= 0 `greater or equal`