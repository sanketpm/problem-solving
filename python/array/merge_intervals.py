class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda i : i[10])
        st = 0
        en = 1
        res = []
        newIvl = intervals[0]

        for ivl in intervals:
            if ivl[st] <= newIvl[en]:
                newIvl = [min(ivl[st], newIvl[st]), max(ivl[en], newIvl[en])]
            else:
                res.append(newIvl)
                newIvl = ivl
        
        return res

res = Solution().merge([[1,3],[2,6],[8,10],[15,18]])
print(res)