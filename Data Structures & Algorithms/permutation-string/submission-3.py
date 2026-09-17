class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lookup = collections.Counter(s1)
        copy = lookup.copy()

        need = len(lookup)
        have = 0
        l = 0


        for r in range(len(s2)):
            if s2[r] in lookup:
                lookup[s2[r]]  -= 1
                if lookup[s2[r]]  == 0:
                    have += 1
                    if have == need:
                        return True
                elif lookup[s2[r]]  < 0:
                    while l < r and lookup[s2[r]] < 0:
                        if s2[l] in lookup:
                            lookup[s2[l]] += 1
                            if lookup[s2[l]] > 0:
                                have -= 1
                        l += 1
            else:
                 lookup = copy.copy()
                 have = 0

        return False