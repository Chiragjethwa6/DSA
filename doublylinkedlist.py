class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        if self.head is None:
            new_node = Node(data, self.head, None)
            self.head = new_node
        else:
            new_node = Node(data, self.head, None)
            self.head.prev = new_node
            self.head = new_node

    def printList(self):
        if self.head is None:
            print("list is empty")
            return
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None, itr)    

    def insertValues(self, datas):
        for data in datas:
            self.insert_at_end(data)      

    def length(self):
        c = 0
        itr = self.head
        while itr:
            c += 1
            itr = itr.next
        print("length : ",c)  
        return c 

    def removeAt(self, index):
        if index < 0 or index > self.length():
            raise Exception("The index does not exists")
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
        itr = self.head
        c = 0
        while itr:
            if c == index - 1:
                itr.next = itr.next.next
               
                itr.next.prev = itr.prev
                break
            c += 1
            itr = itr.next

    def insert_at(self, index,data):
        if index < 0 or index > self.length():
            raise Exception("The index does not exists")
        if index == 0:
            self.insert_at_begining(data)
        itr = self.head
        c = 0
        while itr:
            if c == index - 1:
                new_node = Node(data, itr.next, itr)
                if new_node.next:
                    new_node.next.prev = new_node
                itr.next = new_node
                break
            c += 1
            itr = itr.next   

    def print_forward(self):
        if self.head is None:
            print("list is empty")
            return
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next

    def get_last_noe(self):
        if self.head is None:
            return 
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr    

    def print_bakcward(self):
        last_node = self.get_last_noe()
        while last_node.prev:
            print(last_node.data)
            last_node = last_node.prev    

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            raise Exception("Linkedlist is empty")
        itr = self.head
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)  
                break
            itr = itr.next      

    def remove_by_value(self, data):
        if self.head is None:
            raise Exception("Linkedlist is empty")
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head 
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next           

if __name__ == "__main__": 
    ll = DoublyLinkedList()
    ll.insertValues(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_bakcward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0,"jackfruit")
    ll.print_forward()
    ll.insert_at(6,"dates")
    ll.print_forward()
    ll.insert_at(2,"kiwi")
    ll.print_forward()



