#Doing many operations on HashTable using 00P
class HashTable:
#function for initializing our class by passing size of array and init array(None) 
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
#function for returnning the index of the key     
    def get_hash(self,key):
        h=0
        for char in key:
            h += ord(char)
        return h % self.MAX
#function for adding item in your array
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        found = False
        for idx,element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
                break
        if not found:        
            self.arr[h].append((key,val))
#function for returnning the item of its key    
    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]
#function for deleting the item of its key   
    def __delitem__(self,key):
        h = self.get_hash(key)
        for idx,element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]
#create object from class HashTable        
t = HashTable()

#Trying our operations
t['march 5'] = 20
t['march 5'] = 30
del t['mrach 5']
print(t.arr)