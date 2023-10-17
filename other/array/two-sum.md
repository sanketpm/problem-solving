
### Brute Force
```
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        int[] res = new int[2];
        boolean found = false;

        for(int i = 0; i < n; i++) {
            for(int j = i + 1; j < n; j++) {
                if( nums[i] + nums[j] == target) {
                    res[0] = i;
                    res[1] = j;
                    found = true;
                    break;
                }
            }
            if(found) {
                break;
            }
        }

        return res;   
    }
}
```
T = O(n^2)
S = O(1)

## Optimized Approach
1. Use Map to record [ element : index ]
2. At each index check:
   1. If `diff = target - nums[i]` is present in the map
   2. If present: extract the index & return along with present index

```
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        int[] res = new int[2];

        Map<Integer, Integer> map = new HashMap<>();

        for(int i = 0; i < n; i++) {
            int diff = target - nums[i];

            if(map.containsKey(diff)) {
                res[0] = map.get(diff);
                res[1] = i;
                break;
            }
            map.put(nums[i], i);
        }

        return res;   
    }
}
```

**mistakes**
1. forgot to put the `element : index`
```
for(int i = 0; i < n; i++) {
    // calculate diff
    // check diff exist
    // put [ele : index]
}
```