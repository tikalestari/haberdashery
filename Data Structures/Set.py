#everything unique
#add
#remove

class Set:
    def __init__(self, l = []):
        self.container = {}
        for item in l:
            self.container[item] = None

    def add(self, element):
        if element in self.container.keys():
            return
        self.container[element] = None

    def remove(self, element):
        if element not in self.container.keys():
            print ("Value not found")
            return
        del self.container[element]

    def print_set(self):
        print(list(self.container.keys()))




s = Set([1,2,3])
s.add(1)
s.add(5)
s.remove(2)

s.print_set()
