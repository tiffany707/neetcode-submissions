class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        lookup = {}
        words = set(wordDict)  # Turn list into a set for O(1) lookups!

        def rec(i):
            # 1. Base case: If we reach the end of the string, we successfully broke it!
            if i == len(s):
                return True
            
            # 2. Check the whiteboard
            if i in lookup:
                return lookup[i]
            
            # 3. Try every word in the dictionary to see if it matches starting at index i
            for w in words:
                length = len(w)
                # Check if the word fits and matches the slice of s starting at i
                if i + length <= len(s) and s[i : i + length] == w:
                    # If this path works, save it and return True
                    if rec(i + length):
                        lookup[i] = True
                        return True
            
            # 4. If no words worked from this index, cache it as False and return
            lookup[i] = False
            return False

        # Start our search at index 0
        return rec(0)