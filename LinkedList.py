class Node :
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
        
        

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self,data):
        if self.head == None:
            self.head = self.tail = Node(data)
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
    def display(self):
        current = self.head
        while current:
            print(current.data,end="-")
            current = current.next
        
        
        
l = LinkedList()
l.insert(1)
l.insert(2)
l.insert(3)

l.display()
        
        
        
        