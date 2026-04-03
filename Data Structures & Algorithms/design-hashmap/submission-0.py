

class MyHashMap:

    def __init__(self):
        self.map = [[] for _ in range(10000)]

    def hash_key(self,key):
        return key%10000    
        

    def put(self, key: int, value: int) -> None:
        index = self.hash_key(key)
        for i in range(len(self.map[index])):
            if self.map[index][i][0] == key:
                self.map[index][i][1] = value
                return
        self.map[index].append([key,value])        

    def get(self, key: int) -> int:
        index = self.hash_key(key)
        for i in range(len(self.map[index])):
            if self.map[index][i][0] == key:
                return self.map[index][i][1] 
        return -1 
        

    def remove(self, key: int) -> None:
        index = self.hash_key(key)
        for i in range(len(self.map[index])):
            if self.map[index][i][0] == key:
                self.map[index].pop(i)
                return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)