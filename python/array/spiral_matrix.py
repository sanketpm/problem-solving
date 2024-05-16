class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        top, left = 0, 0
        bottom, right = len(matrix) - 1, len(matrix[0]) - 1
        res = []

        while left <= right and top <= bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            
            top += 1

            for i in range(top, bottom):
                res.append(matrix[i][right])
            
            right -= 1

            if not (left <= right and top <= bottom):
                break
            
            for i in range(right, left, -1):
                res.append(matrix[bottom][i])
            
            bottom -= 1

            for i in range(bottom, top, -1):
                res.append(matrix[i][left])
            
            left += 1
        
        return res

res = Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
print(res)