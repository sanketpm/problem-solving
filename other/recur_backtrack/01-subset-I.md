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

## Python

```
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        N = len(nums)

        def dfs(start, sub):
            res.append(sub.copy())

            for i in range(start, N):
                sub.append(nums[i])
                dfs(i + 1, sub)
                sub.remove(nums[i])
        
        dfs(0, [])

        return res
```