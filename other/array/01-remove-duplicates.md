## Expected Output
Length of the array after the duplicates are removed

## Hints
1. No need to remove the duplicates and create a unique array
2. Need to return only unique elements since after removing duplicates only unique elements remain

## Approach
1. Count the number of unique elements in the array
2. If two adjacent elements are not equal then `++uniqueElementCount`
2. Return `uniqueElementCount + 1` to consider the last element

```
class Result {
    public static int remove_dupli(List<Integer> arr) {
        int nUnique = 0;
        int LIST_SIZE = arr.size();
        
        if(LIST_SIZE == 0 || LIST_SIZE == 1) {
            return LIST_SIZE;
        }
        
        for(int i = 0; i < LIST_SIZE-1; i++) {
            if( arr.get(i) != arr.get(i+1)) {
                ++nUnique;
            }
        }
        
        return nUnique + 1;
    }

}
```