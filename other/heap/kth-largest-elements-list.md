## Links
[GFG](https://practice.geeksforgeeks.org/problems/k-largest-elements3736/1)

## Expected Output
List of K largest elements

### Brute Force
1. Sort the array & return elements from `n - k + 1` to `n`

### Optimized
1. Use min-heap to filter out n - k elements by popping them out when `heap_size > k`, there by elements remaining in heap will the max ones

**Approach**
```
class Solution {
    public static ArrayList<Integer> kLargest(int arr[], int n, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        for(int i = 0; i < n; i++) {
            pq.offer(arr[i]);
            
            if( pq.size() > k) {
                pq.poll();
            }
        }
        
        ArrayList<Integer> res = new ArrayList<>();
        while( !pq.isEmpty() ) {
            res.add(0, pq.poll());
        }
        
        return res;
    }
}
```