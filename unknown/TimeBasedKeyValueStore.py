class TimeMap:
    def __init__(self):
        self.h_map = dict()
        self.time_stamps = []

    def set(self, key: str, value: str, timestamp: int) -> None:
        key_time = key + str(timestamp)
        self.h_map[key_time] = value
        self.time_stamps.append(timestamp)

        if key in self.h_map:
            small_stamp = self.h_map[key][-1]
            self.h_map[key].append(value)
            if small_stamp > timestamp:
                self.h_map[key].append(timestamp)
            else:
                self.h_map[key].append(small_stamp)
        else:
            self.h_map[key] = [value, timestamp]
        return

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.h_map:
            return ""
        key_time = key + str(timestamp)

        if self.h_map[key][-1] > timestamp:
            return ""

        if key_time in self.h_map:
            return self.h_map[key_time]
        else:
            return self.find_prev(timestamp, key)

    def find_prev(self, timestamp: int, key: str) -> str:
        if timestamp < self.time_stamps[0]:
            return ""
        elif timestamp > self.time_stamps[-1]:
            return self.h_map[key][-2]
        else:
            low, high = 0, len(self.time_stamps) - 1

            while low <= high:
                mid = (low + high) // 2
                if self.time_stamps[mid] < timestamp:
                    low = mid + 1
                else:
                    high = mid - 1
            key_stamp = key + str(self.time_stamps[high])
            return self.h_map[key_stamp] if key_stamp in self.h_map else ""


obj = TimeMap()
method_calls = ["TimeMap", "set", "set", "get", "set", "get", "get"]
params = [
    [],
    ["a", "bar", 1],
    ["x", "b", 3],
    ["b", 3],
    ["foo", "bar2", 4],
    ["foo", 4],
    ["foo", 5],
]
# param_2 = obj.get(key,timestamp)
for i in range(len(method_calls)):
    method = method_calls[i]
    param = params[i]

    # Call the appropriate method
    if method == "set":
        print(obj.set(*param))
    elif method == "get":
        print(obj.get(*param))
