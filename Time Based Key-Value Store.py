from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.keyStore = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyStore[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.keyStore.get(key)

        if not values or timestamp < values[0][0]:
            return ""

        if timestamp >= values[-1][0]:
            return values[-1][1]

        res = ""
        l, r = 0, len(values) - 1

        while l <= r:
            mid = (l + r) // 2
            mid_timestamp, mid_value = values[mid]

            if mid_timestamp <= timestamp:
                res = mid_value
                l = mid + 1
            else:
                r = mid - 1
        return res


if __name__ == "__main__":
    tm = TimeMap()

    # Example 1
    tm.set("foo", "bar", 1)
    out1 = tm.get("foo", 1)
    out2 = tm.get("foo", 3)
    print("Example 1:")
    print("get(foo, 1) ->", out1, "(expected 'bar')")
    print("get(foo, 3) ->", out2, "(expected 'bar')")
    print()

    # Example 2
    tm.set("foo", "bar2", 4)
    out3 = tm.get("foo", 4)
    out4 = tm.get("foo", 5)
    print("Example 2:")
    print("get(foo, 4) ->", out3, "(expected 'bar2')")
    print("get(foo, 5) ->", out4, "(expected 'bar2')")
