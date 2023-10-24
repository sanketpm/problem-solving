## Links
[Leetcode](https://leetcode.com/problems/permutations-ii/)

## Expected Output

## Approach
1. Same as permutation 1 but add a result_list check
   1. If a list exists in result_list don't add it to the result

## Questions
1. Why use used[] boolean array?
2. Why `pop the last element` why not remove the value that was added in the loop?

**Approach**
```
class Solution {
    private void permuteUnique(int[] nums, int N, boolean[] used,List<Integer> list, List<List<Integer>> res) {
        if(list.size() == N && !res.contains(list)) {
            res.add(new ArrayList<>(list));
        }

        for(int i = 0; i < N; i++) {
            if( used[i] ) {
                continue;
            }

            used[i] = true;
            list.add(nums[i]);

            permuteUnique(nums, N, used, list, res);

            used[i] = false;
            list.remove(list.size() - 1);
        }
    }
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> list = new ArrayList<>();

        boolean[] used = new boolean[nums.length];

        permuteUnique(nums, nums.length, used, list, res);

        return res;
    }
}
```

## Python

```
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        
        res = []
        vis = set()
        lst = collections.deque()

        def dfs():
            if len(lst) == N and lst not in res:
                res.append(lst.copy())
                return
            
            for i in range(N):
                if i in vis:
                    continue
                
                vis.add(i) 
                lst.append(nums[i])
                dfs()

                lst.pop()
                vis.remove(i)
            
        dfs()

        return res
```