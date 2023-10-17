## Expected Output
Index at which target elements exists or will exist if not present in array

## Hints
1. Array is sorted (can utilize Binary Search)

## Approach
1. Binary till you reach the break point `(high - low == 1?)`
2. Check if target is equal to lower index
3. If **equal** return `lower index`, if **not equal** then return `higher index`

```
class Result {

    private static int findIndex(List<Integer> arr, int low, int high, int target) {
        if( high - low == 1) {
            if( arr.get(low) == target ) 
                return low;
            
            return high;
        }

        int mid = low + (high - low) / 2;
        
        int midVal = arr.get(mid);
        
        if( midVal == target ) {
            return mid;
        }
        
        if( target < midVal ) {
            return findIndex(arr, low, mid, target);
        }
        
        // target > midVal
        return findIndex(arr, mid, high, target);
    }

    public static int search_pos(List<Integer> arr, int target) {
        int LIST_SIZE = arr.size();
        
        int firstElement = arr.get(0);
        int lastElement = arr.get(LIST_SIZE - 1);
        
        if( target < firstElement) {
            return 0;
        }
        
        if( target > lastElement) {
            return LIST_SIZE;
        }
        
        if(LIST_SIZE == 0 || LIST_SIZE == 1) {
            return 0;
        }
        
        return findIndex(arr, 0, LIST_SIZE - 1, target);
    }
}
```