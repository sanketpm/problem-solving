class Solution:
    def oneCnt(self, n : int) -> int:
        cnt = 0

        while n != 0:
            cnt += 1
            n = n & n - 1
        
        return cnt


    def countBits(self, n: int) -> int:
        n = 5
        res = []
        for i in range(n + 1):
            print(i)
            res.append(self.oneCnt(i))
        
        return res

# Calling methods
res = Solution().countBits(5)
print(res)
