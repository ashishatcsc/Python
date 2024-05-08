
class Node:
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
            self.insert_at_begining(data)

    def insert_at(self,place,data):
        if self.head is None:
            self.insert_at_begining(data)
        itr = self.head
        while self.head:
            if itr.data != data:
                itr = itr.next
            else:
                itr.next = self # This code is not correct. 



if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(10)
    ll.insert_at_begining(20)
    ll.insert_at_begining(30)
    ll.insert_at_begining(40)
    ll.print()
    ll.insert_values(["Ashish","Shah","is","a","good","boy"])
    ll.print()

