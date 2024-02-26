## Links
[Leetcoce](https://leetcode.com/problems/subsets-ii/)

## Expected Output
List of All subsets

## Dry Run:
```
1.
nums = [1, 1, 1, 1]
op = [[], [1], [1, 1], [1, 1, 1], [1, 1, 1, 1]]

2.
nums = [1, 2, 2]
op = [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]

```

## Approach
**Core Logic:**
The loop & recurion relation with `start` & `i` can be better understood with `dry-run` example 1

## Questions
1. Why is sorting necessary?
   - Yes, w.r.t to logic we've written it is necessary to sort the array cuz the sorted array property that two same numbers are adjacent in an array we skip such values which are same as the previous value
2. Why did you use `i > start && nums[i] == nums[i - 1]`, how does it help filter duplicates?

**Approach**
```
class Solution {

    private void subsets(int[] nums, int start, int N, List<Integer> subset, List<List<Integer>> allSubset) {
        allSubset.add(new ArrayList<>(subset));

        for(int i = start; i < N; i++) {
            // skips the same intergers & only the unique intergers get picked
            if( i > start && nums[i] == nums[i-1]) {
                continue;
            }
            subset.add(nums[i]);
            subsets(nums, i + 1, N, subset, allSubset);
            subset.remove(Integer.valueOf(nums[i]));
        }
    }

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> allSubset = new ArrayList<>();
        List<Integer> subset = new ArrayList<>();
        
        Arrays.sort(nums);
        int N = nums.length;

        subsets(nums, 0, N, subset, allSubset);

        return allSubset;
    }
}
```

## Python

```
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = []
        nums.sort()

        def dfs(start, sub):
            res.append(sub.copy())

            for i in range(start, N):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                sub.append(nums[i])
                dfs(i + 1, sub)
                sub.remove(nums[i])
        
        dfs(0, [])

        return res
```