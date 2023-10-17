## Links
[Leetcode](https://leetcode.com/problems/search-in-rotated-sorted-array/)

## Expected Output
Target element's index

## Brute Force
Linear Search
T = O(N)

## Optimised
Modified Binary Search

**Observations**:
- Single ascending array is split into two ascending array now
- At any given iteration of binary search, `mid` will either lie on first-array(Array-I) or second-array(Array-II)
- At any given iteration target will lie between (start------mid) or (mid-----end), based on where the target lies update the start & end pointers

1. Loops while start <= end
1. At any iteration if `arr[mid] == target` return `mid`
2. check if the `mid` is in first array
   1. check if the target lies in between (start--------mid) : yes => update `end` to `mid-1`
   2. update `start` to `mid+1` since the target doesn't lie between (start------mid)
3. check if the `mid` in in second array
   1. check if the target lies between (mid-----end): yes => update `start` to `mid+1`
   2. update `end` to `mid-1` since the target doesnt' lie between (mid-----end) 

T = O(logn)\
S = O(1)
```
class Solution {
    public int search(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;
        int mid = 0;

        // 1. check if `mid` is in Array-I
            // 1. check `tar` is in range
        // 2. Check if `mid` is in Array-II 
            // 1. check `tar` is in range
        while(start <= end) {
           mid = start + (end - start)/2;

           if(nums[mid] == target) {
               return mid;
           }
           if(nums[start] <= nums[mid]) {
               if(nums[start] <= target && target < nums[mid]) {
                   end = mid - 1;
               } else {
                   start = mid + 1;
               }
           } else {
               if(nums[mid] < target && target <= nums[end]) {
                   start = mid + 1;
               } else {
                   end = mid - 1;
               }
           }
        }

        return -1;
    }
}
```

**Pseudo**

**Mistakes**
1. 47: I did -> `if(nums[start] < nums[end])` it must be a `<=` comparison why?
   1. nums[start] can be nums[mid]
   2. execution will never enter the case where `nums[start] == nums[mid]` resulting in an infinite loop
2. Snippet:
```
if(nums[start] <= nums[mid]) {
    if(nums[start] <= target && target < nums[mid]) {
        end = mid - 1;
    } else {
        start = mid + 1;
    }
} else {
    if(nums[mid] < target && target <= nums[end]) {
        start = mid + 1;
    } else {
        end = mid - 1;
    }
}
```
a. Why are using `nums[start] <= target` and not `nums[start] < target`
    - if your're `nums[start] <= target` then why are we incrementing `start = mid + 1`, wont the start be incremented from `mid` & if true how are we suppose to get the correct mid, same questions for `end = mid - 1` where `target <= nums[end]`