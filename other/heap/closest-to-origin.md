## Links
[Leetcode](https://leetcode.com/problems/k-closest-points-to-origin/)

## Expected Output

## Approach
1. Closest distance to origin => distance between the points & origin must be minimum. Therefore, we can safely say we need to use `Max Heap`. (k + Smallest => Max Heap)

**Priority Queue - Comparator**
```
PriorityQueue<Tuple> pq = new PriorityQueue<Tuple>( (a, b) -> -(a.dist - b.dist) );
```

**Approach**
```
class Solution {
    class Tuple {
        int dist;
        int[] coor = new int[2];

        Tuple(int _dist, int _x, int _y) {
            dist = _dist;
            coor[0] = _x;
            coor[1] = _y;
        }
    }
    private int distance(int x, int y) {
        return x*x + y*y; 
    }

    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<Tuple> pq = new PriorityQueue<Tuple>( (a, b) -> -(a.dist - b.dist) );

        for(int[] coor : points) {
            pq.offer(new Tuple(distance(coor[0], coor[1]), coor[0], coor[1]));

            if( pq.size() > k ) {
                pq.poll();
            }
        }

        int[][] res = new int[k][2];

        int i = 0;
        while( !pq.isEmpty() ) {
            Tuple t = pq.poll();
            res[i][0] = t.coor[0];
            res[i][1] = t.coor[1];
            i++;
        }

        return res;
    }
}
```