class TimeMap:

    def __init__(self):
        from collections import defaultdict
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if len(self.map[key]) == 0:
            return ""
        min_t = self.map[key][0][1]
        if timestamp < min_t:
            return ""

        l = 0
        r = len(self.map[key]) - 1
        while l <= r: 
            mid = l + (r-l)//2

            mid_timestamp = self.map[key][mid][1]
            if mid_timestamp < timestamp:
                l = mid + 1
            elif mid_timestamp > timestamp: 
                r = mid - 1
            else: 
                return self.map[key][mid][0]
        return self.map[key][l-1][0]

