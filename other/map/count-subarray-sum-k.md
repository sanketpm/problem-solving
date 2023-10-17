## Links
[Leetcode]()

## Expected Output
Count of subarrays with sum k

### Brute Force
1. `i` holds the startIndex
2. `j` holds the endIndex
3. `k` iterates from `i` to `j` & calculates the `sum`
4. check if sum == k, if `yes` increment the count

T = O(n^3)
O = O(1)

```

```

### Brute Force Optimised
1. `i` holds the startIndex
2. `j` holds the endIndex
3. `sum` is calculated for every `j` iteration & `count` is incremented `sum == k`

```

```

### Optimized

> If prefixSum exist in the map, then subarray with sum k also exist

**dry run**
[1, 2, 3, -3, 1, 1, 1, 1, 4, 2, -2]
[0, 0, 3]

**Approach**
```

```

**Questions**
1. Why put `(0, 1)` in map
2. Difference between `sum` and `prefixSum`
3. How is this kind of related to `Two sum`