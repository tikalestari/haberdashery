
class HashTable:
    def __init__(self, container_size, load_factor):
        self.container_size = container_size
        self.container = [[] for i in range(container_size)]
        self.count = 0
        self.load_factor = load_factor

    def insert(self, key, value):
        index = hash(key) % self.container_size
        for pair in self.container[index]:
            if pair[0] == key:
                pair[1] = value
                return

        self.container[index].append([key,value])
        self.count += 1
        if self.count / len(self.container) > self.load_factor:
            self.redistribute()

    def get(self, key):
        index = hash(key) % self.container_size
        for pair in self.container[index]:
            if pair[0] == key:
                return pair[1]
        return -1

    def delete(self,key):
        index = hash(key) % self.container_size
        for i in range(len(self.container[index])):
            if self.container[index][i][0] == key:
                self.container[index].pop(i)
                return

    def redistribute(self):
        new_container = [[] for i in range(2*len(self.container))]
        for index in range(len(self.container)):
            for pair in self.container[index]:
                new_index = hash(pair[0]) % len(new_container)
                new_container[new_index].append(pair)
        self.container = new_container
        self.container_size *= 2

h = HashTable(3,4)
h.insert("Tika",1)
h.insert("Cameron",2)
h.delete("Tika")
print(h.container)
