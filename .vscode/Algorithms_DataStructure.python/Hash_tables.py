

class Hash_tables:
    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)]

    def get_index(self,key):
        count = 0
        for i in key:
            count += ord(i)
        return count % (self.max)    
    
    def add_element(self,key,val):
        h = self.get_index(key)
        self.arr[h] = val



    def get_element(self,key):
        h = self.get_index(key)
        return  self.arr[h]
    




if __name__ == '__main__':
    t = Hash_tables()
    