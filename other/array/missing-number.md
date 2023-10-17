## Links
[Leetcode](https://leetcode.com/problems/missing-number/description/)

## Expected Output
Given an array of size n, it will contain elements from [0, n], but one number will be missing, return that number

### Brute Force - I
1. Sort the array
2. Parse from 1 to N - 1, window size = 2, if arr[i] - arr[i - 1] != 1 => return `arr[i] + 1`

### Brute Force II
1. Create a HashMap or another boolean array of size `n`
2. Put each into put with value 1 or mark it's position in bool array as true
3. The key with value = 0 or the index with value = false => is our answer

### Optimized
1. calculate the total sum till n => (n * (n + 1)) // 2
2. Subract each element in the array from the sum, the sum remaining is our answer

**Approach**
```
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum = (n * (n + 1)) // 2

        for i in range(n):
            sum -= nums[i]
        
        return sum
```