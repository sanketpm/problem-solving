## Links
[GFG](https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1)

## Expected Output
Sorted Array

**Dry run**:
```
[2,0,2,1,1,0]
[2, 1, 0]

edge case: [1, 2, 0]
```

## Brute Force Approach
1. Use Any sorting method

## Optimized Approach
1. Have 3 Pointer L: Left, M: Mid, R: Right
2. Loop while: `M < R`
   1. If `( arr[M] == 0 )` => Swap (M, L, arr); Increment thier position by 1 (++L, ++M)
   2. If `( arr[M] == 1 )` => Increment M position by 1
   3. If `( arr[M] == 2 )` => Swap (M, R, arr); Decrement R by 1 (--R)

**Brute force**
```
class Solution
{
    public static void sort012(int a[], int n)
    {
        Arrays.sort(a);
    }
}
```

**Optimized Approach**
```
class Solution
{
    private static void swap(int i, int j, int[] arr) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    public static void sort012(int a[], int n)
    {
        int L = 0;
        int R = n - 1;
        int M = 0;
        
        while( M <= R ) {
            if( a[M] == 0 ) {
                swap(M, L, a);
                ++M;
                ++L;
            } else if( a[M] == 1 ) {
                ++M;
            } else if( a[M] == 2 ) {
                swap(M, R, a);
                --R;
            }
        }

    }
}
```