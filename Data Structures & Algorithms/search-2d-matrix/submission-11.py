class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        while l < r:
            m = math.ceil((l + r) / 2)
            if matrix[m][0] == target:
                return True
            elif target > matrix[m][0]:
                l = m
            else:
                r = m - 1
        
        row = l
        l = 0
        r = len(matrix[0]) - 1
        while l <= r:
            m = (l + r) // 2

            if matrix[row][m] == target:
                return True
            elif target > matrix[row][m] :
                l = m + 1
            else:
                r = m - 1
        return False


