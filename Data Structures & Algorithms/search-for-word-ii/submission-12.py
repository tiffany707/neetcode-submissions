class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        class Trie():
            def __init__(self):
                self.children = {}
                self.isEnd = False
                self.word = ""
            
            def insert(self, word):
                curr = self
                for char in word:
                    if char not in curr.children:
                        curr.children[char] = Trie()
                    curr = curr.children[char]
                curr.isEnd = True
                curr.word = word


        def rec(i, j, n):
            if i < 0 or j < 0 or i >= len(board)  or j >= len(board[0]) or  board[i][j] not in n.children:
                return
            if board[i][j] in n.children:
                if n.children[board[i][j]].isEnd:
                    recList.append(n.children[board[i][j]].word)
                    n.children[board[i][j]].isEnd = False
            temp = board[i][j]
            board[i][j] = "#"
            rec(i + 1, j, n.children[temp])
            rec(i - 1, j, n.children[temp])
            rec(i, j + 1, n.children[temp])
            rec(i, j - 1, n.children[temp])
            board[i][j] = temp

            if not n.children[temp].children:
                del n.children[temp]

            return
            

        ans = []
        recList = []

        myTrie = Trie()
        for word in words:
            myTrie.insert(word) 
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in myTrie.children:
                    recList = []
                    rec(i, j, myTrie)
                    if recList:
                        ans += recList

        return ans
            
           
