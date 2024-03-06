class hashtable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)] 

    def get_hash(self, key):
        h = 0
        for i in key:
            h += ord(i)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        print(h)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break    
        if not found:     
            self.arr[h].append((key,value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                return element[1]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]

if __name__ == "__main__":
    hash = hashtable()
    hash["march 6"] = 10
    hash["march 1"] = 11
    print(hash.arr)    
    hash["march 17"] = 12
    print(hash.arr)    
    del hash["march 17"]    
    print(hash.arr)
    print(hash["march 17"])

