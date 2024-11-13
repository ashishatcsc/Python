class HashTableChainingCollision:  
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        self.count = 0  # Track number of active items
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        for keyvalpair in self.arr[h]:
            if keyvalpair[0] == key:
                return keyvalpair[1]         
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
        if not found:
            self.arr[h].append((key,val))   
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, keyvalpair in enumerate(self.arr[h]):
            if keyvalpair[0] == key:
                print("del",index)
                del self.arr[h][index]  



class HashTableLinearProbing:  
    def __init__(self):
        self.MAX = 10 # I am keeping size very low to demonstrate linear probing easily but usually the size should be high
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:
                return
            if element[0] == key:
                return element[1]
           
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key,val)
        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key,val)
        print(self.arr)
        
    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0,index)]
    
    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
        raise Exception("Hashmap full")
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return # item not found so return. You can also throw exception
            if self.arr[prob_index][0] == key:
                self.arr[prob_index]=None
        print(self.arr)                

if __name__ == "__main__":
    # t = HashTableChainingCollision()
    # t["Jan 1"] = 27
    # t["Jan 2"] = 31
    # t["Jan 3"] = 23
    # t["Jan 4"] = 34
    # t["Jan 5"] = 37
    # t["Jan 6"] = 38
    # t["Jan 7"] = 29
    # t["Jan 8"] = 30
    # t["Jan 9"] = 35
    # t["Jan 10"] = 30
    # print(t.arr)
    # Days = ["Jan 1","Jan 2","Jan 3","Jan 4","Jan 5","Jan 6","Jan 7","Jan 8","Jan 9","Jan 10"]
    # sum = 0
    # count = 0
    # print(len(Days[0:7]))
    # for day in Days:
    #     if count < 7:
    #         sum += t[day]
    #         count +=1
    # print("Average temperature for fist week of Januar is :", sum/7)    
    # max_temp = max(t[day] for day in Days[0:10])
    # print("Maximum temperature between January 1 and January 10 is:", max_temp)


    t = HashTableLinearProbing()
    t["march 6"] = 20
    t["march 17"] =  88
    t["march 17"] = 29
    t["nov 1"] = 1
    t["march 33"] = 234
    print(t["dec 1"])
    print(t["march 33"])
    t["march 33"] = 999
    print(t.arr)
    t["april 1"]=87
    print(t.arr)
    t["april 2"]=123
    print(t.arr)
    t["april 3"]=234234
    print(t.arr)
    t["april 4"]=91
    print(t.arr)
    t["May 22"]=4
    print(t.arr)
    t["May 7"]=47
    print(t.arr)
    t["Jan 1"]=0
    print(t.arr)
    del t["april 2"]
    t["Jan 1"]=0

