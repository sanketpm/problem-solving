## Links
[Leetcode](https://leetcode.com/problems/counting-bits/)

## Expected Output
Given upper bound e.g.: 5
Return an array which consits of count of 1 bits for each number from 1 to 5

### Brute Force
1. Calculate the no of one bits for each number & add into array

```

```

### Optimized
1. use dp. with each offset we can divide the problem into subproblems to sove them effectively

> offset is reset to i whenever offset * 2 = i
> dp[i] == 1 + dp[i - offset]

**Approach**
```

```