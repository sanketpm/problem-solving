## Links
[Leetcode](https://leetcode.com/problems/word-search/)

## Expected Output

## Brute Force Approach

## Optimized Approach

**Brute force**
```
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        # tracking visited paths
        path = set()

        dir = [[1, 0],[-1, 0],[0, 1], [0, -1]]

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if (
                r< 0 or r >= ROWS or 
                c < 0 or c >= COLS or
                word[i] != board[r][c] or
                (r,c) in path 
            ):
                return False

            path.add((r,c))

            res = False 
            for d in dir:
                res = res or dfs(r+d[0], c + d[1], i + 1)

            path.remove((r,c))

            return res
        

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        
        return False
```

**Optimized Approach**
```
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        wordLen = len(word) 

        vis = set()

        def dfs(r, c, i):
            if i == wordLen:
                return True

            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] != word[i] or
                (r,c) in vis
            ):
                return False
            
            vis.add((r,c))

            res = (
                    dfs(r + 1, c, i + 1) or 
                    dfs(r - 1, c, i + 1) or 
                    dfs(r, c + 1, i + 1) or 
                    dfs(r, c - 1, i + 1)
                )

            vis.remove((r,c))
            return res

            return res
        

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        
        return False
        
```