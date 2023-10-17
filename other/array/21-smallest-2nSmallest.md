## Expected Output
Return smallest & 2nd smallest element from the array

## Hint
1. None

## Approach
1. If element is `smaller than min1` => replace min1.
2. If element  is `not smaller than min1` but `smaller than min2` => replace min2

```
class Result {
    public static List<Integer> minAnd2ndMin(int n, List<Integer> arr) {
        int min1 = Integer.MAX_VALUE;
        int min2 = Integer.MAX_VALUE;
        
        int elem = 0;
        for(int i = 0; i < n; i++) {
            elem = arr.get(i);
            
            if( elem < min1 ) {
                min1 = elem;
            } else if ( elem > min1 && elem < min2) {
                min2 = elem;
            }
        }
        
        return Arrays.asList(min1, min2);
    }

}
```