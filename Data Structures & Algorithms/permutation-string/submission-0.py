from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1 = defaultdict(int)
        for key in s1:
            dict1[key] += 1
        dict2 = defaultdict(int)
        l = 0

        for i in range(len(s2)):
            if s2[i] in dict1:
                dict2[s2[i]] += 1
            if i - l + 1 == len(s1):
                print(s2[i])
                print(dict2)
                if dict1 == dict2:
                    return True
                else:
                    if s2[l] in dict1:
                        dict2[s2[l]] -= 1
                    l += 1 
        return False