
class Node:   
    def __init__(self, data=None, next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head  = node;  

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr =  self.head
        llstr =  ' '
        while itr:
            llstr += str(itr.data)  +  '-->'
            itr = itr.next
        print(llstr)

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr =  self.get_last_node()
        llstr =  ' '
        while itr:
            llstr += str(itr.data)  +  '-->'
            itr = itr.prev
        print(llstr)   

    def get_last_node(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr =  self.head
        while itr.next:
            itr = itr.next
        return itr        

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at(self,index,data):
        if self.head is None:
            self.insert_at_begining(data)

        if index < 0 or index > self.get_length():
            raise Exception ("Invalid Index") 

        if index == 0:
            self.insert_at_begining(data) 
            return 
        
        count = 0   
        itr = self.head
        while itr:
            if count < index -1:
                itr = itr.next
                count += 1
            else:
                nodetoinsert = Node(data,itr.next,itr)
                itr.next = nodetoinsert
                break

    def insert_at_end(self, data):
        if self.head is None:
            self.head= Node(data,self.head,None)
            return
        itr =  self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None,itr)
        
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
            self.head.prev = None
            return
        
        itr = self.head
        count = 0
        while count < index-1:
            itr = itr.next
            count += 1
        itr.next = itr.next.next   
          

    def insert_after_value(self,value,data):

        if self.head is None:
            raise Exception("List is empty")
                
        count = 0   
        found = False
        itr = self.head
        while itr:
            if itr.data == value:
                NodeToInsert = Node(data,itr.next, itr)
                itr.next = NodeToInsert
                found = True
                break
            else:
                itr = itr.next  
        if found == False:
            print("value povided is not in the list")

    def remove_by_value(self,value):

        if self.head is None:
            raise Exception("List is empty")
                
        count = 0   
        found = False
        itr = self.head
        while itr:
            if itr.data == value:
                self.remove_at(count)                
                found = True
                break
            itr = itr.next
            count += 1
              
        if found == False:
            print("value povided is not in the list")

if __name__ == "__main__":
    ll = DoublyLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0,"jackfruit")
    ll.print_forward()
    ll.insert_at(6,"dates")
    ll.print_forward()
    ll.insert_at(2,"kiwi")
    ll.print_forward()
    ll.remove_at(2)
    ll.print_forward()
    ll.insert_after_value("mango","watermelon")
    ll.print_forward()
    ll.remove_by_value("watermelon")
    ll.print_forward()