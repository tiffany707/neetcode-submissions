class WordDictionary:

    def __init__(self):
        self.children = {}
        self.isEnd = False

    def addWord(self, word: str) -> None:
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = WordDictionary()
            curr = curr.children[char]
        curr.isEnd = True

    def search(self, word: str) -> bool:

        def rec(self, word):
            curr = self
            
            for x in range(len(word)):
                if word[x] == '.':
                    for letter in curr.children:
                        if rec(curr.children[letter], word[x+1:]):
                            return True
                if word[x] not in curr.children:
                    return False
                curr = curr.children[word[x]]
            return curr.isEnd
        return rec(self, word)
