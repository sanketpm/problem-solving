## Links
[Leetcode](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)

## Expected Output
Kth smallest element

**dry run**
```
    arr[]: [ 1  3  2  5  4 ]
    index:   0  1  2  3  4
    n = 5
    k = 2
```

### Brute Force
1. sort the array
2. return `n - k`th element

```
class Solution {
    public int findKthLargest(int[] nums, int k) {

        int n = nums.length;

        Arrays.sort(nums);

        return nums[n - k];
    }
}
```

### Better
**I. Min Heap**
1. Put all elements into the Priority Queue: top->[ 1, 2, 3, 4, 5 ]
2. Pop `n - k` times

```
class Solution {
    public int findKthLargest(int[] nums, int k) {
        int n = nums.length;
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for(int i = 0; i < n; i++) {
            pq.offer(nums[i]);
        }

        int res = 0;
        for(int i = 0; i <= n - k; i++) {
            res = pq.poll();
        }

        return res;
    }
}
```

**II. Max Heap**
1. Put all elements into the Priority Queue: top->[ 5, 4, 3, 2, 1 ]
2. Pop `k` times

T = O( n * log k)
S = O( k )

```
class Solution {
    public int findKthLargest(int[] nums, int k) {
        int n = nums.length;
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

        for(int i = 0; i < n; i++) {
            pq.offer(nums[i]);
        }

        int res = 0;
        for(int i = 0; i < k; i++) {
            res = pq.poll();
        }

        return res;
    }
}
```

## Optimised
> Note: K + Largest => min heap
1. Use a `Min Heap` with size = k
2. All the larger elements will settle kind of at the base as you keep putting the element into the heap
3. Whenever size of heap crosses k, you can say that element present over the `line of k` are smaller than the below hence pop it out
4. Finally when array traversal in done, our heap has k elements
5. Poll() the top element - that is our result => `kth largest element`

```
class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for(int i = 0; i < nums.length; i++) {
            pq.offer(nums[i]);

            if( pq.size() > k) {
                pq.poll();
            }
        }

        return pq.peek();
    }
}
```