arr = []
d = {}
c = {}
with open("nyc_weather.csv", "r") as file:
    for line in file:
        a = line.split(",")
        try:
            key = a[0]
            numbers = int(a[1])
            d[key] = numbers
            arr.append(numbers)
        except:
            print("not valid. ignore the row")    
    avg = sum(arr[:7])/7     
    m = max(arr)

with open("poem.txt","r") as f:
    for line in f:
        sentence = line.split(" ")   
        for word in sentence:
            word = word.replace("\n","")
            if word in c:
                c[word] += 1
            else:
                c[word] = 1      

class hashtable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)] 

    def get_hash(self, key):
        h = 0
        for i in key:
            h += ord(i)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key,value)
        else:
            new_h = self.getSlots(key, h)
            self.arr[new_h] = (key,value)
        print(self.arr)    

    def getSlots(self, key, index):
        prob_range = self.getProbRange(index)
        for i in prob_range:
            if self.arr[i] is None:
                return i
            if self.arr[i][0] == key:
                return i
        raise Exception("Hashmap Full") 

    def getProbRange(self, index):
        return [*range(index, len(self.arr))] + [*range(0, index)]
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        prob_range = self.getProbRange(h)
        for i in prob_range:
            element = self.arr[i]
            if element is None:
                return
            if element[0] == key:
                print(element[1])
            
    def __delitem__(self, key):
        h = self.get_hash(key)
        prob_range = self.getProbRange(h)
        for i in prob_range:
            if self.arr[i] is None:
                return
            if self.arr[i][0] == key:
                self.arr[i] = None
        print(self.arr)        

if __name__ == "__main__":
    t = hashtable()
    t["march 6"] = 20
    t["march 17"] =  88
    t["march 17"] = 29
    t["nov 1"] = 1
    t["march 33"] = 234
    t["dec 1"]
    t["march 33"]
    t["march 33"] = 999
    t["march 33"]
    t["april 1"]=87
    t["april 2"]=123
    t["april 3"]=234234
    t["april 4"]=91
    t["May 22"]=4
    t["May 7"]=47
    del t["april 2"]
    print(t.arr)
    t["Jan 1"]=0