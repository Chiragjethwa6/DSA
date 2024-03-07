from collections import deque
import time
import threading

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.appendleft(data)

    def dequeue(self):
        if len(self.queue)==0:
            print("Queue is empty")
            return
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0   

    def front(self):
        return self.queue[-1]

    def binary_numbers(self, n):
        self.enqueue("1")
        for i in range(n):
            front = self.front()
            print(front)
            self.enqueue(front + "0")
            self.enqueue(front + "1")
            self.dequeue()
    
q = Queue()
# q.binary_numbers(10)   

def placeOrder(orders):
    for order in orders:
        print("placing order for : ", order)
        q.enqueue(order)
        time.sleep(0.5)

def serverOrder():
    time.sleep(1)
    while True:
        order = q.dequeue()
        print("serving the order : ", order)
        time.sleep(2)        
               
if __name__ == "__main__":
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=placeOrder, args=(orders,))
    t2 = threading.Thread(target = serverOrder)  
    t1.start()
    t2.start()   