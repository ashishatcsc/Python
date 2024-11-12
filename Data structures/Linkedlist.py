
class Node:
    data = None
    next = None
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data,  self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr =  self.head
        llstr =  ' '
        while itr:
            llstr += str(itr.data)  +  '-->'
            itr = itr.next
        print(llstr)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at(self,place,data):
        if self.head is None:
            self.insert_at_begining(data)

        if place < 0 or place > self.get_length():
            raise Exception ("Invalid Index") 

        count = 0   
        itr = self.head
        while itr:
            if count < place -1:
                itr = itr.next
                count += 1
            else:
                nodetoinsert = Node(data,itr.next)
                itr.next = nodetoinsert
                break

    def insert_at_end(self, data):
        if self.head is None:
            self.head= Node(data,None)
            return
        itr =  self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
        
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self,index):
        if index<0 or index > self.get_length():
            raise Exception("Invalid index; not within the bounds of Linked List")
            
        if index == 0:
            self.head = self.head.next
            return
        
        itr = self.head
        count = 0
        while count < index-1:
            itr = itr.next
            count += 1
        itr.next = itr.next.next    
        

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(10)
    ll.insert_at_begining(20)
    ll.insert_at_begining(30)
    ll.insert_at_begining(40)
    ll.print()
    ll.insert_at(3,45)
    ll.print()
    ll.insert_values(["Ashish","Shah","is","a","good","boy"])
    ll.insert_at_end(99)
    ll.print()
    print("Length of the list is:", ll.get_length())
    ll.remove_at(2)
    ll.print()
    