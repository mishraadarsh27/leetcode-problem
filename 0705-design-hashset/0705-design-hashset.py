class MyHashSet:
    def __init__(self):
        self.__store = {}
        

    def add(self, key: int) -> None:
        if self.contains(key): return

        self.__store[key] = key
        

    def remove(self, key: int) -> None:
        if not self.contains(key): return

        del self.__store[key]
        

    def contains(self, key: int) -> bool:
        return key in self.__store
