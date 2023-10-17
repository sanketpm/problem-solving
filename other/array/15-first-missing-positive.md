## Links
[Leetcode](https://leetcode.com/problems/first-missing-positive/description/)

## Expected Output
Smallest Missing Positive Number

## Brute Force Approach
1. HashSet
2. Return the missing element from 1 to N + 1

## Optimized Approach
1. Using index as indicator

**Brute force**
```
class Solution {
    public int firstMissingPositive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        int n = nums.length;

        for(int i = 0; i < n; i++) {
            set.add(nums[i]);
        }

        for(int i = 1; i <= n + 1; i++) {
            if( !set.contains(i) ) {
                return i;
            }
        }

        return 1;
    }
}
```

**Optimized Approach**
```
class Solution {
    public int firstMissingPositive(int[] A) {
        int n = A.length;

        for(int i = 0; i < n; i++) {
            if( A[i] < 0 ) {
                A[i] = 0;
            }
        }

        int idx = 0;
        for(int i = 0; i < n; i++) {
            idx = Math.abs(A[i]);

            if( 1 <= idx && idx <= n) {
                if( A[idx - 1] > 0 ) {
                    A[idx - 1] *= -1;
                } 
                else if(A[idx - 1] == 0){
                    A[idx - 1] = -1 * (n + 1);
                }
            }
        }

        for(int i = 0; i < n; i++) {
            System.out.print(A[i]+" ");
        }

        for(int i = 1; i < n + 1; i++) {
            if( A[i - 1] >= 0 ) {
                return i;
            }
        }

        return n + 1;
    }
}
```
