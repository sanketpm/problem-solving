## Expected Output
Index of two elements when added equals to target

## Hints
1. Array is sorted (can utilize `Two Pointer`);

## Approach
1. Point L, R at 0th and Last Index and sum them
2. Based on the sum move the pointers

Follow the code, it is self-explanatory.

```
class Result {

    public static List<Integer> twoSum(int target, int n, List<Integer> arr) {
        int l = 0;
        int r = n - 1;
        
        int sum = 0;

        while(l < r) {
            sum = arr.get(l) + arr.get(r);

            if( sum == target ) {
                return Arrays.asList(l+1, r+1);
            } 
            
            if( sum < target) {
                ++l;
            } 
            else {
                --r;
            }
        }
        
        return new ArrayList();
    }

}
```