## Links
[Leetcode](https://leetcode.com/problems/word-search/)

## Approach
- DFS

```
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(word)
        rows, cols = len(board), len(board[0])
        vis = set()

        def outOfRange(r, c):
            return r < 0 or c < 0 or r >= rows or c >= cols

        def dfs(r, c, i):
            if i == n:
                return True
            
            if outOfRange(r, c):
                return False
            
            if (r, c) in vis:
                return False
            
            if board[r][c] != word[i]:
                return False
            
            vis.add((r, c))

            res = (
                dfs(r, c + 1, i + 1) or
                dfs(r + 1, c, i + 1) or
                dfs(r, c - 1, i + 1) or
                dfs(r - 1, c, i + 1)
            )

            vis.remove((r, c))

            return res
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        return False
```

**Questions:**
1. What happens if you don't remove element from set `vis.remove((r,c))`?
2. What happends if you remove outOfRange?
3. Why do you need to check if an element is already visited?