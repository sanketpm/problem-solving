

## Expected Output
Return smallest & 2nd smallest element from the array

## Hint
1. None

## Approach
1. If element is `smaller than min1` => replace min1.
2. If element  is `not smaller than min1` but `smaller than min2` => replace min2

```
def minAnd2ndMin( nums, n):
    min1 = float('inf')
    min2 = float('inf')
    
    for el in nums:
        if el < min1:
            min2 = min1
            min1 = el
        elif el < min2 and el != min1:
            min2 = el
    
    if min2 == float('inf'):
        return [-1]
    
    return [min1, min2]
```