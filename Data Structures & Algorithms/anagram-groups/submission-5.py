class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = collections.defaultdict(list)
        ans = []
        for s in strs:
            key = "".join(sorted(s))
            lookup[key].append(s)
        for value in lookup.values():
            ans.append(value)
        return ans