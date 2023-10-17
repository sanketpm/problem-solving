## Links
[Leetcode](https://leetcode.com/problems/number-of-islands/description/)

## Expected Output

## Approach
- Modified No of provinces + 1-degree BFS (up, right, bottom, right) cells

**Approach**
```
class Solution {

    class Pair {
        int r;
        int c;

        public Pair(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }

    private boolean isValidCell(char[][] grid, int[][] visited, int row, int col, int m, int n) {
        return row >= 0 && row < n && col >= 0 && col < m && visited[row][col] == 0 && grid[row][col] == '1';
    }

    private void bfs(int ro, int co, int[][] visited, char[][] grid, int n, int m) {
        visited[ro][co] = 1;

        Queue<Pair> q = new LinkedList<Pair>();
        q.add(new Pair(ro, co));

        while( !q.isEmpty() ) {
            int row = q.peek().r;
            int col = q.peek().c;
            q.remove();

            // top & bottom cell
            for(int i = -1; i <= 1; i++ ) {
                if( i == 0 ) continue;

                if( isValidCell( grid, visited, row + i, col, m, n) ) {
                    visited[row + i][col] = 1;
                    q.add(new Pair(row + i, col));
                }
            }

            // left & right cell
            for(int j = -1; j <= 1; j++) {
                if( j == 0 ) continue;

                if( isValidCell( grid, visited, row, col + j, m, n) ) {
                    visited[row][col + j] = 1;
                    q.add(new Pair(row, col + j));
                }
            }
        }
    }

    public int numIslands(char[][] grid) {
        int n = grid.length;    // row
        int m = grid[0].length; // col

        int[][] visited = new int[n][m];

        int cnt = 0;

        for(int row = 0; row < n; row++) {
            for(int col = 0; col < m; col++) {
                if( grid[row][col] == '1' && visited[row][col] == 0 ) {
                    ++cnt;
                    bfs(row, col, visited, grid, n, m);
                }
            }
        }

        return cnt;
    }
}
```

### Python:
**DFS**
```
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        visited = set()

        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(row, col):
            if (
                row >= ROWS
                or row < 0
                or col >= COLS
                or col < 0
                or grid[row][col] != "1"
                or (row, col) in visited
            ):
                return

            visited.add((row, col))
            for d in dir:
                dfs(row + d[0], col + d[1])


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    count += 1
        return count
```