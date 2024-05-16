class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        
        for i, ivl in enumerate(intervals):
            if newInterval[1] < ivl[0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > ivl[1]:
                res.append(ivl)
            else:
                tempInt = [min(newInterval[0], ivl[0]), max(newInterval[1], ivl[1])]
                print([min(newInterval[0], ivl[0]), max(newInterval[1], ivl[1])])
                newInterval = [min(newInterval[0], ivl[0]), max(newInterval[1], ivl[1])]
        
        # if at the last iteration the intervals overlap
        # 1. you create a new extended interval & then loop ends, this new interval in not added to res
        # hence we handle the above edge case
        res.append(newInterval)
        
        return res

# res = Solution().insert([[2,4],[6,8]], [0,1])
# res = Solution().insert([[2,4],[6,8]], [10,12])
res = Solution().insert([[2,4],[6,8],[10,12],[14,16]], [1,9])
print(res)