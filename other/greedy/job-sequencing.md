## Links
[GFG](https://www.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1)

## Expected Output

```
Input:
    N = 4
    Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}

Output:
    2 60

Explanation:
    Job1 and Job3 can be done with maximum profit of 60 (20+40).

Input:
    N = 5
    Jobs = {(1,2,100),(2,1,19),(3,2,27), (4,1,25),(5,1,15)}

Output:
    2 127

Explanation:
    2 jobs can be done with maximum profit of 127 (100+27).

```

### Greedy

**Efficiency**:
- Time: `O(Nlogn)`, Where N is .
- Space: `O(N)`, Where N is

**code**:
```
# (jobId, deadline, profit)

jobs = [(1,4,20),(2,1,10),(3,1,40),(4,1,30)]

n = len(jobs)

jobs.sort(key=lambda x : (x[2], x[1]), reverse=True)

res = [-1] * (n + 1)

for cur_job in jobs:
    job_id, deadline, profit = cur_job

    if res[deadline] == -1:
        res[deadline] = profit

no_of_jobs, total_profit = 0, 0

for pro in res:
    if pro != -1:
        no_of_jobs += 1
        total_profit += pro

print([no_of_jobs, total_profit])
```