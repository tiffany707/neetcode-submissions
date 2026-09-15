class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for k in range(len(matrix[0])): #col
                        if matrix[i][k] != 0:
                            matrix[i][k] = "#"
                    for k in range(len(matrix)): #row
                        if matrix[k][j] != 0:
                            matrix[k][j] = "#"
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "#":
                    matrix[i][j] = 0
            



        