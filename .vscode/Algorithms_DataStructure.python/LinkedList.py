class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
        

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node


    def insert_at_end(self,data):
        itr = self.head 
        if self.head is None:
            self.insert_at_beginning(data)
        else:    

            while itr.next:
                itr = itr.next
            itr.next = Node(data,None)
    def insert_values(self,data_list):
        for data in data_list:
            self.insert_at_beginning(data)        
           
    def get_lenght(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count

    def remove_at(self,index):
        if index <0 or index >= self.get_lenght():
            raise Exception("Invalid index")
        else:
            if index == 0:
                self.head = self.head.next
            else:
                count = 0
                itr = self.head
                while itr:
                    if count == index - 1:
                        itr.next = itr.next.next
                        break
                    itr = itr.next
                    count += 1    
   
    def insert_at(self,index,data):
        if index <0 or index >= self.get_lenght():
            raise Exception("Invalid index")
        else:
            if index == 0:
                self.insert_at_beginning(data)
                return
            else:
                count = 0
                itr = self.head
                while itr:
                    if count == index - 1:
                        node = Node(data,itr.next)
                        itr.next = node
                        break
                    itr = itr.next    
                    count += 1



    def print(self):
        if self.head == None:
            print("LinkedList is empty")
            return
        

        itr = self.head
        llstr = ''
        while itr:
            llstr+=str(itr.data) + '---->'
            itr = itr.next
        print(llstr)    

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(3)   
    ll.insert_at_beginning(4)
    ll.insert_at_end(6)
    ll.remove_at(1)
    ll.insert_values(["mm","nn","uu"])
    ll.print()
    print(ll.get_lenght())            
    ll.insert_at(3,8)
    ll.print()