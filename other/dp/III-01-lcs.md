## Links
[Leetcode](https://leetcode.com/problems/longest-common-subsequence/description/)
[GFG](https://practice.geeksforgeeks.org/problems/longest-common-subsequence-1587115620/1)

## Expected Output
Length of Longest Common Subsequence

## Approach
```
fn(String X, String Y, int m, int n) {
    // code
}
```
1. If X[m - 1] == Y[n - 1]
   - If the characters match:    1 + recur( X, Y, m - 1, n - 1)
2. If X[m - 1] != Y[n - 1]
   - If the characters dont match: MAX( recur(X, Y, m -1, n), recur(X, Y, m, n - 1) )
   - We recur twice:
     1. We move M by 1 character before current & match it with X[m-1] == Y[n]
     2. We move N by 1 character before current & match it with X[m] == Y[n - 1]  

## Questions:
1. What is difference between a subsequence and subtring?
   - Subsequence: Only the order matter, it doensn't matter if the characters have some other character between them
   - Substring: no spacing between characters, it is string

## Recursive Approach
Refer code - self explanatory

**Java**
```
class Solution {
    static int lcs(int x, int y, String s1, String s2) {
        if( x == 0 || y == 0 ) {
            return 0;
        }
        
        if( s1.charAt(x - 1) == s2.charAt(y - 1) ) {
            return 1 + lcs(x - 1, y - 1, s1, s2);
        } else {
            return Math.max( lcs(x - 1, y, s1, s2), lcs(x, y - 1, s1, s2) );
        }
    }
    
}
```

**Python**
```
class Solution:
    def lcs(self, text1: str, text2: str, i: int, j: int) -> int:
        if i == len(text1) or j == len(text2):
            return 0
        
        if text1[i] == text2[j]:
            return 1 + self.lcs(text1, text2, i + 1, j + 1)
        else:
            return max(self.lcs(text1, text2, i + 1, j), self.lcs(text1, text2, i, j + 1))

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.lcs(text1, text2, 0, 0);
```
## Memoization - Top Down
Refer code - self explanatory

**Java**
```
class Solution
{
    //Function to find the length of longest common subsequence in two strings.
    static int lcs(int x, int y, String s1, String s2, int[][] dp) {
        if( x == 0 || y == 0 ) {
            return 0;
        }
        
        if(dp[x][y] != -1) {
            return dp[x][y];
        }
        
        if(s1.charAt(x - 1) == s2.charAt(y - 1)) {
            return dp[x][y] = 1 + lcs(x - 1, y - 1, s1, s2, dp);
        } else {
            return dp[x][y] = 
                    Math.max(
                        lcs(x - 1, y, s1, s2, dp), 
                        lcs(x, y - 1, s1, s2, dp)
                    );
        }
    }
    
    static int lcs(int x, int y, String s1, String s2) {
        int[][] dp = new int[x + 1][y + 1];
        
        for(int[] arr: dp) {
            Arrays.fill(arr, -1);
        }
        
        return lcs(x, y, s1, s2, dp);
    }
    
}
```

**Python**
```
class Solution:
    def lcs(self, text1: str, text2: str, n: int, m: int, dp: List[List[int]]) -> int:
        if n == 0 or m == 0:
            dp[n][m] = 0
            return 0
        
        if dp[n][m] != -1:
            res = dp[n][m]
            return res
        
        if text1[n - 1] == text2[m - 1]:
            dp[n][m] = 1 + self.lcs(text1, text2, n - 1, m - 1, dp)
        else:
            dp[n][m] = max(self.lcs(text1, text2, n - 1, m, dp), self.lcs(text1, text2, n, m - 1, dp))
        
        res = dp[n][m]
        return res

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        
        dp = [ [-1 for i in range(m + 1)] for j in range(n + 1)]
        
        return self.lcs(text1, text2, n, m, dp)
```


## Tabulation - Bottom Up

**Java**
```
class Solution
{
    static int lcs(int x, int y, String s1, String s2) {
        int[][] dp = new int[x + 1][y + 1];
        
        for(int[] arr: dp) {
            Arrays.fill(arr, -1);
        }
        
        for(int i = 0; i < y + 1; i++) {
            dp[0][i] = 0;
        }
        
        for(int i = 0; i < x + 1; i++) {
            dp[i][0] = 0;
        }
        
        /**
         * x = i
         * y = j
         */
        for(int i = 1; i < x + 1; i++) {
            for(int j = 1; j < y + 1; j++) {
                if( s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        
        return dp[x][y];
    }
    
}
```

**Python**
```
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        
        dp = [ [0 for i in range(m + 1)] for j in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        res = dp[n][m]

        return res
```