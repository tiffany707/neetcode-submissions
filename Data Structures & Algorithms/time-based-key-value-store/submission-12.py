class TimeMap:

    def __init__(self):
        self.lookup = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.lookup[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        r = len(self.lookup[key]) -1

        while l < r:
            m = math.ceil((l + r) / 2)

            if self.lookup[key][m][0] > timestamp:
                r =  m - 1
            else:
                l = m
        if not self.lookup[key] or self.lookup[key][l][0]> timestamp:
            return ""
        return self.lookup[key][l][1]

