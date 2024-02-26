## Links
[Leetcode](https://leetcode.com/problems/permutations/)

## Expected Output
List of all permutations

## Approach - Recursive
1. Use list to store to dynamic values
2. Every Recusion: traverse array from 0th index
   1. If the element exists in list move to next index - (use a boolean array or check the list itself)
   2. If them element doesnt exist
      1. add to the list
      2. recur
   3. When you reach a recusion base condition where list-size == array.size - store the list

> DFS with a dynamic list which stores & pops the values on go & result is stored when list.size becomes equal to array size

![permuation-i](../../images/permutation-i.svg)

**Approach_1**
```
class Solution {

    private void permute(int[] nums, int N, boolean[] used, List<Integer> list, List<List<Integer>> res) {
        if( list.size() == N ) {
            res.add(new ArrayList<>(list));
            return;
        }

        for(int i = 0; i < N; i++) {
            if( used[i] ) {
                continue;
            }

            used[i] = true;
            list.add(nums[i]);

            permute(nums, N, used, list, res);

            used[i] = false;
            list.remove(list.size() - 1);
        }
    }

    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> list = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        
        permute(nums, nums.length, used, list, res);

        return res;
    }
}
```

**Approach_2**
```
class Solution {

    private void permute(int[] nums, int N, List<Integer> list, List<List<Integer>> res) {
        if( list.size() == N ) {
            res.add(new ArrayList<>(list));
            return;
        }

        for(int i = 0; i < N; i++) {
            if( list.contains(nums[i])) {
                continue;
            }

            list.add(nums[i]);

            permute(nums, N, list, res);

            list.remove(list.size() - 1);
        }
    }

    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> list = new ArrayList<>();
        
        permute(nums, nums.length, list, res);

        return res;
    }
}
```


## Python

**Approach: Using visited set**
```
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)

        res = []
        vis = set()
        sub = collections.deque()

        def dfs():
            if len(sub) == N:
                res.append(sub.copy())
                return
            
            for i in range(N):
                if i in vis:
                    continue

                vis.add(i)
                sub.append(nums[i])
                
                dfs()

                sub.pop()
                vis.remove(i)

        dfs()

        return res
```

**Approach: Using Swap**

```
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(start):
            if start == n:
                res.append(nums.copy())
                return
            
            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]
                dfs(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        
        dfs(0)
        return res
```