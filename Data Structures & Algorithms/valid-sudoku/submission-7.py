class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        lookup = collections.defaultdict(set)
        for i in range(len(board)):
            rows = set()
            cols = set()
            for j in range(len(board)):
                if board[i][j] != ".":
                    #rows
                    if board[i][j] in rows:
                        return False
                    else:
                        rows.add(board[i][j])

                    #square
                    location = (i//3, j//3)
                    if location in lookup:
                        print(location, lookup[location],board[i][j])
                        if board[i][j] in lookup[location]:
                            return False
                    lookup[location].add(board[i][j])

                #cols
                if board[j][i] != ".":
                    if board[j][i] in cols:
                        return False
                    else:
                        cols.add(board[j][i])
                
                
        return True