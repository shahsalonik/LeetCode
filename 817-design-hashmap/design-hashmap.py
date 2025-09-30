class Node:
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:
    # use an array + handle collisions
    # use hash() function for the key to determine the index
    # add to the tail of the list sicne you need to search through
    def __init__(self):
        self.hash_map = []
        for i in range(1000):
            self.hash_map.append(Node())

    def put(self, key: int, value: int) -> None:
        # create hash value of a key
        index = self.hash_map[self.hash(key)]

        while index.next:
            if index.next.key == key:
                index.next.val = value
                return
            index = index.next
        
        index.next = Node(key, value)

    def get(self, key: int) -> int:
        index = self.hash_map[self.hash(key)]

        while index.next:
            if index.next.key == key:
                return index.next.val
            index = index.next
        
        return -1

    def remove(self, key: int) -> None:
        index = self.hash_map[self.hash(key)]

        while index.next:
            if index.next.key == key:
                # relinking here
                index.next = index.next.next
                return
            index = index.next

    def hash(self, key):
        return key % len(self.hash_map)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)