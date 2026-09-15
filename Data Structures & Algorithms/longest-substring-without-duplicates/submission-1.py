class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        curRes = 0
        mySet = set()
        window = [0, 0]

        for key in s:
            print(key)
            print(mySet)
            print(curRes)
            if key in mySet:
                while True:
                    i = window[0]
                    window[0] = window[0] + 1
                    if s[i] == key:
                        break
                    else:
                        mySet.remove(s[i]) 
                        curRes -= 1
            else:
                mySet.add(key)
                window[1] += 1
                curRes += 1
                if curRes > res:
                    print("hi", curRes)
                    res = curRes
                    print("bye",res)
        return res

        