## Links
[Leetcode](https://leetcode.com/problems/3sum/description/)

## Expected Output

**Dry run**
```
[-1, 0, 1, 2, 1, -1, 4, -1]

[-2, -2, -2, -1, -1, -1, 0, 0, 0, 2, 2, 2, 2]

```

### Brute Force
1. i -> n - 2
2. j -> n - 1
3. k -> n
4. check if `a[i] + a[j] + a[k] == 0`, 
   1. sort the list & add them to a `set` (avoiding duplicates)

```
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Set<List<Integer>> resultSet = new HashSet();
        int n = nums.length;

        for(int i = 0; i < n - 2; i++)
            for(int j = i + 1; j < n - 1; j++)
                for(int k = j + 1; k < n; k++) 
                    if(nums[i] + nums[j] + nums[k] == 0) {
                        List<Integer> list = new ArrayList<>(Arrays.asList(nums[i], nums[j], nums[k]));
                        Collections.sort(list);
                        resultSet.add(list);
                    }

        return new ArrayList<>(resultSet);
    }
}
```
T = O(n ^ 3)
S = O ( no of triplets )

### Better
1. Additive inverse property ( a + b + c = 0, then c = -( a + b) )
2. `-(A[i] + A[j]) = X`, this X is also present in hashset 
- If such a combination occurs record the three values (A[i], A[j], X), 
- If X doesn't exist then put A[j] into the set & let `j` move to the next element
3. Clear the set after every n traversal of j

**Approach**
```
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Set<List<Integer>> res = new HashSet<>();
        Set<Integer> inverse = new HashSet<>();
        int n = nums.length;

        for(int i = 0; i < n; i++) {
            for(int j = i + 1; j < n; j++) {
                int inv = -(nums[i] + nums[j]);
                
                if( inverse.contains(inv) ) {
                    List<Integer> list = new ArrayList<>(List.of(nums[i], nums[j], inv));
                    Collections.sort(list);
                    res.add(list);
                }
                inverse.add(nums[j]);
            }
            inverse.clear();
        }

        List<Integer> = new ArrayList<>(res);
        return res;
    }
}
```
T = O(N ^ 2) (j loop can store all the elements from `i + 1` to `n` in worst case)
S = O(N) + O(no of triplets) * 2 
whey `*2` inverse & res both store triplets

What we did in this better solution?
- Removed the third nested loop
- Reduced the complexity by N times N^3 to N^2

### Optimised
1. Based on Two-sum-ii
2. Sort the array
3. 

**dry run**
nums[] = {-1, -1, -1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3};

```
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        int n = nums.length;

        for(int i = 0; i < n; i++) {
            if( i > 0 && nums[i] == nums[i-1]) {
                continue;
            }

            int j = i + 1;
            int k = n - 1;

            while( j < k ) {
                int sum = nums[i] + nums[j] + nums[k];

                if(sum < 0) {
                    ++j;
                } else if( sum > 0) {
                    --k;
                } else {
                    List<Integer> list = new ArrayList<>(List.of(nums[i], nums[j], nums[k]));
                    res.add(list);
                    ++j;
                    --k;

                    while(j < k && nums[j] == nums[j - 1]) {
                        ++j;
                    }

                    while(j < k && nums[k] == nums[k + 1]) {
                        --k;
                    }
                }
            }
        }
        return res;
    }
}
```


## Python

### Brute Force
```
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        
        return [list(val) for val in res]
```

### Optimised
- Additive Inverse 

```
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        inverse = set()
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                sum = -(nums[i] + nums[j])

                if sum in inverse:
                    res = sorted([nums[i], nums[j], sum])
                    triplets.add(tuple(res))

                inverse.add(nums[j])
            inverse.clear()
        
        return [list(val) for val in triplets]
```
