## Links
[Leetcode](https://leetcode.com/problems/valid-sudoku/submissions/1154896062/)

## Expected Output

### Brute Force
**Approach**:
1. Check whole row
2. Check whole column
3. for 3x3 cells, split the whole table into 9 bigger cells it will effectively put into one of 9 bigger cells:
    [1, 1]  => [1/3, 1/3] => [0, 0]
    [2, 2]  => [2/3, 2/3] => [0, 0]

    [0, 0] represents 3x3 block for the cells 00, 01, 02, 10, 11, 12, 20, 21, 22, divide all the cells by 3 you will get (0, 0)

    similarly,
    [3, 3]  => [3/3, 1/3] => [1, 1]
    [5, 5]  => [5/3, 5/3] => [1, 1]

    [1, 1] represents 3x3 block for cells 33 34 35, 43 44 45, 53, 54 55


**Time Complexity:** 
- `O(N)`, Where N is ..\

**Auxiliary Space:**
- `O(N)`, due to ...

**code**:
```
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(lambda: set())
        cols = collections.defaultdict(lambda: set())
        squares = collections.defaultdict(lambda: set())

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                if ( board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[r//3, c//3] ):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        
        return True
```