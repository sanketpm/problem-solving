## Links
[Leetcode](https://leetcode.com/problems/two-sum/description/)

## Expected Output
Indexes of two values in array when summed equals the target

## Brute Force Approach
1. Nested Loop the array
2. At each index calculate the sum with all other indexes
   1. If the sum match the target => return the two indexes
   2. If the loop ends without a match return null

Code: Self Explainatory

## Optimized Approach
1. Use Map to record the `value: index`
2. At every index : check if the `compliment` exists in the Map
    - If exists: return the indexes
    - If no match found: return null

*Note: Comliment = target - nums[i];*

**Brute force**
```
class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        for(int i = 0; i < nums.length; i++) {
            for(int j = 0; j < nums.length; j++) {
                if( i !=j && nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }

        return null;
    }
}
```

**Optimized Approach**
```
class Solution {
    public int[] twoSum(int[] nums, int target) {

        Map<Integer, Integer> map = new HashMap<>();
        int compliment = 0;

        for(int i = 0; i < nums.length; i++) {
            compliment = target - nums[i];

            if( map.containsKey(compliment) ) {
                return new int[]{map.get(compliment), i};
            }

            map.put(nums[i], i);
        }

        return null;
    }
}
```