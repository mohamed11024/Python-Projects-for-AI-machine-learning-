from collections import deque
class stack:
    def __init__(self):
        self.container = deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0
     
    def size(self):
        return len(self.container)


def reverse_string(string):
    s = stack()
    for ch in string:
        s.push(ch)
    
    t = ''
    while s.size() != 0:
        t += s.pop()
    print(t)    

reverse_string("we have")


