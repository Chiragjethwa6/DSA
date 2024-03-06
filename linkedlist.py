class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        new_node = Node(data, self.head)
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
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)    

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
        if index < 0 or index >= self.length():
            raise Exception("The index does not exists")
        if index == 0:
            self.head = self.head.next
        itr = self.head
        c = 0
        while itr:
            if c == index - 1:
                itr.next = itr.next.next
                break
            c += 1
            itr = itr.next

    def insert_at(self, data, index):
        if index < 0 or index >= self.length():
            raise Exception("The index does not exists")
        if index == 0:
            self.insert_at_begining(data)
        itr = self.head
        c = 0
        while itr:
            if c == index - 1:
                new_node = Node(data, itr.next)
                itr.next = new_node
                break
            c += 1
            itr = itr.next    

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
    ll = LinkedList()
    ll.insertValues(["banana","mango","grapes","orange"])
    # ll.printList()
    ll.insert_after_value("mango","apple") # insert apple after mango
    # ll.printList()
    ll.remove_by_value("orange") # remove orange from linked list
    # ll.printList()
    ll.remove_by_value("figs")
    # ll.printList()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.printList()



