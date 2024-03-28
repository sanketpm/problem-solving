## Links
[GFG](https://www.geeksforgeeks.org/problems/maximum-meetings-in-one-room/1)

## Expected Output

```
start[] = [8, 0, 1, 5, 3, 5]
end[]   =  [9, 6, 2, 9, 4, 7]
op = 4

```

### Greedy

**Efficiency**:
- Time: `O(N*logN)`, Where N is .
- Space: `O(N)`, Where N is

**code**:
```
class Solution:
    def maxMeetings(self, N : int, S : List[int], F : List[int]) -> List[int]:
        meetings = [ [S[i], F[i], i] for i in range(N) ]
        meetings.sort(key = lambda x : x[1])

        res = []
        prev_end = -1
        
        for start, end, meet_id in meetings:
            if start > prev_end:
                res.append(meet_id + 1)
                prev_end = end
        
        return sorted(res)
```

Note:
`if meetings[i][0] > prev_end:`: current meeting start_time must be strictly greater than the previous_meeting_end_time else the meeting cannot start.