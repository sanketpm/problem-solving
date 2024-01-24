## Links
[Leetcode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)

## Expected Output
Array of two element indexes when added produce the sum

## Brute Force
Normal Two sum approach using HashMap & `diff`
> Write the code for this & then optimise

## Optimised Approach
1. Two pointer
2. `A[i] + A[j]` > target : --j
3. `A[i] + A[j]` < target : ++i
4. `A[i] + A[j]` == target : record the i & j return the result
 
**Approach**
```
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        int i = 0;
        int j = n - 1;

        while( i < j ) {
            if( nums[i] + nums[j] > target) {
                --j;
            }

            if( nums[i] + nums[j] < target) {
                ++i;
            }

            if(nums[i] + nums[j] == target) {
                return new int[]{i+1, j+1};
            }
        }

        return new int[]{-1, -1};
    }
}
```

## Python
```
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            sum = numbers[i] + numbers[j] 

            if sum == target:
               return [i + 1, j + 1]
            elif sum > target:
                j -= 1
            else:
                i += 1
                
        return [0, 0]
```