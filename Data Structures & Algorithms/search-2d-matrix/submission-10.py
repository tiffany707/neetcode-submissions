import math
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #ROW

        top, bot = 0, len(matrix) - 1

        while top <= bot:
            m = (top + bot) // 2
            if target > matrix[m][len(matrix[0])-1]:
                top = m + 1
            elif target < matrix[m][0]:
                bot = m -1
            else:
                break
            
        if top > bot:
            return False
        else:
            row = (top + bot) //2
            l, r = 0, len(matrix[0]) - 1
            while l <= r:
                m = (l + r) //2
                if target > matrix[row][m]:
                    l = m + 1
                elif target < matrix[row][m]: 
                    r = m - 1
                else:
                    return True
        return False

        

        