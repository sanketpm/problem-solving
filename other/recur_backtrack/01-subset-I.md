## Links
[Leetcoce](https://leetcode.com/problems/subsets/description/)

## Expected Output
List of All subsets

## Brute Force Approach

## Optimized Approach

**Brute force**
```

```

**Optimized Approach**
```
class Solution {

    private void subsets(int[] nums, int start, int N, List<Integer> subset, List<List<Integer>> allSubset) {
        
        allSubset.add(new ArrayList<>(subset));

        for(int i = start; i < N; i++) {
            subset.add(nums[i]);
            subsets(nums, i + 1, N, subset, allSubset);
            subset.remove(Integer.valueOf(nums[i]));
        }
    }

    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> allSubset = new ArrayList<>();
        List<Integer> subset = new ArrayList<>();
        
        int N = nums.length;

        subsets(nums, 0, N, subset, allSubset);

        return allSubset;
    }
}
```