## Links
[Leetcode](https://leetcode.com/problems/flood-fill/description/)

## Expected Output
Modified array

## Approach
1. Modified DFS/BFS

**Approach**
```
class Solution {

    private boolean isInBounds(int row, int col, int n, int m) {
        return row >= 0 && row < n && col >= 0 && col < m;   
    }

    private void dfs(int[][] image, int row, int col, int initColor, int newColor) {
        image[row][col] = newColor;

        int[] delRow = {-1, 0, 1, 0};
        int[] delCol = {0, 1, 0, -1};
        int n = image.length;
        int m = image[0].length;

        for(int i = 0; i < 4; i++) {
            int nrow = row + delRow[i];
            int ncol = col + delCol[i];

            // check valid cell
            if( !isInBounds(nrow, ncol, n, m)){
                continue;
            }
            // check valid color
            if( image[nrow][ncol] == initColor && image[nrow][ncol] != newColor ) {
                dfs(image, nrow, ncol, initColor, newColor);
            }
        }
    }

    public int[][] floodFill(int[][] image, int sr, int sc, int color) {

        dfs(image, sr, sc, image[sr][sc], color);

        return image;
    }
}
```