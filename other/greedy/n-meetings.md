## Links
[GFG](https://www.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1)

## Expected Output

```
start[] = [8, 0, 1, 5, 3, 5]
end[]   =  [9, 6, 2, 9, 4, 7]
op = 4

```

### Greedy
1. Sort the meetings [ [start[i], end[i], i], ....] based on (end[i], i), if two end match choose the one with lower `i` value (basically the meeting with shorter duration using (end[i], i) as key for sorting)
2. 

**Efficiency**:
- Time: `O(NlogN)`, Where N is .
- Space: `O(N)`, Where N is

**code**:
```
class Solution:
    def maximumMeetings(self,n,start,end):
        meetings = [ [start[i], end[i]] for i in range(n) ]
        meetings.sort(key=lambda x : x[1])
        
        res = 0
        prev_end = -1
        for start, end in meetings:
            if start > prev_end:
                res += 1
                prev_end = end
        
        return res
```

Note:
`if meetings[i][0] > prev_end:`: current meeting start_time must be strictly greater than the previous_meeting_end_time else the meeting cannot start.
