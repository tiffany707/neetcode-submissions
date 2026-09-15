from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dict = defaultdict(int)

        for row in board:
            mySet = set()
            for num in row:
                if num in mySet and num != ".":
                    print("bye")
                    return False
                else:
                    mySet.add(num)
        
        for i in range(len(board)):
            mySet = set() 
            for j in range(len(board)):
                if board[j][i] in mySet and board[j][i] != ".":
                    print("hi")
                    return False
                else:
                    mySet.add(board[j][i])
        for x in range(3):
            for i in range(3):
                mySet = set()
                for j in range(3):
                    for k in range(3):
                        if board[x*3 + j][i*3 + k] in mySet and board[x*3 + j][i*3 + k] != ".":
                            print("yo", mySet)
                            print(board[x*3 + j], board[x*3 + j][i*3 + k])
                            return False
                        else:
                            mySet.add(board[x*3 + j][i*3 + k])
                print(mySet)
        return True


        
