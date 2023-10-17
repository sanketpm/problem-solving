## Links
[Leetcode](https://leetcode.com/problems/delete-operation-for-two-strings/)
[GFG](https://practice.geeksforgeeks.org/problems/minimum-number-of-deletions-and-insertions0209/1)

## Expected Output
Total count of insertions and deletions to convert String s1 to String s2

## Approach
1. Find the LCS
2. Deletions = Str1.length - lcs
3. Insertions = Str2.length - lcs
4. Return `Insertions + deletions`

**Tabulation - Bottom Up**
```
class Solution
{
	public int minOperations(String str1, String str2) 
	{ 
	    int m = str1.length();
	    int n = str2.length();
	    
	    int[][] dp = new int[m + 1][n + 1];
	    
	    for(int i = 1; i < m + 1; i++) {
	        for(int j = 1; j < n + 1; j++) {
	            if( str1.charAt(i - 1) == str2.charAt(j - 1)) {
	                dp[i][j] = 1 + dp[i - 1][j - 1];
	            } else {
	                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
	            }
	        }
	    }
	    
	    int lcs = dp[m][n];
	    int deletions = m - lcs;
	    int insertions = n - lcs;
	    
	    return insertions + deletions;
	} 
}
```