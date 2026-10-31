class MyCircularQueue(object):
    def __init__(self, k):
        self.queue = [0] * k 
        self.front = -1 
        self.rear = -1
        self.size = 0 
        self.capacity = k
        

    def enQueue(self, value):
        if self.isFull() :
            return False 
        if self.isEmpty() :
            self.front = 0 
            self.rear = 0 
        else :
            self.rear = (self.rear + 1) % self.capacity 
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        
        if self.rear == self.front : # means queue is empty 
            self.rear = -1
            self.front = -1 
        else :
            self.front = (self.front + 1) % self.capacity
        
        self.size -= 1 
        return True 

    def Front(self):
        if self.isEmpty() :
            return -1
        return self.queue[self.front]
        

    def Rear(self):
        if self.isEmpty() :
            return -1
        return self.queue[self.rear]
        

    def isEmpty(self):
        return self.size == 0
        

    def isFull(self):
        return self.size == self.capacity
        


# Your MyCircularself.queue object will be instantiated and called as such:
# obj = MyCircularself.queue(k)
# param_1 = obj.enself.queue(value)
# param_2 = obj.deself.queue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()