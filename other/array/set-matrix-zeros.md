## Links
[Leetcode](https://leetcode.com/problems/set-matrix-zeroes)

## Expected Output

### Brute Force

**Approach**

**Efficiency**:
- Time: `O(m * n)`, m = no of rows, n = no of cols
- Space: `O(m * n)`, m = no of rows, n = no of cols

**code**:
```
class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        row, col = len(mat), len(mat[0])
        i, j = 0, 0

        init_zero = set()

        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    init_zero.add((r, c))

        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0 and (r, c) in init_zero:
                    # set row
                    for i in range(col):
                        mat[r][i] = 0

                    # set col
                    for i in range(row):
                        mat[i][c] = 0
```

### Optimized
- code is self explanatory

**Approach**

**Efficiency**:
- Time: `O(m * n)`, m = len(rows), n = len(cols)
- Space: `O(m + n)`, m = len(row), n = len(col)

**code**:
```
class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        m, n = len(mat), len(mat[0])

        row = [False] * m
        col = [False] * n

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    row[i] = True
                    col[j] = True
        
        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    mat[i][j] = 0
```