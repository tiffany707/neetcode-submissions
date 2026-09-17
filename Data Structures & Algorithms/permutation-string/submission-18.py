class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        lookup1 = [0] * 26
        lookup2 = [0] * 26
        match = 0

        for s in s1:
            num = ord(s) - 97
            lookup1[num] += 1
        

        for i in range(len(s1)):
            num = ord(s2[i]) - 97
            lookup2[num] += 1

        for i in range(len(lookup1)):
            if lookup1[i] == lookup2[i]:
                match += 1
        l = 0
        for r in range(len(s1), len(s2)):
            if  match == 26:
                return True
            else:
                lookup2[ord(s2[r])-97] += 1
                if lookup2[ord(s2[r])-97] == lookup1[ord(s2[r])-97]:
                    match += 1
                elif lookup2[ord(s2[r])-97] == lookup1[ord(s2[r])-97] + 1:
                    match -= 1
                lookup2[ord(s2[l])-97] -= 1
                if lookup1[ord(s2[l])-97] == lookup2[ord(s2[l])-97]:
                    match += 1
                elif lookup1[ord(s2[l])-97] - 1 == lookup2[ord(s2[l])-97]:
                    match -= 1
                l += 1
                print(s2[r], match)
        if  match == 26:
                return True
        return False
        



        
        