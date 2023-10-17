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

**Fails-1**:

```
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int):
        freq_map = Counter(nums)

        q = [] 

        for key in freq_map.keys():
            q.append((key, freq_map[key]))

        heapq.heapify(q)

        res = []

        for i in range(k):
            res.append(heapq.heappop(q)[0])

        return res


# nums = [1, 1, 1, 2, 2, 3]
nums = [4,1,-1,2,-1,2,3]
print(Solution().topKFrequent(nums, 2))
```

1. Heapify - based on indexed value not frequency, therefore -1, 1 will appeart at the top, irrespective of the freq. value

**Passes 1**
T = O(N * logN) 
S = 

```
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(lambda: 0)
        hp = [] 
        res = []

        for num in nums:
            freq_map[num] += 1

        for key in freq_map.keys():
            hp.append((freq_map[key] * -1, key))

        heapq.heapify(hp)

        for i in range(k):
            res.append(heapq.heappop(hp)[1])

        return res
```