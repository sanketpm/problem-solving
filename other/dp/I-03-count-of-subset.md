## Links
[GFG](https://practice.geeksforgeeks.org/problems/perfect-sum-problem5633/1)

## expected output


**Edge Case:**
We miss out reading the problem carefully, the given array contains `non-negative numbers`,
- `non-negative numbers` -> fancy of saying that array contains **ZERO (0)**

If we dont consider the case:
- [ 0 ] -> we return 1
- [ 0 ] -> we must return `2` because `{}` & `{0}`

## Recursive approach

```
class Solution:
	def countSubset(self, arr, n, sum):
        if sum == 0 and n == 0:
            return 1

		if n == 0:
		    return 0
                    
        dntTake = self.countSubset(arr, n - 1, sum)
        
        take = 0
        if arr[n - 1] <= sum:
            take = self.countSubset(arr, n - 1, sum - arr[n - 1])
        
        return take + dntTake

	def perfectSum(self, arr, n, sum):
	    return self.countSubset(arr, n, sum) % ((10 ** 9 + 7))
```

## Memoization - top down

```
class Solution:
	def countSubset(self, arr, n, sum, dp):
        if sum == 0 and n == 0:
            return 1

		if n == 0:
		    return 0
                    
        if (n, sum) in dp:
            return dp[(n, sum)]
        
        dntTake = self.countSubset(arr, n - 1, sum, dp)
        
        take = 0
        if arr[n - 1] <= sum:
            take = self.countSubset(arr, n - 1, sum - arr[n - 1], dp)
        
        dp[(n, sum)] = take + dntTake
        
        return dp[(n, sum)]


	def perfectSum(self, arr, n, sum):
	    dp = {}
	    return self.countSubset(arr, n, sum, dp) % ((10 ** 9 + 7))
```

## Tabulation - bottom up

```

```