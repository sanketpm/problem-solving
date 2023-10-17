## Links
[Leetcode](https://leetcode.com/problems/n-queens/description/)

## Expected Output
Boards where n queens on an n x n chessboard are placed such that no two queens attack each other

## Optimized Approach
1. Use DFS

## Questions:
1. What approach of finding is used in this?
    - DFS - Depth First Search
2. Time Complexity?
    - O(N!)
3. Space Complexity?
    - O(N^2)

**Optimized Approach**
```
class Solution {

    private void recordBoard(char[][] board, List<List<String>> res) {
        List<String> snap = new ArrayList<>();

        for(char[] arr: board) {
            String s = new String(arr);
            snap.add(s);
        }

        res.add(snap);
    }

    private boolean isValidCell(int row, int col, int n, char[][] board) {
        int _row = row;
        int _col = col;

        // Left
        while( _col >= 0 ) {
            if( board[_row][_col] == 'Q' ) {
                return false;
            }
            _col--;
        }
        // Diagonal up
        _row = row;
        _col = col;
        
        while( _row >= 0 && _col >= 0 ) {
            if( board[_row][_col] == 'Q' ) {
                return false;
            }
            _row--;
            _col--;
        }
        // Diagoanal down
        _row = row;
        _col = col;

        while( _row < n && _col >= 0 ) {
            if( board[_row][_col] == 'Q' ) {
                return false;
            }
            _row++;
            _col--;
        }

        return true;
    }

    private void solveNQueens(int col, int n, char[][] board, List<List<String>> res) {
        if( col == n ) {
            recordBoard(board, res);
            return;
        }

        for(int row = 0; row < n; ++row) {
            if( isValidCell(row, col, n, board) ) {
                board[row][col] = 'Q';
                solveNQueens(col + 1, n, board, res);
                board[row][col] = '.';
            }
        }
    }
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> res = new ArrayList<>();
        char[][] board = new char[n][n];

        for(char[] arr: board) {
            Arrays.fill(arr, '.');
        }

        solveNQueens(0, n, board, res);

        return res;
    }
}
```