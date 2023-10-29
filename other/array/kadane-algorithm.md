## Links
[coding_ninjas](https://www.codingninjas.com/codestudio/problems/630526)

## Expected Output
Maximum sum of a contiguous subarray

## Brute Force
1. Use Two loops
2. Outer Loop holds the start index
3. Inner loop holds the end index (begins at start-index)
   1. Calculate the sum at each cell in `sum`
   2. Record the max at each cell in `max`

> NOTE: Reset sum = 0 before every executing of inner loop

**Dry run**
```
arr = [4, -1, 2, -7, 3, 4]
```


**code**
```
public static long maxSubarraySum(int[] arr, int n) {
    long max = Long.MIN_VALUE;
    long sum = 0;

    for(int i = 0; i < n; i++) {
        sum = 0;
        for(int j = i; j < n; j++) {
            sum = sum + arr[j];

            max = Math.max(sum , max);
        }
    }

    return max > 0? max: 0;
}
```

## Optimized Approach - Kadane's Algorithm
- meh : max ending here
- msf : max so far
1. At every cell
   1. Add it's value to `meh`
   2. Store the max value `meh + arr[i]` or `arr[i]` in meh
   3. Store the max value `meh` or `msf` in msf
2. return `msf`

> `meh`: at any cell if the cell value is greater then `meh + arr[i]` it resets to that cell

**code**
```
public static long maxSubarraySum(int[] arr, int n) {
    if( n == 0 ) {
        return 0;
    }

    long meh = arr[0];
    long msf = arr[0];

    for(int i = 1; i < n; i++) {
        meh = meh + arr[i];
        meh = Math.max(meh, arr[i]);
        msf = Math.max(msf, meh);
    }

    return msf > 0? msf : 0;
}
```