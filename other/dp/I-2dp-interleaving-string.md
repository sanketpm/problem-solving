## links
[leetcode](https://leetcode.com/problems/interleaving-string/description/)

## expected output
Can `s1` and `s2` maintain their relative order & mix-together to form `s3`

**Observations:**
- Relative order of `s1` & `s2` must be maintained in `s3`
- When verifying `s3`, the index if `s3` is equal to `i + j`
- len(s1) + len(s2) => len(s3)

## Recursive approach

```
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)

        def dfs(i, j):
            if i == l1 and j == l2 and i + j == l3:
                return True
            
            if i + j >= l3:
                return False 

            if i < l1 and s1[i] == s3[i + j] and dfs(i + 1, j):
                return True
            
            if j < l2 and s2[j] == s3[i + j] and dfs(i, j + 1):
                return True
            
            return False 

        return dfs(0, 0)
```

## memoization - top down

```
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)

        dp = {}

        def dfs(i, j):
            // base case
            if i == l1 and j == l2 and i + j == l3:
                return True
            
            // edge case
            if i + j >= l3:
                return False

            if (i, j) in dp:
                return dp[(i, j)]

            iSelect =  i < l1 and s1[i] == s3[i + j] and dfs(i + 1, j)
            jSelect = j < l2 and s2[j] == s3[i + j] and dfs(i, j + 1)

            dp[(i, j)] = iSelect or jSelect
            
            return dp[(i, j)] 

        return dfs(0, 0)
```

**Questions:**
1. How/Why `i + j` == index of s3
2. Explain base case & edge case
3. Can the solution also be memoized?
4. Time complexity??

**Mistakes I made:**
1. Forgot about edge base