## Links
[Leetcode](https://leetcode.com/problems/top-k-frequent-elements/description/)

## Expected Output
List of most frequent elements

## Approach
1. Use Map & Heap
2. Put [elem : count] into the map
3. Since we need k most frequent number i.e., k numbers with largest frequency (k - largest => Min heap), use Min Heap
4. Min Heap stores Pair[elem : count]. Set the size of heap = k
5. All large frequency elements settle at bottom on heap stack & bigger elements lie above the `k-line`, pop them
6. The remaining elements in the PriorityQueue is our answer

T = O(N + k * log(k))
S = O(N + k)
**Approach**
```
class Solution {
    class Pair {
        int elem;
        int count;

        Pair(int _elem, int _count) {
            elem = _elem;
            count = _count;
        }
    }

    public int[] topKFrequent(int[] arr, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        PriorityQueue<Pair> pq = new PriorityQueue<>((a, b) -> a.count - b.count);
        int[] res = new int[k];

        for(int e : arr) {
            map.put(arr[e], map.getOrDefault(arr[e], 0) + 1);
        }

        for(int key : map.keySet()) {
            pq.offer(new Pair(key, map.get(key)));

            if(pq.size() > k) {
                pq.poll();
            }
        }

        for(int i = 0; i < k; i++) {
            res[i] = pq.poll().elem;
        }

        return res;
    }
}
```

### Python

**Heap Solution**
T = O(n * logn) (n elements into min-heap * popping k elements from heap (logn) )
S = O(N)

```
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)

        heap = [ (freq, num) for (num, freq) in count.items() ]
        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)
        
        return [num for (freq, num) in heap]
```

Note: If you use Max-Heap the Time complexity improves to `O(k*logk) `

**Bucket Sort Modified**
T = O(N)
S = O(N)
```
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        count = collections.Counter(nums)

        for (num, fre) in count.items():
            freq[fre].append(num)

        res = [] 
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return []
```