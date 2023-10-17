
## Links
[Leetcode](https://leetcode.com/problems/number-of-1-bits)

## Expected Output
Count of 1 bits in given input

## Intuitive Approach
1. Right shift the input by 1, use `1 & 1 = 1` and `1 & 0 = 0` properties to check the LSB if 1 if yes increment the counter 

**Approach 1**
```
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0

        while n != 0:
            prod = n & 1
            n = n >> 1

            if prod == 1:
                cnt += 1
            
        return cnt
```

## Brian Kernighan Approach
1. use `n & n - 1` with counter

**Approach 2**
```
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0

        while n != 0:
            prod = n & 1
            n = n >> 1

            if prod == 1:
                cnt += 1
            
        return cnt
```