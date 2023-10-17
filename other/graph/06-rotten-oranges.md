## Links
[Leetcode](https://leetcode.com/problems/rotting-oranges/description/)
[GFG](https://practice.geeksforgeeks.org/problems/rotten-oranges2536/1)

## Expected Output
Time consumed to convert fresh oranges to rotten oranges

## Approach
1. Modified BFS - With a Time Counter

>NOTE:\
> grid[nrow][ncol] == 1 => Is Fresh?\
> grid[nrow][ncol] == 2 => Is Rotten?\
> !visited[nrow][ncol] -=> Is Unvisted?

**Logic to note**
1. time = Math.max(time, p.time);
2. drow & dcol
3. ++fresh and ++rotten and rotten == fresh?

**code**
```
class Solution
{
    class Pair {
        int row;
        int col;
        int time;

        Pair(int row, int col, int time) {
            this.row = row;
            this.col = col;
            this.time = time;
        }
    }
    
    private boolean isInBounds(int row, int col, int n, int m) {
        return row >= 0 && row < n && col >= 0 && col < m;
    }
    
    public int orangesRotting(int[][] grid)
    {
        int n = grid.length;
        int m = grid[0].length;

        int[] drow = {-1, 0, 1, 0};
        int[] dcol = {0, 1, 0, -1};

        boolean[][] visited = new boolean[n][m];
        Queue<Pair> q = new LinkedList<>();
        
        int time = 0;
        
        int rotten = 0;
        int fresh = 0;

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if( grid[i][j] == 2 ) {
                    q.add(new Pair(i, j, 0));
                    visited[i][j] = true;
                }
                
                if(grid[i][j] == 1) {
                    ++fresh;
                }
            }
        }

        while( !q.isEmpty() ) {
            int size = q.size();
            Pair p = q.poll();
            time = Math.max(time, p.time);
            
            // time = t.time;
            // for(int j = 0; j < size; j++) {  // causes TLE
                for(int i = 0; i < 4; i++) {
                    int nrow = p.row + drow[i];
                    int ncol = p.col + dcol[i];

                    if( isInBounds(nrow, ncol, n, m) && grid[nrow][ncol] == 1 && !visited[nrow][ncol]) {
                        q.add(new Pair(nrow, ncol, p.time + 1));
                        visited[nrow][ncol] = true;
                        grid[nrow][ncol] = 2;
                        ++rotten;
                    }
                }
            // }
        }

        return fresh == rotten? time : -1;
    }
}
```