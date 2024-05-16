class Solution:
    def rotate(self, mat: list[list[int]]) -> None:
        n = len(mat)

        l, r = n - 1, n - 1

        while l <= r:
            t, b = l, r 
            length = r - l

            for i in range(length):
                topLeft = mat[t][l + i]
                mat[t][l + i] = mat[b - i][l]
                mat[b - i][l] = mat[b][r - i]
                mat[b][r - i] = mat[t + i][r]
                mat[t + i][r] = topLeft
            
            l += 1
            r -= 1
    
res = Solution().rotate([[1,2,3],[4,5,6],[7,8,9]])