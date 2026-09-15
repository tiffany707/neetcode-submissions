class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def rec(i, j, t):
            if t == len(word):
                return True
            if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0 or board[i][j] != word[t]:
                return False
            
            temp = board[i][j]
            board[i][j] = "#"  # Mark as visited
            
            # Explore all 4 directions
            found = (
                rec(i + 1, j, t + 1) or 
                rec(i - 1, j, t + 1) or 
                rec(i, j + 1, t + 1) or 
                rec(i, j - 1, t + 1)
            )
            
            board[i][j] = temp  # Backtrack
            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if rec(i, j, 0):
                        return True

        return False