class LRUCache:

    def __init__(self, capacity: int):
        # print(capacity)
        self.capacity = capacity
        self.cache = {}

    def __inc_response_time(self):
        for key in self.cache:
            self.cache[key][1] += 1

    def get(self, key: int) -> int:
        self.__inc_response_time()

        # print(key, "get"); print(self.cache)

        res = self.cache.get(key, None)
        if res is not None:
            self.cache[key][1] = 0; return res[0]
        return -1

    def put(self, key: int, value: int) -> None:
        self.__inc_response_time()

        # print(key, value, "put")

        items = list(self.cache.items())
        if len(items) >= self.capacity and key not in self.cache:
            # Removing least recently used key
            LRU_key = max(items, key = lambda x : x[1][1])[0]; self.cache.pop(LRU_key, None)
        self.cache[key] = [value, 0]
        # print(self.cache)
