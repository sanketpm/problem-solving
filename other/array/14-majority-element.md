## Expected Output
Return element that occurs more than n/2 times

## Hint
1. We need to count the times an element occurs (can utilize Map)

## Approach
1. Traverse the array and to put the key & value(default = 0).
2. If key already exits then increment it's value by 1

```
class Result {
    public static int majorityElement(int n, List<Integer> arr) {
        Map<Integer, Integer> map = new HashMap<>();

        int elem = 0;
        int nby2 = n / 2;

        for(int i = 0; i < arr.size(); i++) {
            elem = arr.get(i);
            map.put(elem, map.getOrDefault(elem, 0) + 1);
        }
        
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if(entry.getValue() > nby2) {
                return entry.getKey();;
            }
        }
        
        return -1;
    }

}
```