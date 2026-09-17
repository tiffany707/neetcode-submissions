class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        lookup = [0] * 10
        #row
        for i in range(len(board)):
            lookup = [0] * 10
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    lookup[int(board[i][j])] += 1
                    if lookup[int(board[i][j])] > 1:
                        return False
        
        #col
        lookup = [0] * 10
        for i in range(len(board)):
            lookup = [0] * 10
            for j in range(len(board[0])):
                if board[j][i] != ".":
                    lookup[int(board[j][i])] += 1
                    if lookup[int(board[j][i])] > 1:
                        return False
        
        #square
        lookup = collections.defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != ".":
                    print(lookup[(0,0)])
                    if board[i][j] in lookup[(i//3, j//3)]:
                        return False
                    lookup[(i//3, j//3)].add(board[i][j])
        return True
            