class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key] = self.store.get(key, [])
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.store.get(key, []); res = ""
        if len(arr):
            s = 0; e = len(arr) - 1
            while s <= e:
                mid = (s + e)//2
                if arr[mid][1] <= timestamp:
                    res = arr[mid][0]; s = mid + 1
                else:
                    e  = mid - 1
            return res
        else:
            return ""
        
